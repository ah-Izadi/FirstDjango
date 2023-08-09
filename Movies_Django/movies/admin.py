from django.contrib import admin
from .models import gener,movie

class generAdmin(admin.ModelAdmin):
    list_display = ('id','name') 
    
class movieAdmin(admin.ModelAdmin):
    fields = ('name','release_year','Gener','Date_time')
    list_display = ('name','release_year','Gener','Date_time')
admin.site.register(gener, generAdmin)
admin.site.register(movie,movieAdmin)