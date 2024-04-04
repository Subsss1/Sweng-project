'''
Run model on given arguments
Usage: python3 inference.py <source_port> <destination_port> <protocol> <length> <length_deviation> <delta_time> <flow_average_length> <flow_length_deviation> <flow_delta_time>
'''

import sys
import pandas as pd
import joblib
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS

# Get arguments
arguments = sys.argv[1:]

if len(arguments) != 9:
  print('-1')
  sys.exit(1)

# Load model
model = joblib.load('./model.pkl')

# Prepare input data
input_data = pd.DataFrame({
  'source_port':            int(arguments[0]),
  'destination_port':       int(arguments[1]),
  'protocol':               int(arguments[2]),
  'length':                 int(arguments[3]),
  'length_deviation':       float(arguments[4]),
  'delta_time':             float(arguments[5]),
  'flow_average_length':    float(arguments[6]),
  'flow_length_deviation':  float(arguments[7]),
  'flow_delta_time':        float(arguments[8]),
}, index=[0])

# Get prediction
# Returns list of probabilities [macnine_probability, human_probability][]
result = model.predict_proba(input_data)
#if(result[0]>0.5):testResult = 1
#else: testResult = 0



# InfluxDB settings
bucket = "TestB"  # Bucket name
org = "SWENG-11"  # Organization name
token = "57dykGMfLWOWjLKWJmWBz5Bgr4hVE7fppm3SyFe5BWZY83Xt99m-PcFPClrMl048uYHc3Q6dJ6eUYdjvYdQOpA=="  # Token
url = "https://eu-central-1-1.aws.cloud2.influxdata.com"  # InfluxDB Cloud URL

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)


if(result[0,0]>0.5):testResult = 1
else: testResult = 0


def insert_data(measurement, fields={}, tags={}):
    p = Point(measurement).tag("dissector", "wireshark")
    for tag_key, tag_value in tags.items():
        p.tag(tag_key, tag_value)
    for field_key, field_value in fields.items():
        p.field(field_key, field_value)
    write_api.write(bucket=bucket, org=org, record=p)

insert_data("test_measurement2",
            {"source_port": arguments[0],
             "destination_port": arguments[1],
             "length":arguments[3],
             "length_deviation":arguments[4],
             "delta_time":arguments[5],
             "flow_average_length":arguments[6],
             "flow_length_deviation":arguments[7],
             "flow_delta_time":arguments[8]
             }, {"protocol":arguments[2],"Is machine":testResult})  # Example data point



# Return result
print(result[0][0])
