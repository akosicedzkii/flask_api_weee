import run

from flask import jsonify

app = run.app
@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})