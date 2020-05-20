from flask import Flask, jsonify, request
from server.mongo import Mongo


app = Flask(__name__)
db = Mongo()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        db.insert(data)
        return jsonify({'response': 'ok'})
    if request.method == 'GET':
        clients = db.get()
        return jsonify(clients)

@app.route('/drop', methods=['DELETE'])
def drop():
    db.drop()
    return jsonify({'response': 'database dropped'})


if __name__ == "__main__":
    app.run()
