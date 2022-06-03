from ast import Constant
from cmath import log
from os import environ
from django.shortcuts import render, redirect
from django.views.generic import ListView
import  requests
from decouple import config
from django.contrib import messages


#for our forms
from django.contrib.auth.forms import UserCreationForm
from.forms import RegisterForm

from django.contrib.auth import authenticate, login, logout


THE_MOVIE_DB_API_KEY = config('THE_MOVIE_DB_API_KEY')



# Create your views here.



def home(request):
    return render(request, 'home.html')


#-----------Movies ------------------------------------------------------
def netflix_home(request):

    now_playing_movies_request = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key=" + THE_MOVIE_DB_API_KEY)
    now_playing_movies_results = now_playing_movies_request.json()
    now_playing_movies = now_playing_movies_results['results']
    
    # popular ones
    popular = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=" + THE_MOVIE_DB_API_KEY)
    popular_ones = popular.json()
    popular_ones_now = popular_ones['results']
    
    # top rated ones
    top_rated_movies = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=" + THE_MOVIE_DB_API_KEY)
    top_rated_results = top_rated_movies.json()
    top_ratings = top_rated_results['results']
    
    #Upcoming movies
    upcoming_movies = requests.get("https://api.themoviedb.org/3/movie/upcoming?api_key=" + THE_MOVIE_DB_API_KEY)
    upcoming_results = upcoming_movies.json()
    upcomings = upcoming_results['results']
    
    
    #----TV SHOWS--------------------------------------------------------
    
    tv_shows = requests.get("https://api.themoviedb.org/3/tv/popular?api_key=" + THE_MOVIE_DB_API_KEY)
    tv_results =  tv_shows.json()
    shows = tv_results['results']
    
    
    airing_today_tv_shows = requests.get("https://api.themoviedb.org/3/tv/airing_today?api_key=" + THE_MOVIE_DB_API_KEY)
    airing_tv_results =  airing_today_tv_shows.json()
    airing_shows = airing_tv_results['results']
    
    #top rated TV-shows
    top_rated_tv_shows = requests.get("https://api.themoviedb.org/3/tv/airing_today?api_key=" + THE_MOVIE_DB_API_KEY)
    top_rated_tv_shows_results = top_rated_tv_shows.json()
    top_rated = top_rated_tv_shows_results['results']
    
    #on the air
    on_air_results = requests.get("https://api.themoviedb.org/3/tv/on_the_air?api_key=" + THE_MOVIE_DB_API_KEY)
    on_air_tv_shows_results =  on_air_results.json()
    on_air = on_air_tv_shows_results['results']
    
    

    return render (request, 'index.html',{'movies':now_playing_movies,'popular_movies':popular_ones_now, 'up_comings': upcomings ,'top_movies':top_ratings,  'shows':shows,'airing_shows':airing_shows,'top_rated':top_rated,'on_air':on_air})

def register(request):
    form = RegisterForm()
    
    
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "account created for" + user )
            return redirect('login')
        
    return render(request, 'register.html', {'form':form, 'messages':messages})


def login(request):
    
    if request.method =="POST":
        username = request.POST.get('username')
        password= request.POST.get('password')
        
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Seems username or password is invalid")
            
    
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect ('login')





