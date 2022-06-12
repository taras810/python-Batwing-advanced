from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/name")
def my_name():
    return "<h1>Taras Senko</h1>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
