from django.urls import path
from .import views

urlpatterns=[
    path('' ,views.netflix_home, name="home")
    
]