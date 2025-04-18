#!/bin/sh
python /app/wait_for_postgres.py
uvicorn app.main:app --host 0.0.0.0 --port 8000