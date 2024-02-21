ismachine_protocol = Proto("ismachine", "IsMachine Protocol")
ismachine_protocol.fields = {}
ismachine_protocol.fields.is_machine_generated = ProtoField.bool("ismachine.is_machine_generated", "Is Machine Generated")
ismachine_protocol.fields.is_machine_generated_probability = ProtoField.string("ismachine.is_machine_generated_probability", "Is Machine Generated Probability")

function ismachine_protocol.dissector(buffer, pinfo, tree)
  -- Set name in "Protocol" column
  pinfo.cols.protocol = ismachine_protocol.name

  -- Add subtree in packet info
  local subtree = tree:add(ismachine_protocol, buffer(), "IsMachine Protocol Data")

  -- Get packet info
  local args = {} 

  -- Execute model
  local inference_output = infer(args)
  local is_machine_generated_probability = inference_output
  local is_machine_generated = tonumber(is_machine_generated_probability) >= 0.5

  -- Add fields
  subtree:add(ismachine_protocol.fields.is_machine_generated, is_machine_generated)
  subtree:add(ismachine_protocol.fields.is_machine_generated_probability, is_machine_generated_probability)
end

local udp_table = DissectorTable.get("udp.port")
udp_table:add(1900, ismachine_protocol)

----- Helpers -----
function infer(args)
  local command = "python3 ~/.local/lib/wireshark/plugins/inference.py " .. table.concat(args, " ")
  print(command)
  local handle = io.popen(command,"r")
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

----- Helpers -----
function infer(args)
  local command = "python3 ~/.local/lib/wireshark/plugins/inference.py " .. table.concat(args, " ")
  print(command)
  local handle = io.popen(command,"r")
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
