from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'v3 - Hello from the simple-rest-app!!!!!'

@app.route('/rota2')
def rota2():
    return 'v3 - Hello from the simple-rest-app rota2!'


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8181, debug=True)