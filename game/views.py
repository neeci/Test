from django.shortcuts import render
from django.http import HttpResponse
from django import forms

def intro(request):
    return render(request, "game/intro.html")

def input(request):
    return render(request, "game/input.html")