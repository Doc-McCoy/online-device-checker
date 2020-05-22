from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/check')
def check():
    data = {'status': 'online'}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
