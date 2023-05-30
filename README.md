A Password manager website made using django's template

The following tutorials were used: https://docs.djangoproject.com/en/3.1/intro/tutorial01/ and https://www.youtube.com/watch?v=llbtoQTt4qw


Installation guide:
Clone the repository or download the latest release. Navigate to the folder where the manage.py file is and run the command 
```bash
python manage.py runserver
```

If this fails, you might have to use the command 
```bash
python3 manage.py runserver
```
Then you can access the website at http://127.0.0.1:8000/ while the server is running.


Users have to create an account or login to an existing account, by default there should be a superuser account whose username is admin and password is admin. To create a new superuser,
run the command
```bash
python manage.py createsuperuser
```

If you get an error and you are using git bash from windows you might have to use the command 

```bash
winpty python manage.py createsuperuser
```