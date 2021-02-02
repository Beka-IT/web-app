from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:film_id>',views.film_page,name='film_page')
]