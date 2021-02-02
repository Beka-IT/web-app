from django.shortcuts import render
from main.models import Films
def crossovers_page(request):
    co_films = Films.objects.all().filter(isSolo=False).order_by('premiere_year')
    return render(request,'crossovers/co.html',{'co_films':co_films})
