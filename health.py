from flask import Flask, jsonify, json

app = Flask(__name__)

@app.route('/latest', methods=['GET'])
def get_latest():
	# Need a middleground between the database and app
	# Sharynne's app calls this endpoint on a set interval
	# this method calls Lucy's db methods
	# returns JSON response for Sharynne's map
	# could return big JSON with results from all streams/categories and app can filter which to pick from?
	pass 

if __name__ == '__main__':
	app.debug = True
	app.run(port = 8000)