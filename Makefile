PIP = pip3
PYTHON = python3
INSTANCE_CONNECTION_NAME = project-hybrid-187000:australia-southeast1:project-hybrid-postgres

run: check-venv
	$(PYTHON) manage.py runserver

migrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate
	
init-js:
	sudo apt-get install nodejs
	sudo apt-get install npm
	npm install
	
test:
	$(PYTHON) manage.py test

check-venv:
ifndef VIRTUAL_ENV
	echo "\033[1;91m\n❗  You don't appear to be in a virtual environment, did you remember to";\
	echo "\033[0m    source bin/activate"; echo "\033[1;91m?\033[0m"; exit 1
endif
