from django.db import models

class Country(models.Model):
    '''Cтрана'''
    name = models.CharField(max_length=100, verbose_name="Название страны")

    def __str__(self):
        return self.name

class City(models.Model):
    '''Город'''
    name = models.CharField(max_length=100, verbose_name="Название города")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
