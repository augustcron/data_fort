from django.db import models


from django.db import models


class City(models.Model):
    name = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.name


class Weather(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    condition = models.CharField(max_length=70)
    condition_description = models.CharField(max_length=255)
    average_temp = models.FloatField()
    feels_like_temp = models.FloatField()
    min_temp = models.FloatField()
    max_temp = models.FloatField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()

    def __str__(self):
        return f'Погода для города {self.city} на {self.timestamp}'
