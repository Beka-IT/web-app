from django.shortcuts import render
from main.models import Films
from . import forms
def search_film(request):
    form = request.POST
    films = Films.objects.all().filter(name__startswith=form['name'])
    return render(request,'search/search.html',{'films':films})
