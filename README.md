docker-compose down -v

docker-compose up -d --build

docker-compose run --rm web python manage.py createsuperuser


command: sh -c "python /code/manage.py makemigrations && 
                    python /code/manage.py migrate && 
                    python /code/manage.py runserver 0.0.0.0:8000 &&
                    python /code/manage.py seed"