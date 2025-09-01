from django.shortcuts import render

# Create your views here.
# recommendations/views.py
from django.http import JsonResponse
from .models import Movie
from .ml import recommend_by_genre
import pandas as pd

def recommend(request):
    genre = request.GET.get('genre', 'Action')
    movies = pd.DataFrame(list(Movie.objects.all().values()))
    recommendations = recommend_by_genre(movies, genre)
    return JsonResponse(recommendations, safe=False)
