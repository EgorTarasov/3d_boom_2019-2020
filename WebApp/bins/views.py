from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Bins, Record
from .forms import BinForm
from geopy.geocoders import Nominatim
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from datetime import datetime


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def index(request):
    context = dict()
    bins = Bins.objects.all()
    context['bins'] = bins
    return render(request, 'index.html', context)


def set_coordinates(adress):
    geolocator = Nominatim()
    location = geolocator.geocode(adress)
    a, b  = location.latitude, location.longitude
    return a, b


@login_required
def createBin(request):
    context = dict()
    if request.method == 'POST':
        f = BinForm(request.POST)
        if f.is_valid():
            adress = f.data['tittle']
            x, y = set_coordinates(adress)
            post = Bins( field_addres=f.data['tittle'], ip_addres=f.data['description'], cordinates_x=x,
                         corfinates_y=y)
            post.save()
        else:
            context['form'] = f
    else:
        context['form'] = BinForm()
    return render(request, 'bin.html', context)


def refresh(request, bin_id, data):
    bins = Bins.objects.all()
    bin = bins[int(bin_id) - 1]
    old_data = bin.field_data
    bin.ref(data)
    bin.save()
    context = dict()
    posts = Bins.objects.all()
    context['bins'] = posts
    '''
        1 - значение увеличилось
        2 - мусор вывезли
    '''
    if old_data > data:
        record = Record(bin=bin_id, value=data, date=datetime.now(), operation='вывоз мусора')
    else:
        record = Record(bin=bin_id, value=data, date=datetime.now(), operation='обновление данных')
    record.save()
    return render(request, 'index.html', context)


@login_required
def binview(request, bin_id):
    bin_id = int(bin_id) - 1
    bins = Bins.objects.all()
    bin = bins[bin_id]
    context = dict()
    context['addres'] = bin.field_addres
    context['data'] = bin.field_data
    context['ip'] = bin.ip_addres
    context['id'] = bin.id
    context['cordinates_x'] = bin.cordinates_x
    context['corfinates_y'] = bin.corfinates_y
    bin_id += 1
    context['records'] = Record.objects.filter(bin=bin_id)
    return render(request, 'tittle_page.html', context)
