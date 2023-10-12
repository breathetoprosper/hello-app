"""
#BKP. This one works. Do others besides this one.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('hello.html', name=name)
"""
from flask import Flask, render_template, request, flash

app = Flask(__name__)#defines the class
app.secret_key = '12345lwzdmO5DqpK#rCbKSCi#5S^$&#~QP}ZzD&?teNf=lIRA@aoP-nSlC)Z|UL2e;'

@app.route('/')#defines the route
def index():
	flash("What's your name?")#displays a message
	return render_template('hello.html')#uses the template from the html file

@app.route("/greet", methods=["POST","GET"])
def greet():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")#displays a message
	request.form['name_input']
	return render_template('hello.html')