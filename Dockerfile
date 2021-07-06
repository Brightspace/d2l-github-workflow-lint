FROM python:3-alpine@sha256:f278386b0cef68136129f5f58c52445590a417b624d62bca158d4dc926c340df
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY lint.py ./

CMD ["python", "/app/lint.py"]
