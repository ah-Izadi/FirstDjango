from django.shortcuts import render
from .models import movie,gener
from django.http import HttpResponse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
message = MIMEMultipart()

def index(request):
    titles = [title for title in movie.objects.all()]  
    Geners = [genre.id for genre in gener.objects.all()] 

    context = {
        "movies" : titles,
        "geners" : Geners
    }

    return render(request, "movies\index.html", context)


def detail(request,MovieID):
    film = movie.objects.filter(id= MovieID)
    return HttpResponse(film)
    



































def detailEmail(request,to):
    message.attach(MIMEText("Body"))
    message["from"] = "Python"
    message["to"] = to+'@gmail.com'
    message["subject"] = 'hello'
    
    with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("your email","your app password")
        smtp.send_message(message)
        return HttpResponse("sending.....")