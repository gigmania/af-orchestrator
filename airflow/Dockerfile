# Use the specified Airflow version
FROM apache/airflow:2.10.3

# Install system dependencies for PgBouncer
USER root
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        postgresql-contrib \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch back to the airflow user
USER airflow

# Set environment variables based on your values.yaml
ENV AIRFLOW__CORE__EXECUTOR=LocalExecutor  
ENV AIRFLOW__API__AUTH_BACKEND=airflow.api.auth.backend.basic_auth  

# Expose the Airflow webserver port
EXPOSE 8080

# Healthcheck (Important for Kubernetes)
HEALTHCHECK --interval=30s --timeout=30s --retries=3 \
  CMD curl --fail http://localhost:8080/health || exit 1