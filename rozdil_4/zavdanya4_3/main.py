import os
from dotenv import load_dotenv


load_dotenv()


def connect_to_database():
    db_url = os.getenv("DB_URL")

    if not db_url:
        print("Помилка: DB_URL не знайдено!")
        return

    print(f"Підключення до бази даних за адресою: {db_url}")


def call_external_api():
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Помилка: API_KEY відсутній!")
        return

    print(f"Використання API ключа: {api_key[:5]}*** (приховано)")


if __name__ == "__main__":
    print("--- Запуск програми ---")

    if os.getenv("DEBUG_MODE") == "True":
        print("Режим: DEBUG")

    connect_to_database()
    call_external_api()