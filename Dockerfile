FROM python:3.11-slim

# Security: never run as root in production
RUN adduser --disabled-password --gecos "" appuser

WORKDIR /app

# Copy deps first so this layer is cached unless requirements.txt changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Make startup script executable
RUN chmod +x start.sh

# Switch to non-root user
USER appuser

# Cloud Run injects $PORT at runtime (default 8080).
# start.sh seeds the vector store on cold start, then launches uvicorn.
CMD ["/bin/sh", "start.sh"]

