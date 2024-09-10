from django.shortcuts import render
from .models import HomePage

def homepage_view(request):
    homepage = HomePage.objects.first()
    return render(request, 'home.html', {'homepage': homepage})