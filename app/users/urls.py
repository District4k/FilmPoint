from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('watchlist/', views.watchlist, name='watchlist'),

]