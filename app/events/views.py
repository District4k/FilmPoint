from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from events.api import get_film_list_by_filter
from .models import Movie, SurveyQuestion, SurveyAnswer, Watchlist


def retake_survey(request):
    current_user = request.user
    current_user.current_stage = 1
    stage_check = 1
    if request.method == 'POST':
        stage_reset = request.POST.get('reset') == "reset"
        if stage_reset:
            current_user.current_stage = 1
            current_user.save()
            answers = SurveyAnswer.objects.filter(user=current_user)
            answers.delete()
            if stage_check == current_user.current_stage:
                return redirect('intro_survey')


def intro_survey(request):
    question_title = None
    current_user = request.user
    user_survey_stage = current_user.current_stage
    # This line of code does this and this
    questions = SurveyQuestion.objects.filter(stage=user_survey_stage)
    if len(questions) > 0:
        question_title = questions[0].title
    stage_limit = 4
    if request.method == 'POST' and user_survey_stage < stage_limit:
        submitted_answer = request.POST.get('answer')
        question_id = request.POST.get('question')
        question = questions.get(id=int(question_id))
        SurveyAnswer.objects.create(
            user=current_user,
            question=question,
            answer=submitted_answer
        )
        current_user.current_stage += 1
        current_user.save()
        return redirect('intro_survey')
    elif user_survey_stage == stage_limit:
        return redirect('get_recommendations')
    return render(request, 'events/movie_survey.html',
                  {'questions': questions, 'question_title': question_title}
                  )


def index(request):
    return render(request, 'events/index.html')


def get_recommendations(request):
    current_user = request.user
    answers = SurveyAnswer.objects.filter(user=current_user)
    answers_list = []
    for answer in answers:
        answers_list.append(answer.answer)
    recommended_movies = get_film_list_by_filter(answers_list, request)
    return render(
        request,
        'events/recommendation.html',
        {'movie': 'movie', 'recommended_movies': recommended_movies}
    )


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, '', {'movies': movies})


def movie_detail(request, movie_name):
    movie = Movie.objects.get(name=movie_name)
    return render(request, '', {'movie': movie})


def add_to_watchlist(request):
    # if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
    movie_id = request.POST.get('movie_id')
    movie_name = request.POST.get('movie_name')
    movie_image = request.POST.get('movie_image')
    movie_year = request.POST.get('movie_year')
    movie_rating = request.POST.get('movie_rating')
    movie_description = request.POST.get('movie_description')
    movie_genre = request.POST.get('movie_genre')

    movie_data = {
        'name': movie_name,
        'image': movie_image,
        'genre': movie_genre,
        'year': movie_year,
        'description': movie_description,
        'rating': movie_rating,
        'movie_id': movie_id
    }

    movie, created = Movie.objects.get_or_create(
        movie_id=movie_id,
        defaults=movie_data
    )

    Watchlist.objects.create(user=request.user, movie=movie)
    return JsonResponse({'status': 'added'})


def delete_from_watchlist(request):
    movie_id = request.POST.get('movie_id')

    movie = get_object_or_404(Movie, movie_id=movie_id)

    watchlist_entry = Watchlist.objects.get(user=request.user, movie=movie)
    watchlist_entry.delete()
    movie_ids_in_watchlist = Watchlist.objects.filter(user=request.user).values_list('movie_id', flat=True)
    movies_in_watchlist = Movie.objects.filter(id__in=movie_ids_in_watchlist)
    return render(request, 'events/watchlist.html', {'movies': movies_in_watchlist})  #
