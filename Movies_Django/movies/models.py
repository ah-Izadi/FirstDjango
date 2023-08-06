from django.db import models
from django.utils import timezone

class gener(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class movie(models.Model):
    name = models.CharField(max_length=200)
    release_year = models.IntegerField()
    Gener = models.ForeignKey(on_delete=models.CASCADE ,to=gener)
    Date_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    