from django.shortcuts import render
from main.models import Films

def solo_page(request):
    solo_films = Films.objects.all().filter(isSolo=True).order_by('premiere_year')
    return render(request,'solo/solo.html',{'solo_films':solo_films})