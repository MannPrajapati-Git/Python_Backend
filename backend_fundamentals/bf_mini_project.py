# project : Python Dummy API
# This mini project is a simple Flask API that responds to a GET request at /api/data with a JSON message confirming the backend is working.

# pip install flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getdata', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from backend!", "status": "success"})

if __name__ == '__main__':
    app.run(debug=True)

