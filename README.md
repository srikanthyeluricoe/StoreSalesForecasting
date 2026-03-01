![MLOps CI Pipeline](https://github.com/srikanthyeluricoe/StoreSalesForecasting/actions/workflows/main.yml/badge.svg)

Project: Store Sales Forecasting - Model-as-a-Service (MaaS)
🎯 Objective
To transition a Time-Series Forecasting model (trained on the Kaggle Store Sales dataset) into a Production-Ready Inference Service. This project demonstrates the "Last Mile" of Machine Learning: moving from a notebook to a governed, containerized API.

🛠 Tech Stack
ML Engines: Facebook Prophet (Time-Series), Scikit-Learn (Linear Regression & Neural Networks).

Observability: Prometheus & Grafana (Real-time RED metrics: Requests, Errors, Duration).

Security: Secure JSON Serialization for model persistence (replacing insecure pickles).

API Layer: FastAPI (High-performance, asynchronous).

Governance Integration: Designed for Kong Gateway / MuleSoft (Authentication, Rate-limiting, and Logging).

Infrastructure: Docker, Kubernetes-ready.

🧠 Advanced ML Capabilities
Multi-Model Architecture: Supports baseline Linear Regression for explainability and Multi-Layer Perceptrons (Neural Networks) for non-linear pattern recognition.

Feature Scaling: Integrated StandardScaler pipelines to ensure gradient descent convergence for deep learning layers.

Validation: Optimized for RMSLE to handle retail volatility and log-transformed target variables.

📊 Observability & Monitoring
Live Telemetry: Integrated Prometheus middleware to expose /metrics for production monitoring.

Health Checks: Automated startup events to load models into memory, ensuring zero-latency "cold starts" for the API.

🏗 Architecture
Instead of a monolithic script, this project follows a Microservices pattern:

Data Pipeline: Automated merging of Oil prices, Holiday events, and Store metadata.

Inference Service: A RESTful endpoint that accepts JSON payloads and returns sales forecasts.

Governance Layer: Documentation on how to proxy this service via Kong Gateway to provide OAuth2 security and request transformation.

🚀 Key Features
Feature Engineering: Implemented Weekly Lag features and Payday indicators (15th/30th).

Log-Transformed Training: Optimized for RMSLE (Root Mean Squared Logarithmic Error) to handle retail volatility.

Schema Validation: Used Pydantic to enforce strict data contracts, preventing "Garbage In, Garbage Out."

📈 How to Run
Bash

# Build the production container
docker build -t store-sales-api .

# Run the service
docker run -p 8000:8000 store-sales-api
Access the interactive API docs at http://localhost:8000/docs
