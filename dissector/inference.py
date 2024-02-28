import sys
import ipaddress
import joblib

# Get arguments
arguments = sys.argv[1:] # [ number, timestamp, ipv, src, dst, src_port, dst_port, proto, len ]

# Format input data
number = int(arguments[0])
timestamp = float(arguments[1])
ipv = int(arguments[2])
src = int(ipaddress.IPv4Address(arguments[3]))
dst = int(ipaddress.IPv4Address(arguments[4]))
src_port = int(arguments[5])
dst_port = int(arguments[6])
proto = int(arguments[7])
length = int(arguments[8])

input_data = [[number, ipv, timestamp, src, dst, src_port, dst_port, length, proto]]

# Run model
model = joblib.load('model.pkl')
result = model.predict(input_data)

# Return result
print(result[0])
