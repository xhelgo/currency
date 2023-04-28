
manage_py := python app/manage.py

run:
	$(manage_py) runserver

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell:
	$(manage_py) shell_plus --print-sql

createsuperuser:
	$(manage_py) createsuperuser

setup:
	pip install -r requirements.txt

worker:
	cd app && celery -A settings worker -l info --autoscale=0,10

beat:
	cd app && celery -A settings beat -l info

pytest:
	pytest ./app/tests --cov=app  --cov-report html
