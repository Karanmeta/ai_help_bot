FROM python:3.10-slim

WORKDIR /app

# Install system dependencies if any
# RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copy requirements first to leverage Docker cache
COPY requirements.txt requirements.txt

# Install python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY ./app /app