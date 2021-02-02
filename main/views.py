from django.shortcuts import render
from .models import FutureFilms,Films

def index(request):
    future_films = FutureFilms.objects.all()[:5]
    films = Films.objects.order_by('-premiere_year')[:5]
    context = {"f_films":future_films,"films":films}

    return render(request,'main/main.html',context)
