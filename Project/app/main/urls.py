from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("info/", views.info, name="info"),    
    path("contact/", views.сontact, name="contact"),
]
