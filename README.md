# Smart Warehouse System

A smart warehouse inventory system with a simulated automation layer. It provides an API to register products and track stock, and simulated robots ("workers") that fetch items from shelves. I am building it step by step to practice DevOps: containers, CI/CD, Kubernetes, and monitoring.

## Status

Work in progress. Started October 2026.

## Implemented

- Linux development environment (WSL2 + Ubuntu)
- Git and GitHub workflow (SSH authentication, commit history)
- Bash script to check the development environment (`scripts/check_env.sh`)
- REST API built with Python and FastAPI (in-memory storage)
- Automated API tests with pytest

## Planned

PostgreSQL, Docker, CI/CD, Redis task queue, simulated warehouse workers, Kubernetes, Prometheus, Grafana, Azure

## API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| POST | `/products` | Add a product |
| GET | `/products` | List all products |
| GET | `/products/{product_id}` | Get one product by position |
| DELETE | `/products/{product_id}` | Delete one product |
| DELETE | `/products` | Delete all products |

Note: data is stored in memory for now, so it is lost when the server stops. PostgreSQL is the next step.

## Run Locally

```bash
git clone git@github.com:KhaledAnjo/smart-warehouse.git
cd smart-warehouse/api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/docs for the interactive API documentation.

## Run Tests

```bash
cd api
pytest
```

## Project Structure

- `api/`: the inventory API and its tests
- `scripts/`: automation scripts
- `worker/`: simulated warehouse robots (planned)
- `docs/`: documentation (planned)
