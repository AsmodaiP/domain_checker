import requests
import time
from dotenv import load_dotenv
import os

# Загрузка переменных из .env
load_dotenv()

# Конфигурация Telegram бота
BOT_TOKEN = os.getenv("BOT_TOKEN", "ВАШ_TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID", "ВАШ_CHAT_ID")

# Список доменов для проверки
DOMAINS = os.getenv("DOMAINS", "").split(",")

# Параметры проверки
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))

def send_telegram_message(message):
    """
    Отправка сообщения в Telegram через бот API.
    """
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=data, timeout=10)
        if response.status_code != 200:
            print(f"Ошибка отправки сообщения: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Exception при отправке Telegram сообщения: {e}")


def check_domain(domain):
    """
    Проверка доступности домена методом HTTP GET запроса.
    Если домен недоступен или возвращает не 200, отправляется уведомление.
    """
    url = f"https://{domain}"  # можно добавить https:// если поддерживается
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"Домен {domain} доступен (код ответа: 200)")
        else:
            error_message = f"Домен {domain} вернул код {response.status_code}"
            print(error_message)
            send_telegram_message(error_message)
    except Exception as e:
        error_message = f"Домен {domain} недоступен: {e}"
        print(error_message)
        send_telegram_message(error_message)


def main():
    """
    Главный цикл проверки доменов.
    """
    while True:
        for domain in DOMAINS:
            check_domain(domain)
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
