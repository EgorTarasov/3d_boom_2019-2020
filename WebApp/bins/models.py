from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Bins (models.Model):
    field_addres = models.CharField(max_length=100, help_text='Адрес мусорки')
    field_data = models.IntegerField(default=0, help_text='Процент заполнености мусорки ')
    ip_addres = models.CharField(max_length=11, help_text='ip addres')
    def ref(self, data):
            self.field_data = data
            self.save()