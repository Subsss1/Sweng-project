# Script that runs model
import sys
import joblib
import time
import random
# Get arguments


arguments = sys.argv[1:]

data = [1]
arguments[1] = 6.0
if arguments[8] == 'TCP':
    arguments[8] = 6.0
elif arguments[8] == 'UDP':
    arguments[8] = 17.0
else:
    arguments[8] = 252.0

stats = arguments[1:]

data.append([float(num) for num in stats])
data.remove(1)
loaded_model = joblib.load('model.pkl')

result = loaded_model.predict(data)
#result = random.uniform(0, 1)
# Return result
print(result)


