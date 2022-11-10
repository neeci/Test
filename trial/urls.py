from . import views
from django.urls import path

urlpatterns = [
    path("", views.format, name="format"),
    path("<str:value>", views.info, name="info")
    
]