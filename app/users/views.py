from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from events.models import Watchlist, Movie
from .forms import RegisterForm


def index(request):
    return render(request, 'events/index.html')


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created!')
            return redirect('index')
        messages.error(request, 'There was an error with your registration. Please try again.')
    form = RegisterForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('index')
            messages.error(request, 'Invalid username or password.')
        messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')


def profile(request):
    user = request.user
    return render(request, 'events/profile.html', {'user': user}, )


def watchlist(request):
    movie_ids_in_watchlist = Watchlist.objects.filter(user=request.user).values_list('movie_id', flat=True)
    movies_in_watchlist = Movie.objects.filter(id__in=movie_ids_in_watchlist)
    user = request.user

    return render(request, 'events/watchlist.html', {'movies': movies_in_watchlist, 'user': user}, )  #
