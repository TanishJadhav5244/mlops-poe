FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY hello.py test_hello.py monitor_evidently.py ./
CMD ["python", "hello.py"]