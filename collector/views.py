# import os
# import requests
# from dotenv import load_dotenv
# from pprint import pprint


# # load_dotenv()

# # API_KEY = os.getenv('API_KEY')


# # url1 = f'http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API_KEY}'
# # url2 = f'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API_KEY}'

# # response = requests.get(url2)

# # json_content = response.json()
# # pprint(json_content)



# def get_top_50_cities_by_populations():
#     cities_count = 50
#     url = f"https://data.opendatasoft.com/api/records/1.0/search/?dataset=geonames-all-cities-with-a-population-1000%40public&q=&lang=en&rows={cities_count}&sort=population" # noqa
#     r = requests.get(url)
#     initial_data = r.json()["records"]
#     final_data = []
#     for index, element in enumerate(initial_data):
#         intermediate_data = {
#             "id": index + 1,
#             "city_name": element["fields"]["ascii_name"],
#             "country_name": element["fields"]["cou_name_en"],
#             "population": element["fields"]["population"],
#             "latitude": element["fields"]["coordinates"][0],
#             "longitude": element["fields"]["coordinates"][1],
#         }
#         final_data.append(intermediate_data)

#     return final_data

# pprint(get_top_50_cities_by_populations())