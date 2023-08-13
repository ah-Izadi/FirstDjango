from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
import json
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

message = MIMEMultipart()

@csrf_exempt
def Send(request):
    data = json.loads(request.body)
    From = data["from"]
    To = data["to"]
    Subject = data["subject"]
    Body = data["body"]
    message.attach(MIMEText(Body))
    message["from"] = From
    message["to"] = To
    message["subject"] = Subject
    with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("=======","+++++++")
        smtp.send_message(message)
        return HttpResponse('Sending.....')