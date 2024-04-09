'''
Run inference server for the model
Usage: python model_server.py <model_path> <port>
Requests: 
  GET /infer
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

import sys
import pandas as pd
import joblib
from flask import Flask, request

# Run model
def run_model(model, parameters: dict):
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

  return result[0][0]

# Run server
def run_server(model_path: str, port: int):
  app = Flask(__name__)
  model = joblib.load(model_path)

  @app.route('/infer', methods=['GET'])
  def infer():
    parameters = {
      'number':                 request.args.get('number',                None, int),
      'flow':                   request.args.get('flow',                  None, str),
      'source_port':            request.args.get('source_port',           None, int),
      'destination_port':       request.args.get('destination_port',      None, int),
      'protocol':               request.args.get('protocol',              None, int),
      'length':                 request.args.get('length',                None, int),
      'length_deviation':       request.args.get('length_deviation',      None, float),
      'delta_time':             request.args.get('delta_time',            None, float),
      'flow_average_length':    request.args.get('flow_average_length',   None, float),
      'flow_length_deviation':  request.args.get('flow_length_deviation', None, float),
      'flow_delta_time':        request.args.get('flow_delta_time',       None, float),
    }

    if None in parameters.values():
      return "Invalid parameters", 400

    result = run_model(model, parameters)
    return f'{result:.8f}', 200

  app.run(host='0.0.0.0', port=port)
  return app

if __name__ == '__main__':
  if len(sys.argv) != 3:
    print('Usage: python model_server.py <model_path> <port>')
    sys.exit(1)

  model_path = sys.argv[1]
  port = sys.argv[2]

  run_server(model_path, port)
