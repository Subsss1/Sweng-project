from functools import reduce
import pyshark
import csv

input_path = './example.pcapng'
output_path = './output.csv'
rows = []
flows = {}
keys = []

header = ['ipv', 'deltatime', 'src', 'dst', 'srcport', 'dstport', 'length', 'proto', 'human']

def from_string(s):
    "Convert dotted IPv4 address to integer."
    return reduce(lambda a,b: a<<8 | b, map(int, s.split(".")))

with open(output_path, 'w') as output:
    capture = pyshark.FileCapture(input_path, display_filter='tcp or udp')
    writer = csv.writer(output)
    rows.append(header)

    for packet in capture:
        ip_version = 'ipv6' if hasattr(packet, 'ipv6') else 'ip'
        ipv = 6 if ip_version == 'ipv6' else 4
        if ipv == 6:
            continue
        transport_layer = packet.transport_layer
        src = packet[ip_version].src
        src = from_string(src)
        dst = packet[ip_version].dst
        dst = from_string(dst)
        srcport = packet[transport_layer].srcport
        dstport = packet[transport_layer].dstport
        length = packet.length
        proto = 6 if packet.transport_layer == 'TCP' else 17
        time = packet.sniff_time
        flow = str(src) + ", " + str(dst) + ", " + str(srcport) + ", " + str(dstport) + ", " + str(proto) + ", " + str(ipv)
        if not flow in keys:
            delta_time = 0
            keys.append(flow)
        else:
            delta_time = time - flows[flow]
        flows.update({flow: time})
        print(delta_time)
        delta_time = str(delta_time).split(":")
        print(delta_time)
        print(len(delta_time))
        sum = 0
        for i in range(len(delta_time)):
            delta_time[i] = float(delta_time[i])
            if i == 0:
                delta_time[i] *= 3600.0
            elif i == 1:
                delta_time[i] *= 60.0
            sum+=delta_time[i]
        delta_time = '{:f}'.format(sum)

        print(delta_time)
        #if packet.transport_layer == 'TCP' and hasattr(packet.tcp, 'time_delta'):
        #    deltatime = packet.tcp.time_delta
        #elif packet.transport_layer == 'UDP' and hasattr(packet.udp, 'time_delta'):
        #    deltatime = packet.udp.time_delta
        #else:
        #    deltatime = 0
        human = 9 # dummy value, will be replaced

        rows.append([ipv, delta_time, src, dst, srcport, dstport, length, proto, human])
           #(ipv) + str(time) + str(src) + str(dst) + str(srcport) + str(dstport) + str(length) + str(proto)
    print(len(keys))
    writer.writerows(rows)



