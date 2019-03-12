from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from .models import Athlete


# Create your views here.
def home_page(request):
    template_full_path ='C:/Users/Wei Chin/trng_app/trngapp/templates/home.html'
    return render(request, template_full_path)

def our_athletes(request):
    template_full_path = 'C:/Users/Wei Chin/trng_app/trngapp/templates/our_athletes.html'
    athletes = Athlete.objects.all()
    return render(request, template_full_path, {'athletes':athletes})