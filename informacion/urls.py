from django.urls import path
from . import views

app_name = "informacion"

urlpatterns = [
    path('', views.index, name='index'),
]
