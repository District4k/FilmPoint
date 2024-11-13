from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    current_stage = models.IntegerField(default=1, blank=True)


class SurveyQuestion(models.Model):
    title = models.CharField(max_length=100, default="Question")
    question = models.TextField()
    filter = models.CharField(max_length=32, default='filter')
    stage = models.IntegerField(default=1)

    def __str__(self):
        return self.question


class SurveyAnswer(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    answer = models.TextField()
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)


class MoviePreference(models.Model):
    user_id = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    year_range = models.CharField(max_length=50)
    region = models.CharField(max_length=50)


class Amenities(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_id = models.IntegerField(unique=True, default=-1)
    name = models.CharField(max_length=128)
    description = models.TextField()
    year = models.TextField()
    image = models.CharField(max_length=500)
    rating = models.FloatField(default=0)
    genre = models.CharField(max_length=250)

    # amenities = models.ManyToManyField(Amenities)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.comment


class Question(models.Model):
    question = models.CharField(max_length=128)
    score = models.IntegerField()

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=128)

    def __str__(self):
        return self.answer


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Watchlist"
