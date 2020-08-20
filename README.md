# gd-notifications

English:

1.1 update and bugfixes

1.2 - update with friends (only for the original GD) and adding the mute list

Hi there!

You need this program to get notifications in Geometry Dash.

This program is not so easy to set up and is in alpha.

To run this program, you need:

Play market:
- Pydroid - python interpreter

- Pushbullet - notification service

Your own:

- patience)

So, let's get started.
First download Pydroid.

In pydroid, click on the three bars on the top left -> Pip

In the Library name write "requests" and remove the checkmark from "Use prebuild libraries repository"

click install

wait...

Again write "urllib3" and click install

Go back to the side menu and click "Terminal"

There we need to write "python -m pip install https://github.com/NeKitDS/gd.py/archive/master.zip"

Wait...

Go back

Exit Pydroid, let's configure Pushbullet.

You can download it in the play store and signup.

Also go to the browser -> pushbullet.com

Login the account

click on the button on the top right and go to my account

Looking for Access Tokens -> create access token
copy it from the field

go to pydroid -> click on the folder icon -> open -> open config.py from the folder that you downloaded and edit it.

in ACCESS_TOKEN, insert the token that was taken from the site in field

similarly, enter your username and password in userName and password

userName = "username"

password = " password"

Also specify the address of the private server where you want to receive notifications.

By default, this is the server of Nelis, you can specify your own.

After the 1.1 update, you can use the robtop servers

If you want to use them, change switcher to 

switcher = 1-private server

switcher = 0-robtop servers

Click on the folder icon -> save

Open main.py from the same folder as config.py

Click on the lower right button and...

Congratulations! 👏

Русский


1.1 - обновление и фиксы багов

1.2 - обновление с друзьями (только для оригинальной гд) и добавление мут-листа

Привет!

Эта программа нужна для получения уведомлений в Geometry Dash.

Данная программа не так проста в настройке и находится в альфе.

Для запуска этой программы понадобится:

Плей маркет:
- Pydroid — интерпретатор python
- Pushbullet — сервис уведомлений

Свое:

- терпение)

Итак, приступим.
Сначала скачиваем Pydroid - заходим.

В pydroid нажимаем на три полоски слева сверху -> Pip

В Library name пишем requests и снимаем галочку с "Use prebuild libraries repository"

нажимаем install

ждём

Снова пишем urllib3 и нажимаем install

Возвращаемся в боковое меню и нажимаем Terminal

В нем прописываем команду python -m pip install https://github.com/NeKitDS/gd.py/archive/master.zip

Ждём...

ворачиваемся

Пока оставляем Pydroid, приступим к Pushbullet.

Скачиваем его в плей маркете и регаемся.

Также заходим в браузер -> pushbullet.com

Входим в акк

нажимаем на аву сверху справа и идём в my account

Ищем Access Tokens -> create access token
копируем из поля

заходим в pydroid -> нажимаем на папку -> open -> открываем config.py из той папки, которую вы скачали и редактируем его.

в ACCESS_TOKEN в кавычки вставляем токен, который взяли с сайта

аналогично вписываем свой логин-пароль в userName и password

userName = "логин"

password = "пароль"

Также укажите адрес приватного сервера, на котором вы хотите получать уведомления.

По умолчанию это сервер Нелиса, можете указать свой.

После обновления 1.1 можно использовать сервера робтопа

Если вы хотите их использовать, то измените switcher на 

switcher = 1 - приватный сервер

switcher = 0 - сервера робтопа

Нажимаем на папку -> save

Открываем main.py из той же папки, что и config.py

Нажимаем на нижнюю правую кнопку и...

Гц!
