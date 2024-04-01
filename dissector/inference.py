'''
Run model on given arguments.
Usage: python3 inference.py <source_port> <destination_port> <protocol> <length> <length_deviation> <delta_time> <flow_average_length> <flow_length_deviation> <flow_delta_time>
'''

import sys
import pandas as pd
import joblib

# Get arguments
arguments = sys.argv[1:]

if len(arguments) != 9:
  print('-1')
  sys.exit(1)

# Load model
model = joblib.load('./model.pkl')

# Prepare input data
input_data = pd.DataFrame([{
  'source_port':            int(arguments[0]),
  'destination_port':       int(arguments[1]),
  'protocol':               int(arguments[2]),
  'length':                 int(arguments[3]),
  'length_deviation':       float(arguments[4]),
  'delta_time':             float(arguments[5]),
  'flow_average_length':    float(arguments[6]),
  'flow_length_deviation':  float(arguments[7]),
  'flow_delta_time':        float(arguments[8]),
}])

# Get prediction
# Returns list of probabilities [macnine_probability, human_probability][]
result = model.predict_proba(input_data)

# Return result
print(result[0][0])
