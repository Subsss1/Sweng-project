#!/usr/bin/env python

"""
example :
    python 3_add_label.py twitter update_twitter-sg_20180310_135947.csv
Based on:
@author: liutao from https://www.linkedin.com/pulse/build-machine-learning-model-network-flow-tao-liu
"""

import sys
import csv

label = sys.argv[1]
file_name = sys.argv[2]

file = open(file_name)
content = csv.reader(file)
all = []
for idx, row in enumerate (content):
    if idx == 0:
        row.append('Human')
    else:
        if row[6] == 'Application Data':
            row.append(1)
        else:
            row.append(0)
    all.append(row)

new_file = open(label+'_'+ file_name, 'w')
writer = csv.writer(new_file, lineterminator='\n')
writer.writerows(all)