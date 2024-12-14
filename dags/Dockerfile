FROM python:3.11-slim

# Install dependencies
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy the DAGs directory
COPY . /opt/airflow/dags

# Set the working directory
WORKDIR /opt/airflow/dags
