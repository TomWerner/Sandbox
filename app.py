from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/execute', methods=['POST'], )
def execute():
    if request.method != 'POST':
        return
    return request.get_json()


if __name__ == "__main__":
    app.run()