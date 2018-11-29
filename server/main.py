from flask import Flask, jsonify, Response
from subprocess import call
import requests

app = Flask(__name__)
#<script src="jquery-3.2.1.min.js"></script>
@app.route('/')
def homepage():
    return Response(open("static/index.html").read(),  mimetype="text/html")

@app.route('/reloadenv/')
def reloadenv():
	try:
		r = call(["./restartenv.sh"])
		print r
		status = "success"
	except Exception, err:
		print err
		status = "error"
	print status
	return jsonify({"status":status})


@app.route('/ndpexhaustion/')
def ndpexhaustion():
	try:
		r = requests.get('http://127.0.0.1:4381/ndpexhaustion/2a02:16:33::/100',timeout=1)
		status = "success"
		resume = str(r)
	except requests.exceptions.ReadTimeout:
		status = "success"
	except Exception as err:
		status = "error"
		resume = str(err)
	return jsonify({"status":status})

@app.route('/multiplesyn/')
def multiplesyn():
	try:
		r = requests.get('http://127.0.0.1:4381/multiplesyn/2a02:16:33::/2a02:16:33::82/100',timeout=1)
		status = "success"
		resume = str(r)
	except requests.exceptions.ReadTimeout:
		status = "success"
	except Exception as err:
		status = "error"
		resume = str(err)
	return jsonify({"status":status})

@app.route('/multipleh/')
def multipleh():
	try:
		r = requests.get('http://127.0.0.1:4381/multipleh/2a02:16:33::/2a02:16:33::82/100',timeout=1)
		status = "success"
		resume = str(r)
	except requests.exceptions.ReadTimeout:
		status = "success"
	except Exception as err:
		status = "error"
		resume = str(err)
	return jsonify({"status":status})

@app.route('/synflood/')
def synflood():
	try:
		r = requests.get('http://127.0.0.1:4381/synflood/2a02:16:33::81/2a02:16:33::82/500',timeout=1)
		status = "success"
		resume = str(r)
	except requests.exceptions.ReadTimeout:
		status = "success"
	except Exception as err:
		status = "error"
		resume = str(err)
	return jsonify({"status":status})

@app.route('/discovery/')
def discovery():
	try:
		r = requests.get('http://127.0.0.1:4381/discover/2a02:16:33::',timeout=1)
		status = "success"
		resume = str(r)
	except requests.exceptions.ReadTimeout:
		status = "success"
	except Exception as err:
		status = "error"
		resume = str(err)
	print status
	return jsonify({"status":status})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
