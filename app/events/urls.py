"""
URL configuration for film_point project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from events import views

urlpatterns = [
    path('', views.index, name='index'),
    path('survey/', views.intro_survey, name='intro_survey'),
    path('get_recommendations/', views.get_recommendations, name='get_recommendations'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('add_to_watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('delete_from_watchlist/', views.delete_from_watchlist, name='delete_from_watchlist'),
    path('retake_survey/', views.retake_survey, name='retake_survey'),
]
