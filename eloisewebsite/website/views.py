from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'website/index.html')


def products(request):
    return HttpResponse('Products')


def conatct(request):
    return HttpResponse('Contact')
