from django.urls import path
from . import views
urlpatterns = [
    path('',views.solo_page,name='solo'),
]