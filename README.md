# ECMTECK_APP

Full-stack ECM Tek application with:

- **Frontend:** React (Vite)
- **Backend:** FastAPI (Python)
- **Monitoring:** Prometheus & Grafana
- **Database:** External Postgres and MongoDB recommended for production

---

## 🏗 Project Structure

ECMTECK_APP/
│── docker-compose.yml
│── frontend/
│ ├── Dockerfile
│ ├── package.json
│ └── src/...
│── backend/
│ ├── Dockerfile
│ ├── requirements.txt
│ └── main.py
│── prometheus/
│ └── prometheus.yml
│── grafana/
│ └── provisioning/
│ ├── dashboards/
│ └── datasources/
│── README.md


## Initialize frontend with Vite

npm create vite@latest .
npm install

## Build and run Docker containers
docker-compose up --build

## Access the services 

* Frontend: http://localhost:5173

* Backend: http://localhost:8000

* Prometheus: http://localhost:9090

* Grafana: http://localhost:3001

# Notes

Databases (Postgres, Mongo) should ideally run externally (AWS RDS, DocumentDB, or local Docker) for persistence.

Grafana dashboards and Prometheus config are under grafana/provisioning and prometheus/.

Ports can be changed in docker-compose.yml if conflicts exist.