from flask import Flask, jsonify

# just sample code it can be improved!

app = Flask(__name__)

@app.route('/notifications', methods=['GET'])
def get_notifications():
    # Return dummy data for testing
    notifications = [
        {"type": "Attack", "description": "DDoS detected", "timestamp": "2025-01-23T12:00:00Z"},
        {"type": "Malfunction", "description": "Bandwidth drop", "timestamp": "2025-01-23T12:05:00Z"},
    ]
    return jsonify(notifications)

if __name__ == '__main__':
    app.run(debug=True)
