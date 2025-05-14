web: gunicorn acersite.wsgi --log-file -
web: python manage.py migrate && gunicorn acersite.wsgi