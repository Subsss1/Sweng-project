'''
Convert a traffic capture and its labels to a dataset for model training.
Usage: python capture2dataset.py <capture_path> <labels_path> <output_path>
'''

import sys
import pyshark
import ipaddress
import csv


# Convert packets from capture to a list of dictionaries
def read_packets(capture: pyshark.FileCapture):
  packets = []

  for packet in capture:
    network_layer = 'ip' if hasattr(packet, 'ip') else 'ipv6' if hasattr(packet, 'ipv6') else 'other'
    transport_layer = packet.transport_layer

    if network_layer != 'ip':
      continue

    packets.append({
      'number':           int(packet.number),
      'timestamp':        float(packet.sniff_time.timestamp()),
      'source':           int(ipaddress.IPv4Address(packet[network_layer].src)),
      'destination':      int(ipaddress.IPv4Address(packet[network_layer].dst)),
      'source_port':      int(packet[transport_layer].srcport),
      'destination_port': int(packet[transport_layer].dstport),
      'protocol':         int(6 if packet.transport_layer == 'TCP' else 17 if packet.transport_layer == 'UDP' else -1),
      'length':           int(packet.length),
    })

  return packets


# Add fields from labels to packets based on packet number
def add_labels(packets: list, labels: list):
  labeled_packets = []
  packet_map = {packet['number']: packet for packet in packets}

  for label in labels:
    number = label['number']

    if number in packet_map:
      packet = packet_map[number]
      labeled_packets.append({**packet, **label})

  return labeled_packets


# Preprocess packets for model training
def preprocess_packets(packets: list):
  preprocessed_packets = []
  global_flow = {}
  flows = {}

  for packet in packets:
    preprocessed_packet = {
      'number':                 str(packet['number']),
      'source_port':            str(packet['source_port']),
      'destination_port':       str(packet['destination_port']),
      'protocol':               str(packet['protocol']),
      'length':                 str(packet['length']),
      'length_deviation':       str(0),
      'delta_time':             str(0),
      'flow_average_length':    str(packet['length']),
      'flow_length_deviation':  str(0),
      'flow_delta_time':        str(0),
    }

    if bool(global_flow):
      preprocessed_packet['delta_time'] = f'{abs(packet['timestamp'] - global_flow['last_timestamp']):.8f}'
      preprocessed_packet['length_deviation'] = f'{abs(packet['length'] - global_flow['average_length']):.8f}'
      global_flow['duration'] += 1
      global_flow['last_timestamp'] = packet['timestamp']
      global_flow['average_length'] = (global_flow['average_length'] * (global_flow['duration'] - 1) + packet['length']) / global_flow['duration']
    else:
      global_flow = {
        'duration': 1,
        'last_timestamp': packet['timestamp'],
        'average_length': packet['length'],
      }

    flow = (packet['source'], packet['destination'], packet['source_port'], packet['destination_port'], packet['protocol'])

    if flow in flows:
      preprocessed_packet['flow_delta_time'] = f'{abs(packet['timestamp'] - flows[flow]['last_timestamp']):.8f}'
      preprocessed_packet['flow_length_deviation'] = f'{abs(packet['length'] - flows[flow]['average_length']):.8f}'
      flows[flow]['duration'] += 1
      flows[flow]['last_timestamp'] = packet['timestamp']
      flows[flow]['average_length'] = (flows[flow]['average_length'] * (flows[flow]['duration'] - 1) + packet['length']) / flows[flow]['duration']
      preprocessed_packet['flow_average_length'] = f'{flows[flow]['average_length']:.8f}'
    else:
      flows[flow] = {
        'duration': 1,
        'last_timestamp': packet['timestamp'],
        'average_length': packet['length'],
      }

    preprocessed_packets.append(preprocessed_packet)

  return preprocessed_packets


if __name__ == "__main__":
  if len(sys.argv) != 4:
    print('Usage: python capture2dataset.py <capture_path> <labels_path> <output_path>')
    sys.exit(1)

  capture_path = sys.argv[1]
  labels_path = sys.argv[2]
  output_path = sys.argv[3]

  # Read packets
  with open(capture_path, 'r') as _:
    capture = pyshark.FileCapture(capture_path, display_filter='tcp or udp')
    packets = read_packets(capture)
  
  # Preprocess packets
  packets = preprocess_packets(packets)

  # Add labels
  with open(labels_path, 'r') as labels_file:
    reader = csv.DictReader(labels_file)
    labels = list(reader)
    packets = add_labels(packets, labels)

  # Write to CSV
  with open(output_path, 'w') as output_file:
    if len(packets) > 0:
      writer = csv.DictWriter(output_file, fieldnames=packets[0].keys())
      writer.writeheader()
      writer.writerows(packets)
