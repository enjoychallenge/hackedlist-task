test:
	pytest -xvv src/python/

start:
	fastapi dev src/python/main.py

lint:
	black --check src/python

lint-fix:
	black src/python
