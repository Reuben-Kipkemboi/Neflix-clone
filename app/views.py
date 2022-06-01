from django.shortcuts import render
from django.views.generic import ListView
import  requests

# Create your views here.

def netflix_home(request):
    poster_url= "https://image.tmdb.org/t/p/w500/"
    response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=41ee283e92c80a93f1e33b97fa9b441e')
    movies_response = response.json()
    print(movies_response)
    movies=movies_response['results']

    return render (request, 'index.html',{'movies':movies,})

# https://api.themoviedb.org/3/movie/550?api_key=41ee283e92c80a93f1e33b97fa9b441e


# MY_API_KEY = 'MOVIE_DB_API_KEY'
# base_url = 'https://api.themoviedb.org/3/'
