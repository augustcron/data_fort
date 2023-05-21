# Generated by Django 4.2.1 on 2023-05-21 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('country', models.CharField(max_length=70)),
                ('population', models.IntegerField()),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('condition', models.CharField(max_length=70)),
                ('condition_description', models.CharField(max_length=255)),
                ('average_temp', models.FloatField()),
                ('feels_like_temp', models.FloatField()),
                ('min_temp', models.FloatField()),
                ('max_temp', models.FloatField()),
                ('pressure', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.city')),
            ],
        ),
    ]