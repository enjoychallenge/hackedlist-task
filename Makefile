test:
	pytest -xvv src/python/

start:
	fastapi dev src/python/main.py
