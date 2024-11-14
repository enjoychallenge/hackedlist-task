test:
	pytest -xvv src/python/

start-server:
	fastapi dev src/python/main.py

start-client:
	npm --prefix src/js run dev

lint:
	black --check src/python

lint-fix:
	black src/python
