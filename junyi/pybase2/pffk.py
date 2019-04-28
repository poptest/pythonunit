from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/hello/<name>')
def hello_world_by_name(name=None):
    return "Hello %s" % name

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="9527", debug=True)
