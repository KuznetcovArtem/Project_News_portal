# Новостной портал

## Учебный проект на онлайн-курсе Fullstack разработчик на Python

### Как установить
Python3 должен быть уже установлен. <br>
Для установки зависимостей
```commandline
pip install -r requirements.txt
```

Для запуска в корне проекта нужно создать файл .env со следующими настройками:
````python
# Development settings

# Yandex.ru
EMAIL_HOST_YANDEX=<Сервер исходящей почты>
EMAIL_PORT_YANDEX=<Порт исходящей почты>
EMAIL_HOST_USER_YANDEX=<Имя пользователя>
EMAIL_HOST_PASSWORD_YANDEX=<Пароль пользователя>
DEFAULT_FROM_EMAIL_YANDEX=<Полный адрес пользователя исходящей почты>
````

## Основные страницы:<br>
[Backend - admin/admin](http://127.0.0.1:8000/admin/)<br>
[Главная](http://127.0.0.1:8000/news/)<br>
[Залогиниться для пользователя](http://127.0.0.1:8000/accounts/login/)<br>
[Разлогиниться для пользователя](http://127.0.0.1:8000/accounts/logout/)<br>

### Запуск сервера на локальной машине
```commandline
python manage.py runserver
```

### (6.7.1) Команда на запуск автоматического оповещения через django-apscheduler, рассылка настроена на каждую пятницу в 18:00: 
```commandline
python manage.py runapscheduler
```

## Redis
### Далее для работы необходим брокер сообщений. В проекте использовался Redis. [Инструкция по установке для MacOS доступна по ссылке:](https://questpro.club/administration/181-redis-installation-on-macos-debian-ubuntu-centos/#MacOS_Catalina)
### (7.5) п4. Команда на запуск рассылки уведомлений подписчикам через Celery после создания новости:
```commandline
celery -A project worker -l INFO
```

### (7.5) п5. Команда на запуск еженедельной рассылки уведомлений подписчикам через Celery со всеми новостями за прошедшую неделю:
```commandline
celery -A project worker -l INFO -B
```

## Кеширование
### (8.3-8.4) Подключено кеширование:<br> на главную страницу /news/ одна минута;<br> кеширование статьи при изменении;<br> кеширование в шаблоне навигационных эл-тов (меню)<br>
````python
# Filesystem caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}
````

## Уаравляющие команды
### (11.4) Команда удаляет все новости из выбранной категории. <br>
Имена категорий: Economy, Interesting, News, Sport
````commandline
python manage.py deleteallposts <имя_категории>
````
## Логирование
### (13.4) general.log, errors.log, security.log

## Локализация
### (14) Добавлена языкавая локализация, лакализация времени, и отображение тёмной или светлой темы оформления в зависимости от времени пользователя.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе "Fullstack разработчик на Python" [Skillfactory.ru](https://skillfactory.ru)