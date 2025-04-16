# Domain Checker
asdfasdf
`Domain Checker` — это Python-приложение для проверки доступности списка доменов. Если домен недоступен или возвращает код ответа HTTP, отличный от `200`, приложение отправляет уведомление в Telegram.

## Функциональность

- Проверка доступности доменов через HTTP GET-запросы.
- Отправка уведомлений в Telegram при недоступности домена.
- Настройка через файл `.env`.

## Требования

- Python 3.9+
- Docker (опционально, для запуска в контейнере)

## Установка и запуск

### 1. Локальный запуск

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ваш_пользователь/domain_checker.git
   cd domain_checker
   ```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` и настройте переменные:

   ```env
   BOT_TOKEN=ваш_токен_бота
   CHAT_ID=ваш_chat_id
   DOMAINS=example.com,anotherexample.com
   CHECK_INTERVAL=60
   ```

4. Запустите приложение:
   ```bash
   python domain_checker.py
   ```

### 2. Запуск через Docker

1. Соберите Docker-образ:

   ```bash
   docker build -t domain_checker .
   ```

2. Запустите контейнер:
   ```bash
   docker run --env-file .env -d domain_checker
   ```

### 3. Запуск через Docker Compose

1. Убедитесь, что файл `docker-compose.yml` настроен правильно.

2. Запустите контейнер:
   ```bash
   docker-compose up -d
   ```

## Переменные окружения

- `BOT_TOKEN` — токен вашего Telegram-бота.
- `CHAT_ID` — ID чата, куда будут отправляться уведомления.
- `DOMAINS` — список доменов для проверки, разделенных запятыми.
- `CHECK_INTERVAL` — интервал проверки доменов в секундах (по умолчанию: 60).

## Пример уведомления

Если домен недоступен, вы получите сообщение в Telegram, например:

```
Домен example.com недоступен: HTTPSConnectionPool(host='example.com', port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x...>: Failed to establish a new connection: [Errno -2] Name or service not known'))
```
