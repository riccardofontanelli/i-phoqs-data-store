import time
import psycopg2
import sys

while True:
    try:
        conn = psycopg2.connect(
            dbname="registrydb",
            user="postgres",
            password="postgres",
            host="db-postgres",
            port="5432"
        )
        conn.close()
        break
    except psycopg2.OperationalError:
        print("⏳ Aspettando che PostgreSQL sia pronto...")
        time.sleep(1)

print("✅ PostgreSQL è pronto! Avvio FastAPI...")