to install flask (once per computer), open PowerShell & type:
	pip install flask # install flask
	pip install Flask-WTF # install flask wtform

to generate flask environment (once per project), go into project folder, open PowerShell & type:
	python -m venv flask_env # generate flask_env folder & files into project

to start a session on your project (once per session), go into project folder, open PowerShell & type:
	Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process # give permission to execute script (only for this session in this project)
	.\flask_env\Scripts\Activate # enable flask environment
	python -m flask run
	OR
	python run.py # run project (by default OR run a specific file)
(I made a script.bat to launch the 3 commands in one go)

if you encounter a “Could not locate a Flask application” error
	set FLASK_APP=myapp
	OR
	$env:FLASK_APP = "myapp"

to initialize database (once)
	python # activate python commands
	import os # import python os module
	os.urandom(24).hex() # generate encryption key
	pip install Flask-SQLAlchemy # install package
	pip install Flask-Migrate #install migrate package
	flask db init # initialize database
	[ update database datas ]

to update or initialize database datas (once per structure update)
	flask db migrate -m "commit text" # need to be setup in script.py before
	flask db upgrade
