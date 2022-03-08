from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import datetime

# Create your views here.
def index(request):
    return HttpResponse("Merhaba, Hoşgeldiniz.")

def simdikizaman(request):
    simdi = datetime.datetime.now()
    html = "<html> <body> Simdi %s.</body></html>" %simdi
    return HttpResponse(html)