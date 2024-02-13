ismachine_protocol = Proto("ismachine", "IsMachine Protocol")

ismachine_protocol.fields = {}
ismachine_protocol.fields.is_machine_generated =  ProtoField.bool("machine.is_machine_generated", "Is Machine Generated")

function ismachine_protocol.dissector(buffer, pinfo, tree)
  pinfo.cols.protocol = ismachine_protocol.name

  local subtree = tree:add(ismachine_protocol, buffer(), "IsMachine Protocol Data")

  subtree:add(ismachine_protocol.fields.is_machine_generated, true)
end

local udp_table = DissectorTable.get("udp.port")

udp_table:add(1900, ismachine_protocol)
