# Script that runs model
import sys
import time
import random

# Get arguments
arguments = sys.argv[1:]

# Some magical stuff with model (run inference using arguments)
time.sleep(1) # Simulate heavy work
result = random.uniform(0, 1)

# Return result
print(result)

