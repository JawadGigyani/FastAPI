# 1. Start from a small official Python image
FROM python:3.12-slim

# 2. Work inside the /app folder in the container
WORKDIR /app

# 3. Install dependencies first (Docker caches this layer if requirements don't change)
COPY requirements.txt .
RUN pip install -r requirements.txt

# 4. Copy the application code
COPY app ./app

# 5. The API listens on port 8000
EXPOSE 8000

# 6. Start the server (0.0.0.0 makes it reachable from outside the container)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
