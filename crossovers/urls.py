from django.urls import path
from . import views
urlpatterns = [
    path('',views.crossovers_page,name='crossovers_page')
]