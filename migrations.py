import os

app = input("App name or general ")
app_command = ''

if app != '':
    app_command = app


os.system("python manage.py makemigrations " + app_command)

os.system("python manage.py makemigrations " + app_command)
