# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Create upload directory
RUN mkdir uploaded_images

# Expose port 8080
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]