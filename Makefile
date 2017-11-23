PIP=pip3
PYTHON=python3

run: check-venv
	$(PYTHON) manage.py runserver
	
migrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

check-venv:
ifndef VIRTUAL_ENV
	echo "\033[1;91m\n❗  You don't appear to be in a virtual environment, did you remember to";\
	echo "\033[0m    source bin/activate"; echo "\033[1;91m?\033[0m"; exit 1
endif
	