python manage.py makemigrations

# Apply any outstanding database migrations
python manage.py migrate

gunicorn conf.wsgi:application