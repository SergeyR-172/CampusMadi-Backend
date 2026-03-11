# CampusMadi-Backend

## Алгоритм запуска проект

1. Установить Docker Desktop.
2. В корне проекта выполнить:

```bash
docker compose up --build
```

Тогда по адресу `http://localhost:8000/docs` появится документация по реализованным ручкам.

login возвращает в ответе выданный access токен и задает его в cookies.
Для проверки ручки me нужно или в документации вставить токен в Authorize, или в формате запроса к серверу добавить заголовок формата 'Authorization: Bearer <access_token>'

Пока в приложении пользователи заранее определены:
```json
{
        "username": "test_admin",
        "password": "admin123",
        "name": "Test Admin",
        "role": "admin",
    },
    {
        "username": "test_teacher",
        "password": "teacher123",
        "name": "Test teacher",
        "role": "teacher",
    },
    {
        "username": "test_user_1",
        "password": "user123",
        "name": "Test User 1",
        "role": "default",
    },
    {
        "username": "test_user_2",
        "password": "user123",
        "name": "Test User 2",
        "role": "default",
    },
```
