from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_phantom():
    return "<p>Hello, phantom!</p>"