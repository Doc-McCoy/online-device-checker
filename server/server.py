import os
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)
mongo_uri = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/teste')
mongo_uri += '?retryWrites=false'
app.config['MONGO_URI'] = mongo_uri
mongo = PyMongo(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        mongo.db.users.insert_one(data)
        return jsonify({'response': 'ok'})
    if request.method == 'GET':
        query = mongo.db.users.find({}, {'_id': False})
        data = {'clients': list(query)}
        return jsonify(data)

@app.route('/drop', methods=['DELETE'])
def drop():
    return jsonify({'response': 'database dropped'})


if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
