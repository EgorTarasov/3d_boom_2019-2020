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
            name = f.data['tittle']
            description = f.data['description']
            post = Bins( field_addres=name, ip_addres=description)
            post.save()
        else:
            context['form'] = f
    else:
        context['form'] = BinForm()
    return render(request, 'bin.html', context)