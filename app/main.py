import logging
from fastapi import FastAPI, Request
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Store Sales MLOps API")

# 1. Initialize and Instrument the App
# This captures standard HTTP metrics out-of-the-box
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

@app.post("/predict")
async def predict(features: dict):
    # The instrumentator automatically tracks latency and status codes for this route
    prediction = 42.0  # Placeholder for your Prophet model
    logging.info(f"Prediction_Logged | Value: {prediction}")
    return {"prediction": prediction}

@app.get("/health")
async def health():
    return {"status": "healthy"}
