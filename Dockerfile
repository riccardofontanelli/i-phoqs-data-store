FROM python:3.10-slim

WORKDIR /app
COPY ./app /app/app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn requests sqlalchemy psycopg2-binary

COPY ./app/wait_for_postgres.py /app/wait_for_postgres.py
COPY ./start.sh /app/start.sh
RUN chmod +x /app/start.sh

EXPOSE 8000

CMD ["/app/start.sh"]