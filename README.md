# Простой REST API фото менеджер.

## Описание работы сервера:


* `register/`
Страница регистрации пользователя POST запросы.
* `save_photo/`
Страница загрузки фотографии авторизованным пользователем POST запросы. С указанием необязательных параметров (latitude,
longitude, date, people) 
* `show/`
Страница отображения список фотографий, без мета-данных GET запросы.
* `show/date/`
Страница отображения списка фотографии отфильтрованных по дате (на дату, которую передали) GET запросы. 
* `show/people/`
Страница отображения списка фотографии отфильтрованных по имени человека GET запросы. 
* `show/latitude/longitude/`
Страница отображения списка фотографии отфильтрованных по геолокации GET запросы. 
* `detail_photo/pk/`
Страница отображения фотографии с её мета-данными GET запросы.
* `search_name/`
Страница отображения списка автодополнения по поиску возможных имен людей присутствующих на фотографиях (принимает часть
имени/полное имя) GET и POST запросы.

## Реализация сервера:

Пакетным менеджером в проекте является **Poetry**. \
База данных используется **PostgreSQL**. \
Переменные окружения находятся в файле .env, которые затем подгружаются в настройки с помощью **python-dotenv**. Для 
примера смотрите файл .env_example


## Разворачивание сервера:

_Для быстрого разворачивания сервера используется Docker._

1. Для запуска сервера создайте файл **_.env_** рядом с файлом **_.env_example_** и аналогичный ему.
2. Запустите команду _**`docker-compose up -d`**_.
3. Можете начинать обращаться по соответствующим url'ам.


## Доступ к серверу:

http://146.185.240.235:8002/