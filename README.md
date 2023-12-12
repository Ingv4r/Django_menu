# Проект Django-menu: 

### Древовидное меню на Django, испоьзуя custom template tag.

[Тестовое задание](https://docs.google.com/document/d/1XTnbcXhejyGB-I2cHRiiSZqI3ElHzqDJeetwHkJbTa8/edit?pli=1)

<br>

## Оглавление:
- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)
- [Описание работы](#описание-работы)
- [Автор](#автор)

<br>

## Технологии:

<details><summary>Подробнее</summary>

Python 3.12, 
Django 5.0. 
Postgress 15.0, 
Nginx 1.22.1


[⬆️Оглавление](#оглавление)
</details>

<br>

## Установка и запуск:
<details><summary>Локальный запуск</summary> 

**!!! Для пользователей Windows обязательно выполнить команду:** 
```bash
git config --global core.autocrlf false
```
иначе файл start.sh при клонировании будет бракован.

1. Клонируйте репозиторий с GitHub:
```bash
git clone https://github.com/Ingv4r/Django_menu.git && \
cd Django_menu && \
nano .env
```
2. Создайте в корневой директории проекта .env-файл:
```
cd tree_menu
nano .env
```
И заполните его по примеру:
```.env
SECRET_KEY=SECRET
DB_ENGINE=django.db.backends.postgresql
#POSTGRES_USER=postgres
#POSTGRES_PASSWORD=PASSWORD
#POSTGRES_DB=tree_menu
#DB_NAME=tree_menu
#DB_HOST=db
#DB_PORT=5432
```
<details><summary>Локальный запуск: Django/SQLite3</summary>

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
```bash
python -m pip install --upgrade pip && pip install -r requirements.txt
```

4. Выполните миграции, создание суперюзера и запустите приложение вручуню или просто выполните команду start.sh:
```bash
chmod +x start.sh && \
./start.sh
```
Затем
```bash
python tree_menu/manage.py runserver
```
ИЛИ вручуную
```bash
python tree_menu/manage.py makemigrations && \
python tree_menu/manage.py migrate && \
python tree_menu/manage.py create_superuser && \
python tree_menu/manage.py runserver
```

Сервер запустится локально по адресу `http://127.0.0.1:8000/`

5. Остановить приложение можно комбинацией клавиш Ctl-C.
<h1></h1>
 </details>

<details><summary>Локальный запуск: Docker Compose/PostgreSQL</summary>

2. Раскоментируйте .env-файл и из корневой директории проекта выполните команду:
```bash
docker compose -f infra/docker-compose.yml up -d --build
```
Проект будет развернут в трех docker-контейнерах (db, web, nginx) по адресу `http://localhost:8080`.

3. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
docker compose -f infra/docker-compose.yml down
```
</details><h1></h1></details>

Меню представлены по адресу (в зависимости от способа запуска):
  - http://localhost:8080/menu/

Вход в админ-зону осуществляется по адресу (в зависимости от способа запуска):
  - http://localhost:8080/admin/

[⬆️Оглавление](#оглавление)

<br>

## Описание работы:

При клике на название меню происходит переход на страницу данного меню. Возврат к списку меню происходит при клике на `К выбору меню`.
Принцип работы приложения основан на выборке из БД всех пунктов меню, которые имеют в поле `menu` название выбранного меню. Название выбранного меню извлекается из url. Далее происходит отображение этого меню. При клике на пункт меню происходит рекурсивный поиск по извлеченным данным, чтобы построить список пунктов которые должны быть открыты на пути к этому пункту меню. Далее данный список передается в шаблон который выводит пункты меню, рекурсивно вызывая себя при выводе развернутых пунктов меню. Такой алгоритм позволяет обратиться к любому пункту меню указав в url только имя меню и его пункт. Например, при вводе url (в зависимости от типа локального запуска)

  - http://127.0.0.1:8000/menu/first%20menu/Menu%20item/
  - http://localhost:8080/menu/first%20menu/Menu%20item/


произойдет переход на пункт меню `Menu item` с отрисовкой всех уровней вложенности меню `first menu` на пути к этому пункту меню.


[⬆️Оглавление](#оглавление)

<br>

[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Игорь Кузьмин](https://github.com/Ingv4r)

[⬆️В начало](#Проект)
