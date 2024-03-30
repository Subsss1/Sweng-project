import sys
import ipaddress
import joblib

# Get arguments
arguments = sys.argv[1:] # [ src_port, dst_port, proto, delta_time, len, avg_len ]

# Format input data
src_port = int(arguments[0])
dst_port = int(arguments[1])
proto = int(arguments[2])
delta_time = float(arguments[3])
length = int(arguments[4])
avg_len = float(arguments[5])

input_data = [[ src_port, dst_port, proto, delta_time, length, avg_len ]]

# Run model
model = joblib.load('model.pkl')
result = model.predict(input_data)

# Return result
print(result[0])
