from django.db import models
from tastypie.resources import ModelResource
from movies.models import movie,gener
class MovieResource(ModelResource):
    class Meta:
        queryset = movie.objects.all()
        resource_name = 'movie'
    
    class Meta:
        queryset = gener.objects.all()
        resource_name = 'genre'
