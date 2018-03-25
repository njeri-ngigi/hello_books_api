#run.py

from app import app


#app = create_app(config_name)

if __name__ == '__main__':
	app.run(debug=True)


#to run, run the commands: 
#$ export FLASK_APP=run.py
#$ flask run