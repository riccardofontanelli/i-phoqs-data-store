FROM python:3.10-slim

WORKDIR /app
COPY ./app /app/app

RUN pip install --no-cache-dir fastapi uvicorn requests sqlalchemy psycopg2-binary

CMD ["sh", "-c", "python app/wait_for_postgres.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]