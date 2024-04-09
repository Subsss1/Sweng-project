import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock machine learning model
def is_machine_generated(traffic_data):
    
    # return traffic_data.startswith("Machine")

    is_machine = random.randint(0, 1)

    return jsonify({'is_machine_generated': is_machine})

@app.route('/is_machine_generated', methods=['POST'])
def check_machine_generated():
    data = request.json
    traffic_data = data.get('traffic_data')
    if traffic_data is None:
        return jsonify({'error': 'Traffic data not provided'}), 400

    # Call the machine learning model function
    is_machine = is_machine_generated(traffic_data)

    return jsonify({'is_machine_generated': is_machine})

if __name__ == '__main__':
    app.run(debug=True)
