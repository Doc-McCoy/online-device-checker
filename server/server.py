import os
import requests
from server.bot import Bot
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)
mongo_uri = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/teste')
mongo_uri += '?retryWrites=false'
app.config['MONGO_URI'] = mongo_uri
mongo = PyMongo(app)
telegram_bot = Bot()

def is_online(url):
    """
    Faz um GET no client para verificar se ele está online
    """
    complete_url = url + '/check'
    try:
        response = requests.get(complete_url)
        if response.status_code == 200:
            return True
        return False
    except:
        return False

@app.route('/clients', methods=['GET', 'POST', 'DELETE'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        mongo.db.users.insert_one(data)
        return jsonify({'response': 'ok'})
    if request.method == 'GET':
        query = mongo.db.users.find({}, {'_id': False})
        data = {'clients': list(query)}
        return jsonify(data)
    if request.method == 'DELETE':
        data = request.get_json()
        mongo.db.users.delete_one(data)
        return jsonify({'response': 'Client deleted'})

@app.route('/check', methods=['GET'])
def check():
    query = mongo.db.users.find({}, {'_id': False})
    for client in query:
        if not is_online(client['url']):
            telegram_bot.notify(client['name'])
    return jsonify({'response': 'ping clients...'})


if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
