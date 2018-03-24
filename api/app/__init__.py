#app/__init__.py

from flask import Flask

#initialize app
app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def hello():
	print("Helloooo")


app.config.from_object('config')

