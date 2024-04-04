ismachine_protocol = Proto("ismachine", "IsMachine Protocol")
ismachine_protocol.fields = {}
ismachine_protocol.fields.generated_by = ProtoField.string("ismachine.generated_by", "Generated by")
ismachine_protocol.fields.probability = ProtoField.string("ismachine.probability", "Probability")

global_flow = { duration = 0, last_timestamp = 0, average_length = 0 }
flows = {}
results = {}

function ismachine_protocol.dissector(buffer, pinfo, tree)
  local packet_type = buffer(12, 2):uint()
  local protocol_number = buffer(23, 1):uint()
  local is_ipv4 = packet_type == 2048
  local is_ipv6 = packet_type == 34525
  local is_tcp = protocol_number == 6
  local is_udp = protocol_number == 17

  if(not (is_ipv4 and (is_tcp or is_udp))) then
    return
  end

  if results[pinfo.number] == nil then
    local source            = tostring(pinfo.src)
    local destination       = tostring(pinfo.dst)
    local source_port       = tonumber(pinfo.src_port)
    local destination_port  = tonumber(pinfo.dst_port)
    local protocol          = tonumber(protocol_number)
    local length            = tonumber(pinfo.len)
    local timestamp         = tonumber(pinfo.rel_ts)

    local features = get_features(source, destination, source_port, destination_port, protocol, length, timestamp)
    results[pinfo.number] = infer(features)
  end

  local is_machine_probability = tonumber(results[pinfo.number])

  if is_machine_probability == nil or is_machine_probability < 0 then
    return
  end

  local generated_by = is_machine_probability >= 0.5 and "Machine" or "Human"
  local probability = is_machine_probability >= 0.5 and is_machine_probability or 1 - is_machine_probability

  local subtree = tree:add(ismachine_protocol, buffer(), "IsMachine Protocol Data")
  subtree:add(ismachine_protocol.fields.generated_by, generated_by)
  subtree:add(ismachine_protocol.fields.probability, probability)
end

function get_features(source, destination, source_port, destination_port, protocol, length, timestamp)
  local features = {
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
    features.length_deviation = math.abs(length - global_flow.average_length)
    features.delta_time = math.abs(timestamp - global_flow.last_timestamp)
  
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
    features.flow_delta_time = math.abs(timestamp - flows[flow].last_timestamp)
    features.flow_length_deviation = math.abs(length - flows[flow].average_length)
    features.flow_average_length = (flows[flow].average_length * flows[flow].duration + length) / (flows[flow].duration + 1)

    flows[flow] = {
      duration       = flows[flow].duration + 1,
      last_timestamp = timestamp,
      average_length = features.flow_average_length,
    }
  else
    flows[flow] = {
      duration       = 1,
      last_timestamp = timestamp,
      average_length = length,
    }
  end

  return { 
    tostring(features.source_port),
    tostring(features.destination_port),
    tostring(features.protocol),
    tostring(features.length),
    string.format("%.8f", features.length_deviation),
    string.format("%.8f", features.delta_time),
    string.format("%.8f", features.flow_average_length),
    string.format("%.8f", features.flow_length_deviation),
    string.format("%.8f", features.flow_delta_time),
  }
end

function infer(args)
  local windows_command = 'cd "C:/Program Files/Wireshark/plugins/" && python inference.py'
  local unix_command = 'cd ~/.local/lib/wireshark/plugins/ && python inference.py'
  local command = (package.config:sub(1,1) == '\\' and windows_command or unix_command) .. ' ' .. table.concat(args, " ")
  local handle = io.popen(command, "r")
  local output = handle:read("*a")
  handle:close()

  return remove_last_line(output)
end

function remove_last_line(str)
  local last_line_index = str:find("\n[^\n]*$")

  if last_line_index then
    return str:sub(1, last_line_index - 1)
  else
    return ""
  end
end

register_postdissector(ismachine_protocol)
return ismachine_protocol
