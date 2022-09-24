python3 manage.py makemigrations users --no-input
python3 manage.py makemigrations api --no-input
python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input
python3 manage.py loader
gunicorn foodgram.wsgi:application --bind 0:8000