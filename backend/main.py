from fastapi import FastAPI
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from prometheus_client import start_http_server

app = FastAPI()

# ---- OpenTelemetry Setup ----
resource = Resource.create({"service.name": "backend"})

reader = PrometheusMetricReader()
provider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(provider)

# Expose metrics endpoint on :9464
start_http_server(port=9464)

meter = metrics.get_meter("backend_meter")

# Example metric
request_counter = meter.create_counter(
    "backend_requests_total",
    description="Number of requests to backend endpoints"
)

@app.get("/")
async def root():
    request_counter.add(1, {"endpoint": "/"})
    return {"message": "Hello from Backend with OpenTelemetry!"}

@app.get("/health")
async def health():
    request_counter.add(1, {"endpoint": "/health"})
    return {"status": "ok"}
