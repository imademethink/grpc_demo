FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# entrypoint1 uses port 50051, others use 5001-5003
CMD ["python", "main.py"]