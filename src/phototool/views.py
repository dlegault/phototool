from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world") 

def homepage(request):
    return HttpResponse("Welcome to phototool!")

def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body bgcolor=black text=white>It is currently %s.</body></html>" % now
    return HttpResponse(html)