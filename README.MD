# Python Prometheus & Grafana Example

## Instructions

- Install packages: `python3 -m pip install -r requirements.txt`
- Start flask app: `python3 -m flask run --host=0.0.0.0`
- Start services: `docker-compose up -d`
- Stop services: `docker-compose down`
- Visit <http://localhost:3000> to view Grafana dashboard (Login with user=admin, password=admin)

## Tasks

API endpoints: /create, /fetch, /update

- Dashboard Config
- Save dashboard and prometheus past data
- AWS deploy - config
- Status code of each API call
- Average Time duration for each API call
