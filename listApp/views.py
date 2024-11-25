from django.shortcuts import render
from .models import Character

# Create your views here.
def home(request):
    characterList=Character.objects.all();
    return render(request, 'wiki/home.html', {'characterList':characterList})