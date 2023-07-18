init:
	pip3 install -r backend/requirements.txt
	touch backend/.env
.PHONY: init

start:
	python3 backend/manage.py runserver
.PHONY: start

migrate:
	python3 backend/manage.py makemigrations
	python3 backend/manage.py migrate
.PHONY: migrate