# Script that runs model
import sys
import random

# Get arguments
arguments = sys.argv[1:]

# Some magical stuff with model (run inference using arguments)
result = random.uniform(0, 1)

# Return result
print(result)
