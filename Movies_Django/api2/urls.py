from django.urls import path
from .views import GETmovies,ADDmovies,DELmovies,UPDmovies

urlpatterns = [
    path('movie/',GETmovies),
    path('add/',ADDmovies),
    path('del/',DELmovies),
    path('update/',UPDmovies),
]
