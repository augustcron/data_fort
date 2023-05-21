# import os
# import requests
# from dotenv import load_dotenv
# from pprint import pprint

# from .models import City


# load_dotenv()

# API_KEY = os.getenv('API_KEY')


# # url1 = f'http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API_KEY}'
# # url2 = f'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API_KEY}'

# # response = requests.get(url2)

# # json_content = response.json()
# # pprint(json_content)


# url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
# citi = City.objects.get(id=1)
# print(citi)


# response = requests.get(url)