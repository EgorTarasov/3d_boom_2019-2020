from django import forms


class BinForm(forms.Form):
    tittle = forms.CharField(label='Адрес', max_length=265, min_length=8, required=True)
    description = forms.CharField(label='Адрес в сети', max_length=10000, min_length=1,required=False)
    cordinates_x = forms.FloatField(label='Первая кордината', required=True)
    cordinates_y = forms.FloatField(label='Вторая кордината', required=True)

