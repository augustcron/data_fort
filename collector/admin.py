from django.contrib import admin

from .models import City, Weather



class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'population', 'lat', 'lon')


class WeatherAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'timestamp', 'condition', 'average_temp', 'feels_like_temp', 'humidity', 'pressure')

admin.site.register(City, CityAdmin)
admin.site.register(Weather, WeatherAdmin)

