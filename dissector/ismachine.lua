ismachine_protocol = Proto("ismachine", "IsMachine Protocol")
ismachine_protocol.fields = {}
ismachine_protocol.fields.generated_by = ProtoField.string("ismachine.generated_by", "Generated by")
ismachine_protocol.fields.probability = ProtoField.string("ismachine.probability", "Probability")

cached_result = {}

function ismachine_protocol.dissector(buffer, pinfo, tree)
  -- Set name in protocol column
  pinfo.cols.protocol = ismachine_protocol.name

  -- Get packet info
  local args = {}

  -- Get inference result
  local result = cached_result[pinfo.number]
  if not result then
    result = infer(args)
    cached_result[pinfo.number] = result
  end

  -- Get fields
  local machine_generated_probability = tonumber(result)
  local generated_by = machine_generated_probability >= 0.5 and "Machine" or "Human"
  local probability = machine_generated_probability >= 0.5 and machine_generated_probability or 1 - machine_generated_probability

  -- Add subtree
  local subtree = tree:add(ismachine_protocol, buffer(), "IsMachine Protocol Data")
  subtree:add(ismachine_protocol.fields.generated_by, generated_by)
  subtree:add(ismachine_protocol.fields.probability, probability)
end

DissectorTable.get("tcp.port"):add(80, ismachine_protocol)
DissectorTable.get("udp.port"):add(1900, ismachine_protocol)

-- Helpers
function infer(args)
  local windows_command = 'cd "C:/Program Files/Wireshark/plugins/" && python inference.py'
  local unix_command = "python3 ~/.local/lib/wireshark/plugins/inference.py"
  local command = package.config:sub(1,1) == "\\" and windows_command or unix_command
  local command_args = " " .. table.concat(args, " ")
  local handle = io.popen(command .. command_args, "r")
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
