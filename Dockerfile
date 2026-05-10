FROM python:3.11-slim

# Security: never run as root in production
RUN adduser --disabled-password --gecos "" appuser

WORKDIR /app

# Copy deps first so this layer is cached unless requirements.txt changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Switch to non-root user
USER appuser

# Inform Docker which port the app listens on (documentation + -P flag support)
EXPOSE 8000

# For local development: python -m app.knowledge.ingest must be run once
# separately to seed the vector store before starting the server.
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]

