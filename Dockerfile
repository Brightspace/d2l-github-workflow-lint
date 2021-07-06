FROM python:3-alpine@sha256:709505ac2ed5824430abb76db8cd24c45415aa1f267e133546977e0b18241d3e
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY lint.py ./

CMD ["python", "/app/lint.py"]
