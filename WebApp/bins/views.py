from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Bins
from .forms import BinForm

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def index(request):
    context = dict()
    bins = Bins.objects.all()
    context['bins'] = bins
    return render(request, 'index.html', context)

@login_required
def createBin(request):
    context = dict()
    if request.method == 'POST':
        f = BinForm(request.POST)
        if f.is_valid():
            post = Bins( field_addres=f.data['tittle'], ip_addres=f.data['description'], cordinates_x=f.data['cordinates_x'],
                         corfinates_y=f.data['cordinates_y'])
            post.save()
        else:
            context['form'] = f
    else:
        context['form'] = BinForm()
    return render(request, 'bin.html', context)

def refresh(request, bin_id, data):
    bins = Bins.objects.all()
    bin = bins[int(bin_id) - 1]
    bin.ref(data)
    bin.save()
    context = dict()
    posts = Bins.objects.all()
    context['bins'] = posts
    return render(request, 'index.html', context)

def binview(request, bin_id):
    bins = Bins.objects.all()
    bin = bins[int(bin_id) - 1]
    context = dict()
    context['addres'] = bin.field_addres
    context['data'] = bin.field_data
    context['ip'] = bin.ip_addres
    context['id'] = bin.id
    return render(request, 'tittle_page.html', context)