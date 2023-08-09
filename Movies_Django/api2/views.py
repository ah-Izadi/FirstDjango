from django.shortcuts import render
from movies.models import movie,gener
import json
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

def GETmovies(request):

    Film = movie.objects.all()
    filmlist = list(Film)
    movies = {'movies':[]}
    for id in range(len(filmlist)):
        movies['movies'].append({'name':str(filmlist[id])})
    return JsonResponse(movies)

@csrf_exempt
def ADDmovies(request):
    data =json.loads(request.body)
    if not "name" in data or not "year" in data or not "genre" in data:
        return HttpResponse('name/year/genre argument doesnot exist')
    
    filmParam = data["name"]
    yearParam = data["year"]
    genreParam = data["genre"]
     
    filmName = movie.objects.filter(name=filmParam)
    genre_id = gener.objects.filter(name=genreParam).first().id
    
    if filmName:
        return HttpResponse('movie exists')
    elif not filmName:
        movie.objects.create(name=filmParam,release_year=yearParam,Gener=gener(genre_id),Date_time=timezone.now())

    return HttpResponse('Movie inserted')

@csrf_exempt
def DELmovies(request):
    data =json.loads(request.body)
    if not "name" in data:
        return HttpResponse('name argument doesnot exist')
    filmname = data["name"]
    FilmId = movie.objects.get(name=filmname).id
    if not FilmId:
        return HttpResponse('movie doesnot exists')
    elif FilmId:
        m = movie.objects.filter(id=FilmId).delete()
        return HttpResponse('your movie deleted')

@csrf_exempt
def UPDmovies(request):
    
    data = json.loads(request.body)
    if not "name" in data and not "new_name" in data:
        return HttpResponse('new_name/name argument doesnot exist')
    
    old_name = data["name"]
    new_name = data["new_name"]
    
    old_name_obj = movie.objects.filter(name=new_name)
    
    if old_name_obj:
        return HttpResponse('new name exists')
    else :
        movieupdate = movie.objects.get(name=old_name)
        movieupdate.name = new_name
        movieupdate.save()
        return HttpResponse('succes update your movie')