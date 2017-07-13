# leaflet_demo
	work on leaflet without django gis

# Set Up

## Install Pip
	sudo apt-get install python-pip

## SetUp VirtualEnv

	pip install virtualenv
	mkdir ~/.virtualenvs
	pip install virtualenvwrapper
	export Projects=~/.virtualenvs
	
	Add this line to the end of ~/.bashrc so that the virtualenvwrapper commands are loaded.
	. /usr/local/bin/virtualenvwrapper.sh

## Activate VirtualEnv
	mkvirtualenv Locate
	workon Locate

## Clone leaflet repository
	git clone git@github.com:usudaysingh/leaflet_demo.git

## Install Requirements
	pip install -r requirements.txt

## Set Up MySQL
	sudo apt-get install libmysqlclient-dev
	sudo apt-get install mysql-server
	mysql -u root -p --execute "create database locate; grant all on locate.* to uday@localhost identified by 'udaysingh';"

## Load Fixtures
	python manage.py loaddata locate/fixtures/initial_data.json

## Run Server
	python manage.py runserver
	open http://127.0.0.1:8001/index in your browser

### Play with map