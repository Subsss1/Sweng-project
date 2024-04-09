ismachine_protocol = Proto("ismachine", "IsMachine Protocol")

ismachine_protocol.fields = {}
ismachine_protocol.fields.is_machine_generated = ProtoField.bool("machine.is_machine_generated", "Is Machine Generated")

function ismachine_protocol.dissector(buffer, pinfo, tree)
  pinfo.cols.protocol = ismachine_protocol.name

  local subtree = tree:add(ismachine_protocol, buffer(), "IsMachine Protocol Data")

  -- You should replace "Traffic data" with actual data from your packet
  local traffic_data = "Traffic data"
  
  local response = send_request(traffic_data)
  local is_machine_generated = response.is_machine_generated
  
  subtree:add(ismachine_protocol.fields.is_machine_generated, is_machine_generated)
end

local udp_table = DissectorTable.get("udp.port")

udp_table:add(1900, ismachine_protocol)

-- Function to send HTTP request to Python API
function send_request(traffic_data)
  local http = require("socket.http")
  local ltn12 = require("ltn12")
  local json = require("json")

  local payload = json.encode({traffic_data = traffic_data})
  local response_body = {}
  local res, code, response_headers = http.request {
    url = "http://127.0.0.1:5000/is_machine_generated",
    method = "POST",
    headers = {
      ["Content-Type"] = "application/json",
      ["Content-Length"] = payload:len()
    },
    source = ltn12.source.string(payload),
    sink = ltn12.sink.table(response_body)
  }
  
  if code == 200 then
    return json.decode(table.concat(response_body))
  else
    return {is_machine_generated = false}
  end
end
