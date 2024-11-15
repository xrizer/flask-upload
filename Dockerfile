# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Create upload directory
RUN mkdir -p /app/uploaded_images

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app