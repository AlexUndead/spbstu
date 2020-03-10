from django.db import models
from geo.models import City

class Department(models.Model):
    '''Отдел'''
    name = models.CharField(max_length=100, unique=True, verbose_name="Название отдела")
    description = models.TextField(max_length=260, default='', verbose_name="Краткое описание об отделе")

    def __str__(self):
        return self.name

class Employee(models.Model):
    '''Сотрудник'''
    first_name = models.CharField(max_length=100, verbose_name="Имя работника")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия работника")
    age = models.IntegerField()
    description = models.TextField(max_length=260, default='', verbose_name="Краткое описание о работнике")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'f_name: {} l_name: {} age: {} city: {} department: {}'.format(self.first_name, self.last_name, self.age, self.city, self.department)
