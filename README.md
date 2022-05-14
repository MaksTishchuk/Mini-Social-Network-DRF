<h2 align="center">Mini social network by Django</h2>

Мини социальная сеть на Django Rest Framework.

**Ссылки**:
- [Facebook](https://www.facebook.com/profile.php?id=100012110915966)
- [Telegram](https://t.me/maks_tishchuk)

### Инструменты разработки

**Стек:**
- Python >= 3.8
- Django Rest Framework
- Postgres

## Старт

#### 1) Создать образ

    docker-compose build

##### 2) Запустить контейнер

    docker-compose up

##### 3) Перейти по адресу

    http://127.0.0.1:8080/api/v1/swagger/

## Разработка с Docker

##### 1) Сделать форк репозитория

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) В корне проекта создать .env.dev

    DEBUG=1
    SECRET_KEY=fdsadqw3f32wg<43g3hv$%#@%F$F$$F$F
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

    # Data Base
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DB=social_drf
    POSTGRES_USER=social_drf_user
    POSTGRES_PASSWORD=social_drf_pass
    POSTGRES_HOST=social_drf-db
    POSTGRES_PORT=5432
    DATABASE=postgres

    # Email
    DEFAULT_FROM_EMAIL=your@your.com
    EMAIL_USE_TLS=True
    EMAIL_HOST=your_smtp
    EMAIL_HOST_USER=your@your.com
    EMAIL_HOST_PASSWORD=pass
    EMAIL_PORT=587

##### 4) Создать образ

    docker-compose build

##### 5) Запустить контейнер

    docker-compose up

##### 6) Создать миграции

    docker exec -it social_drf_social_drf_back_1 python manage.py makemigrations

##### 7) Применить миграции

    docker exec -it social_drf_social_drf_back_1 python manage.py migrate

##### 8) Создать суперюзера

    docker exec -it social_drf_social_drf_back_1 python manage.py createsuperuser

##### 9) Если нужно зайти в консоли в проект

    docker exec -it social_drf_social_drf_back_1 bash

##### 10) Если нужно очистить БД

    docker-compose down -v

## License

Copyright (c) 2022-present, makstishchuk - Tishchuk Maksym