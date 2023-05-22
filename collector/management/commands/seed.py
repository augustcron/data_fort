import requests
import time
import os
from dotenv import load_dotenv


from django.core.management.base import BaseCommand
from ...models import City, Weather


load_dotenv()
API_KEY = os.getenv('API_KEY')





class Command(BaseCommand):
    help = 'Populate City table with top 50 cities by population'


    def get_top_50_cities_by_populations(self):
        cities_count = 50
        url = f"https://data.opendatasoft.com/api/records/1.0/search/?dataset=geonames-all-cities-with-a-population-1000%40public&q=&lang=en&rows={cities_count}&sort=population" # noqa
        r = requests.get(url)
        initial_data = r.json()["records"]
        final_data = []
        for index, element in enumerate(initial_data):
            intermediate_data = {
                "id": index + 1,
                "name": element["fields"]["ascii_name"],
                "country": element["fields"]["cou_name_en"],
                "population": element["fields"]["population"],
                "lat": element["fields"]["coordinates"][0],
                "lon": element["fields"]["coordinates"][1],
            }
            final_data.append(intermediate_data)

        return final_data


    def update_weather_data(self):
        for city in City.objects.all():
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={city.lat}&lon={city.lon}&appid={API_KEY}&units=metric")
            data = response.json()

            weather_data = Weather( 
                    city=city,
                    condition=data["weather"][0]["main"],
                    condition_description=data["weather"][0]["description"],
                    average_temp=data["main"]["temp"],
                    feels_like_temp=data["main"]["feels_like"],
                    min_temp=data["main"]["temp_min"],
                    max_temp=data["main"]["temp_max"],
                    pressure=data["main"]["pressure"],
                    humidity=data["main"]["humidity"],
                )
            weather_data.save()


    def handle(self, *args, **options):
        cities = self.get_top_50_cities_by_populations()
        for city_data in cities:
            city = City(
                name=city_data['name'],
                country=city_data['country'],
                population=city_data['population'],
                lat=city_data['lat'],
                lon=city_data['lon']
            )
            city.save()
        
        
        while True:
            self.update_weather_data()
            time.sleep(3600)
