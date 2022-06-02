from django.urls import path
from .import views

urlpatterns=[
     path('', views.home ,name ='get_started'),
    path('/movies' ,views.netflix_home, name="home"),
   
    
]