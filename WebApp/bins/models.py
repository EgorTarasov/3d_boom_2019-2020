from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Bins (models.Model):
    field_addres = models.CharField(max_length=100, help_text='Адрес мусорки')
    field_data = models.IntegerField(default=0, help_text='Процент заполнености мусорки ')
    ip_addres = models.CharField(max_length=11, help_text='ip addres')
    cordinates_x = models.FloatField(help_text='Координата мусорки', default=55.785078)
    corfinates_y = models.FloatField(help_text='Координата мусорки', default=37.453163)
    def ref(self, data):
            self.field_data = data
            self.save()