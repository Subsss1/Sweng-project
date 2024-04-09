ismachine_protocol = Proto("ismachine", "IsMachine Protocol")
ismachine_protocol.fields = {}
ismachine_protocol.fields.generated_by = ProtoField.string("ismachine.generated_by", "Generated by")
ismachine_protocol.fields.probability = ProtoField.string("ismachine.probability", "Probability")

global_flow = { duration = 0, last_timestamp = 0, average_length = 0 }
flows = {}
results = {}

function ismachine_protocol.dissector(buffer, pinfo, tree)
  local number = pinfo.number
  local packet_type = buffer(12, 2):uint()
  local protocol_number = buffer(23, 1):uint()
  local is_ipv4 = packet_type == 2048
  local is_ipv6 = packet_type == 34525
  local is_tcp = protocol_number == 6
  local is_udp = protocol_number == 17

  if(not (is_ipv4 and (is_tcp or is_udp))) then
    return
  end

  if results[number] == nil then
    local source            = tostring(pinfo.src)
    local destination       = tostring(pinfo.dst)
    local source_port       = tonumber(pinfo.src_port)
    local destination_port  = tonumber(pinfo.dst_port)
    local protocol          = tonumber(protocol_number)
    local length            = tonumber(pinfo.len)
    local timestamp         = tonumber(pinfo.rel_ts)

    local params = get_params(number, source, destination, source_port, destination_port, protocol, length, timestamp)
    results[number] = infer(params)
  end

  local is_machine_probability = tonumber(results[number])

  if is_machine_probability == nil or is_machine_probability < 0 then
    return
  end

  local generated_by = is_machine_probability >= 0.5 and "Machine" or "Human"
  local probability = is_machine_probability >= 0.5 and is_machine_probability or 1 - is_machine_probability

  local subtree = tree:add(ismachine_protocol, buffer(), "IsMachine Protocol Data")
  subtree:add(ismachine_protocol.fields.generated_by, generated_by)
  subtree:add(ismachine_protocol.fields.probability, probability)
end

function get_params(number, source, destination, source_port, destination_port, protocol, length, timestamp)
  local params = {
    source_port           = source_port,
    destination_port      = destination_port,
    protocol              = protocol,
    length                = length,
    length_deviation      = 0,
    delta_time            = 0,
    flow_average_length   = length,
    flow_length_deviation = 0,
    flow_delta_time       = 0
  }

  if global_flow.duration > 0 then
    params.length_deviation = math.abs(length - global_flow.average_length)
    params.delta_time = math.abs(timestamp - global_flow.last_timestamp)
  
    global_flow = {
      duration       = global_flow.duration + 1,
      last_timestamp = timestamp,
      average_length = (global_flow.average_length * global_flow.duration + length) / (global_flow.duration + 1),
    }
  else
    global_flow = {
      duration       = 1,
      last_timestamp = timestamp,
      average_length = length,
    }
  end

  local flow = source .. "," .. source_port .. "," .. destination .. "," .. destination_port .. "," .. protocol

  if flows[flow] ~= nil then
    params.flow_delta_time = math.abs(timestamp - flows[flow].last_timestamp)
    params.flow_length_deviation = math.abs(length - flows[flow].average_length)
    params.flow_average_length = (flows[flow].average_length * flows[flow].duration + length) / (flows[flow].duration + 1)

    flows[flow] = {
      duration       = flows[flow].duration + 1,
      last_timestamp = timestamp,
      average_length = params.flow_average_length,
    }
  else
    flows[flow] = {
      duration       = 1,
      last_timestamp = timestamp,
      average_length = length,
    }
  end

  return {
    number                = tostring(number),
    flow                  = tostring(flow),
    source_port           = tostring(params.source_port),
    destination_port      = tostring(params.destination_port),
    protocol              = tostring(params.protocol),
    length                = tostring(params.length),
    length_deviation      = string.format("%.8f", params.length_deviation),
    delta_time            = string.format("%.8f", params.delta_time),
    flow_average_length   = string.format("%.8f", params.flow_average_length),
    flow_length_deviation = string.format("%.8f", params.flow_length_deviation),
    flow_delta_time       = string.format("%.8f", params.flow_delta_time),
  }
end

function infer(params)
  local url = 'http://localhost:13131/infer'
  local query_params = string.format(
    '?number=%s&flow=%s&source_port=%s&destination_port=%s&protocol=%s&length=%s&length_deviation=%s&delta_time=%s&flow_average_length=%s&flow_length_deviation=%s&flow_delta_time=%s',
    params.number,
    params.flow,
    params.source_port,
    params.destination_port,
    params.protocol,
    params.length,
    params.length_deviation,
    params.delta_time,
    params.flow_average_length,
    params.flow_length_deviation,
    params.flow_delta_time
  )

  local handle = io.popen("curl -s " .. '"' .. url .. query_params .. '"')
  local result = handle:read("*a")
  handle:close()

  return result
end

register_postdissector(ismachine_protocol)
return ismachine_protocol
