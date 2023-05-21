docker-compose down -v

docker-compose up -d --build

docker-compose run --rm web python manage.py createsuperuser
