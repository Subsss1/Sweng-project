local file = io.open("example_model.pkl", "rb")
local modelData = file:read("*a")
file:close()

local pickle = require "python-pickle"
local model = pickle.loads(modelData)
local prediction = model:predict(data)
