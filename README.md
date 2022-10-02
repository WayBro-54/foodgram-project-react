
[![foodgram-project-react](https://github.com/Waybro-54/foodgram-project-react/actions/workflows/food_workflow.yaml/badge.svg)](https://github.com/Waybro-54/foodgram-project-react/actions/workflows/food_workflow.yaml)

### Администратор
Логин: `dev1@dev.ru`
Пароль: `def`

### адресс проекта
http://84.252.142.15

### Описание проекта  

Приложение для поиска и создания новых рецептов.

### Список технологий
- Python 3.10
- Django 3.2.19
- Django Rest Framework  3.12.4
- djoser 2.1.0
- Yandex Cloud
- PostgreSQL
- Gunicorn
- Docker
- Nginx

### Для запуска проекта нужно

- выполнить команду<br>
```
git clone https://github.com/WayBro-54/foodgram-project-react.git
```
- добавть в папке Infra файл .env содержимым<br>

```bash
DB_ENGINE=django.db.backends.postgresql - # указываем, что работаем с postgresql
DB_NAME=postgres # указываем имя базы данных
POSTGRES_USER=postgres # задаем логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # устанавливаем пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

выполнить команду для запуска контейнеров:
```
sudo docker-compose up -d 
```

Скрипты сбора статики и наполнения ингридиентами находятся в файле entrypoint.sh


## Запуск проекта в Docker
Для запуска приложения в контейнерах установите Docker на ваш компьютер (сервер). 


### Информация по API
`http://84.252.141.70/api/docs/redoc.html`
