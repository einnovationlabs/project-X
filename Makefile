init:
	pip3 install -r main/requirements.txt
	touch main/.env
.PHONY: init

run:
	python3 main/manage.py runserver
.PHONY: run

migrate:
	python3 main/manage.py makemigrations
	python3 main/manage.py migrate
.PHONY: migrate

clean:
	find . | grep -E "(/__pycache__)" | xargs rm -rf
	find . -name "*.pyc" -exec rm -f {} \;
.PHONY: clean

format:
	./main/scripts/format.sh
.PHONY: format