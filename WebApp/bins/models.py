from django.db import models
from django.contrib.auth.models import User


class Bins(models.Model):
    field_addres = models.CharField(
        max_length=100,
        help_text='Адрес мусорки'
    )
    field_data = models.IntegerField(
        default=0,
        help_text='Процент заполнености мусорки '
    )
    field_waste = models.IntegerField(
        default=0,
        help_text='Второй датчик'
    )
    ip_addres = models.CharField(
        max_length=11,
        help_text='ip address'
    )
    cordinates_x = models.FloatField(
        help_text='Координата мусорки',
        default=0.0
    )
    corfinates_y = models.FloatField(
        help_text='Координата мусорки',
        default=0.0
    )
    state = models.BooleanField(
        help_text='Состояние мусорки',
        default=False
    )

    def ref(self, data):
        self.field_data = data
        self.save()


class Record(models.Model):
    bin = models.IntegerField(
        help_text='id мусорки'
    )
    value = models.IntegerField(
        help_text='Новое значение'
    )
    date = models.DateField(
        auto_now_add=True
    )
    operation = models.CharField(
        default='обновление данных',
        max_length=17,
        help_text=''
    )
