FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY config.py .
COPY templates ./templates

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "app.py"]
