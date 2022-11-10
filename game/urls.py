from django.urls import path
from . import views

app_name = "game"
urlpatterns = [
    path("",views.intro, name="intro"),
    path("input", views.input, name= "input")
]