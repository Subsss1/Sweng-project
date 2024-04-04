'''
Run the inference server for the model
Usage: python server.py
Port: 13131
Requires: model.pkl
Request: GET /infer
                   ?number=<int>
                   &flow=<str>
                   &source_port=<int>
                   &destination_port=<int>
                   &protocol=<int>
                   &length=<int>
                   &length_deviation=<float>
                   &delta_time=<float>
                   &flow_average_length=<float>
                   &flow_length_deviation=<float>
                   &flow_delta_time=<float>
'''

import pandas as pd
import joblib
from flask import Flask, request

# Load model
model = joblib.load('./model.pkl')

# Run model on given parameters
def run_model(parameters: dict):
  input_data = pd.DataFrame({
    'source_port':            parameters['source_port'],
    'destination_port':       parameters['destination_port'],
    'protocol':               parameters['protocol'],
    'length':                 parameters['length'],
    'length_deviation':       parameters['length_deviation'],
    'delta_time':             parameters['delta_time'],
    'flow_average_length':    parameters['flow_average_length'],
    'flow_length_deviation':  parameters['flow_length_deviation'],
    'flow_delta_time':        parameters['flow_delta_time'],
  }, index=[0])

  result = model.predict_proba(input_data)

  return f'{result[0][0]:.8f}'

# Flask server
app = Flask(__name__)

# Infer endpoint
@app.route('/infer', methods=['GET'])
def infer():
  args = request.args

  parameters = {
    'number':                 args.get('number',                None, int),
    'flow':                   args.get('flow',                  None, str),
    'source_port':            args.get('source_port',           None, int),
    'destination_port':       args.get('destination_port',      None, int),
    'protocol':               args.get('protocol',              None, int),
    'length':                 args.get('length',                None, int),
    'length_deviation':       args.get('length_deviation',      None, float),
    'delta_time':             args.get('delta_time',            None, float),
    'flow_average_length':    args.get('flow_average_length',   None, float),
    'flow_length_deviation':  args.get('flow_length_deviation', None, float),
    'flow_delta_time':        args.get('flow_delta_time',       None, float),
  }

  if None in parameters.values():
    return "Invalid parameters", 400

  return run_model(parameters)

# Run server
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=13131)
