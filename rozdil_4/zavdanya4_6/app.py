import time
import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    # Робимо кілька спроб підключення, оскільки БД може запускатися довше за застосунок
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host='db', # Ім'я сервісу з docker-compose
                database=os.environ.get('POSTGRES_DB'),
                user=os.environ.get('POSTGRES_USER'),
                password=os.environ.get('POSTGRES_PASSWORD')
            )
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            time.sleep(2)
    return None

@app.route('/')
def hello():
    conn = get_db_connection()
    if conn:
        return "Привіт! З'єднання з PostgreSQL успішне!"
    else:
        return "Помилка: Не вдалося з'єднатися з базою даних."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)