docker-compose down -v
docker-compose up -d --build
docker-compose run web python manage.py createsuperuser
