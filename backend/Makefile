# команды

start-dev:
    poetry run uvicorn app.main:app --reload

migrate:
    poetry run alembic revision --autogenerate -m "init" && poetry run alembic upgrade head

# Запуск команд :
# make start-dev
# make migrate