-- the protocol
local machine_or_humam_protocol = Proto("machine_or_human", "machine or human generated protocol")

-- the fields
local fields = {}

local time = Protofield.uint16("protocol.time", "Time")
local src = Protofield.string("protocol.src", "Source")
local dst = Protofield.string("protocol.dst", "Destination")
local len = Protofield.string("protocol.len", "Length")
local src_port = Protofield.string("protocol.src_port", "Source Port")
local dst_port = Protofield.string("protocol.dst_port", "Destination Port")

local machine_or_human.fields = { time, src, dst, len, src_port, dst_port }

-- dissector method
function machine_or_human_protocol.dissector(buffer, pinfo, tree)
  pinfo.cols['protocol'] = "machine_or_human_generated"
  local subtree = tree:add(machine_or_humam_protocol, buffer())
  local offset = 0

  local length = buffer(0,8):uint()
   if buffer:len() < length then
      pinfo.length = length + 2 - buffer:len()
      return

end


-- register the protocol
local udp_port = -- port ID 
local udp_table = DissectorTable.get("udp.port")

-- print result
local machine_or_human_result = math.random(0,1)  --simulate result
print(machine_or_human_result)

