from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path('home', views.index, name="dashboard"),

]