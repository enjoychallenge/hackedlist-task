test:
	pytest -xvv src/python/

start-server:
	fastapi dev src/python/main.py

start-client:
	npm --prefix src/js run dev

lint-server:
	black --check src/python

lint-fix-server:
	black src/python

lint-client:
	npm --prefix src/js run format
	npm --prefix src/js run ts
	npm --prefix src/js run lint

lint-fix-client:
	npm --prefix src/js run format-fix
	npm --prefix src/js run lint --fix
