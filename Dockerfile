FROM python:3.8.3-alpine3.11
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY lint.py ./

CMD ["python", "/app/lint.py"]
