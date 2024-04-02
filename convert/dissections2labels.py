'''
Convert dissections in CSV format to labels.
Usage: python dissections2labels.py <dissections_path> <output_path>

Based on:
@author: liutao from https://www.linkedin.com/pulse/build-machine-learning-model-network-flow-tao-liu
'''

import sys
import csv


# Get labels from dissections
def get_labels(dissections: list[dict]):
  labels = []

  for dissection in dissections:
    label = { 
      'number': dissection['No.'], 
      'human': int(dissection['Info'] == 'Application Data')
    }

    labels.append(label)

  return labels


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print('Usage: python dissections2labels.py <dissections_path> <output_path>')
    sys.exit(1)

  dissections_path = sys.argv[1]
  output_path = sys.argv[2]

  labels = []

  # Get labels
  with open(dissections_path, 'r') as dissections_file:
    reader = csv.DictReader(dissections_file)
    dissections = list(reader)
    labels = get_labels(dissections)

  # Write to CSV
  with open(output_path, 'w') as output_file:
    if len(labels) > 0:
      writer = csv.DictWriter(output_file, fieldnames=labels[0].keys())
      writer.writeheader()
      writer.writerows(labels)
