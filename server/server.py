from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        register_client()
    if request.method == 'GET':
        get_clients()

def register_client():
    pass

def get_clients():
    pass


if __name__ == "__main__":
    app.run()
