import pyshark
import csv

input_path = './convert/example.pcapng'
output_path = './output.csv'

header = ['ipv', 'src', 'dst', 'srcport', 'dstport', 'length', 'proto']

with open(output_path, 'w') as output:
  capture = pyshark.FileCapture(input_path, display_filter='tcp or udp')
  writer = csv.writer(output)
  writer.writerow(header)

  for packet in capture:
    ip_version = 'ipv6' if hasattr(packet, 'ipv6') else 'ip' 
    transport_layer = packet.transport_layer

    ipv = 6 if ip_version == 'ipv6' else 4
    src = packet[ip_version].src
    dst = packet[ip_version].dst
    srcport = packet[transport_layer].srcport
    dstport = packet[transport_layer].dstport
    length = packet.length
    proto = 6 if packet.transport_layer == 'TCP' else 17

    writer.writerow([ipv, src, dst, srcport, dstport, length, proto])
