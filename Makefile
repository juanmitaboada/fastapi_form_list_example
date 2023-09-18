default:
	make env
	make reqs
	make web
	make server

env:
	virtualenv -p python env
	make reqs

reqs:
	(. ./env/bin/activate && pip install -r requirements.txt)

web:
	open multiform.html &

server:
	(. ./env/bin/activate && uvicorn multiform:app --host 127.0.0.1 --port 8000 --reload)
