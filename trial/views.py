from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def format(request):
    return HttpResponse("Hello Nissi")

def info(request,value):
    return render(request, "trial/info.html",{
        "value":value
    })



