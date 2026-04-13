import time
import psycopg2
import os

while True:
    try:
        conn = psycopg2.connect(
            dbname=os.environ["POSTGRES_DATABASE"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            host=os.environ["POSTGRES_HOST"],
            port="5432",
        )
        conn.close()
        print("Postgres is ready!")
        break
    except psycopg2.OperationalError:
        print("Waiting for Postgres...")
        time.sleep(2)