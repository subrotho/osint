# Import libraries
import os
import flask 
from flask import request,redirect,url_for, render_template, session
from google.cloud import bigquery
from random import random
from flask import jsonify
from flask_session import Session
import math
import datetime
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from os.path import basename




# Initialize flask application
app_flask = flask.Flask(__name__, 
	static_url_path="", 
	static_folder="",
	template_folder='')

# Define API route
@app_flask.route("/")
def root():
	return render_template('uk_govt_open_data.html')

@app_flask.route("/submit",methods=['POST'])
def submit(methods=['POST']):
	base=request.form.get('base')
	url = requests.get(request.form.get('url')).text
	links=[]
	soup = BeautifulSoup(url)
	for link in (urljoin(base, a["href"]) for a in soup.select("a[href$=.xls]")):
		# r = requests.get(link, allow_redirects=True)
		# open('abc.xls', 'wb').write(r.content)
		links.append(link)
	for link in (urljoin(base, a["href"]) for a in soup.select("a[href$=.csv]")):
		# r = requests.get(link, allow_redirects=True)
		# open('abc.xls', 'wb').write(r.content)
		links.append(link)	
	for link in (urljoin(base, a["href"]) for a in soup.select("a[href$=.pdf]")):
		# r = requests.get(link, allow_redirects=True)
		# open('abc.xls', 'wb').write(r.content)
		links.append(link)	
	return jsonify(links)	

app_flask.run(port=8005, host='0.0.0.0')
