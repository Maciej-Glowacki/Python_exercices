from flask import Flask

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return 'Hello World! ' + name + ' <3'

@app.route("/age/<int:num>")
def age(num):
    return f"You are {num} y.o."

app.run(debug=True)