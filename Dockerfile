# Use a lightweight Python image
FROM python:3.9-slim

# Install MLflow and its dependencies
RUN pip install mlflow sqlalchemy boto3

# Create a directory for the model storage (Artifacts)
RUN mkdir -p /mlflow/artifacts

# Expose the default MLflow port
EXPOSE 5000

# Start the MLflow server
# --backend-store-uri: Where the metadata (metrics/params) goes
# --default-artifact-root: Where the actual model files (.pkl) are stored
CMD ["mlflow", "server", \
     "--backend-store-uri", "sqlite:///mlflow.db", \
     "--default-artifact-root", "/mlflow/artifacts", \
     "--host", "0.0.0.0", \
     "--port", "5000"]
