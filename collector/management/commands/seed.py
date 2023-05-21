import requests
from django.core.management.base import BaseCommand
from ...models import City



class Command(BaseCommand):
    help = 'Populate City table with top 50 cities by population'


    def handle(self, *args, **oprions):
        cities = get_top_50_cities_by_populations()
        for city_data in cities:
            city = City(
                name=city_data['name'],
                country=city_data['country'],
                population=city_data['population'],
                lat=city_data['lat'],
                lon=city_data['lon']
            )
            city.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated City table.'))



def get_top_50_cities_by_populations():
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