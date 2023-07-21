init:
	pip3 install -r main/requirements.txt
	touch main/.env
.PHONY: init

start:
	python3 main/manage.py runserver
.PHONY: start

migrate:
	python3 main/manage.py makemigrations
	python3 main/manage.py migrate
.PHONY: migrate

clean:
	find . | grep -E "(/__pycache__)" | xargs rm -rf
	find . -name "*.pyc" -exec rm -f {} \;
.PHONY: clean