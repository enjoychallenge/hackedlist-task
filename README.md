# hackedlist-task


## Install

### Prerequisites
- Python 3.12+
- Node v22

```bash
# server
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# client
npm --prefix src/js ci
```

## Server

### Tests
Run tests with `make test`

### Start
Start server with `make start-server`

Documentation runs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). You can also test endpoints there.

### Lint
Check your code format with `make lint` or format it with `make lint-fix`.
[Black](https://black.readthedocs.io/en/stable/) is used as code formatter.

## Client

### Start
```bash
make start-client
```

Open [http://localhost:3000](http://localhost:3000) with your browser.
