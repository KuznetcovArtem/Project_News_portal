# Проект новостного портала
## Запуск сервера на локальной машине
```commandline
python manage.py runserver
```

## (6.7.1) Команда на запуск автоматического оповещения через django-apscheduler, рассылка настроена на каждую пятницу в 18:00: 
```commandline
python manage.py runapscheduler
```

## (7.5) п4. Команда на запуск рассылки уведомлений подписчикам после создания новости:
```commandline
celery -A project worker -l INFO
```

## (7.5) п5. Команда на запуск еженедельной рассылки уведомлений подписчикам со всеми новостями за прошедшую неделю:
```commandline
celery -A project worker -l INFO -B
```