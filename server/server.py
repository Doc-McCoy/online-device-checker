import os
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
# from server.mongo import Mongo


app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017')
mongo = PyMongo(app)
# db = Mongo()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        # db.insert(data)
        mongo.db.users.insert_one(data)
        return jsonify({'response': 'ok'})
    if request.method == 'GET':
        # clients = db.get()
        clients = mongo.db.users.find({}, {'_id': False})
        return jsonify(clients)

@app.route('/drop', methods=['DELETE'])
def drop():
    # db.drop()
    return jsonify({'response': 'database dropped'})


if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
