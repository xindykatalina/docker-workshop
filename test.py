#packages import 
from flask import Flask, jsonify, make_response, send_from_directory

from functools import wraps
import requests

import os
import sys
import threading


from flask_restful import Resource, request

import json
import time

app = Flask(__name__)

def worker(i):
	"""funcion que realiza el trabajo en el thread"""
	print('contador.............', i)
	r = requests.get("http://35.237.57.195:5000")
	print('Mensaje ', r.text)

@app.route('/testapi', methods=['POST'])
def testapi():

	threads = list()
	#local directory
	for i in range(900000):

		#time.sleep(6)

		t = threading.Thread(target=worker,args=(i,))
		threads.append(t)
		t.start()

	return jsonify({'message' : 'Todo hecho!!'}) 


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000, debug=True, threaded=True)