from ast import Constant
from os import environ
from django.shortcuts import render
from django.views.generic import ListView
import  requests
from decouple import config

from netflix.settings import THE_MOVIE_DB_API_KEY
# print(settings.THE_MOVIE_DB_API_KEY)

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




# https://api.themoviedb.org/3/movie/550?api_key=41ee283e92c80a93f1e33b97fa9b441e


# MY_API_KEY = 'MOVIE_DB_API_KEY'
# base_url = 'https://api.themoviedb.org/3/'
