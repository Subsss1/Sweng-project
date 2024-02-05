import pyshark
import csv

input_path = './example.pcapng'
output_path = './output.csv'

header = ['ipv', 'proto', 'src', 'dst', 'srcport', 'dstport']

with open(output_path, 'w') as output:
  capture = pyshark.FileCapture(input_path, display_filter='tcp or udp')
  writer = csv.writer(output)
  writer.writerow(header)

  for packet in capture:
    ip_version = 'ipv6' if hasattr(packet, 'ipv6') else 'ip' 
    transport_layer = packet.transport_layer

    ipv = 6 if ip_version == 'ipv6' else 4
    proto = 6 if packet.transport_layer == 'TCP' else 17
    src = packet[ip_version].src
    dst = packet[ip_version].dst
    srcport = packet[transport_layer].srcport
    dstport = packet[transport_layer].dstport

    writer.writerow([ipv, proto, src, dst, srcport, dstport])
