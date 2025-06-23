# FastAPI-Users

## Запуск приложения

- Ручной запуск: `uvicorn main:app --host 0.0.0.0 --reload`

## Линтеры

- Сортировка импортов: `isort .`
- Форматирование кода: `black .` или посмотреть предложения `black --diff --color <расположение файла>`

## Запуск докер контейнеров

- Запустить отдельный контейнер `docker compose up -d pg`. Запуск posstgres

## Работа с alembic

- `alembic init -t async alembic` - инициализировать конфигурацию асинхронной `alembic`
- `alembic revision --autogenerate -m "Описание изменений"` - Создание новой миграции
- `alembic upgrade head` - применение миграций
- `alembic downgrade base` - откат до пустой БД

## Запуск через `gunicorn`
```shell
gunicorn main:main_app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```