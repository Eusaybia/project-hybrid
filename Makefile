PIP = pip3
PYTHON = python3
INSTANCE_CONNECTION_NAME = project-hybrid-187000:australia-southeast1:project-hybrid-postgres

# Only needs to be run once
init: start-sql-proxy

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

start-sql-proxy:
	./cloud_sql_proxy -instances="$(INSTANCE_CONNECTION_NAME)"=tcp:5432 &
