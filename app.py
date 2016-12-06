from flask import Flask

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")

def hello_world():
	return "HELLO MOFO!"

@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "correctr"

@app.route("/float/<float:value>")
def float_type(value):
	print value + 1
	return "correctt"

@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correcth"

@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello, {}".format(name),200
	else:
		return "File not found", 404

if __name__ == "__main__":
	app.run()

