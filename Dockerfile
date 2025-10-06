# Dockerfile — FastMCP HTTP server for Boltic

# Use official lightweight Python image
FROM python:3.11-slim

# Environment: safe defaults for container runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install OS-level dependencies (for builds & HTTPS)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /app

# Copy all project files into /app
COPY . /app

# Install Python dependencies
# requirements.txt must be in repo root
RUN python -m pip install --upgrade "pip<25" && \
    pip install -r requirements.txt

# Boltic routes traffic to port 8080
EXPOSE 8080

# Define environment for FastMCP HTTP
ENV MCP_TRANSPORT=streamable-http

# Run your FastMCP server
# This will execute your Starlette app from serverless_app.py
CMD ["python", "serverless_app.py"]
