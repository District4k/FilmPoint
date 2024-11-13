from django.test import TestCase
from django.urls import reverse
from .models import Watchlist, Movie

from django.test import TestCase, Client
from django.urls import reverse
from .models import SurveyAnswer, User

class RetakeSurveyViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass', current_stage=2)
        self.client = Client()
        self.client.login(username='testuser', password='testpass')

        self.answer1 = SurveyAnswer.objects.create(user=self.user, question_id=1, answer='Answer 1')
        self.answer2 = SurveyAnswer.objects.create(user=self.user, question_id=2, answer='Answer 2')

    def test_retake_survey_resets_stage(self):
        self.client.post(reverse('retake_survey'), {'reset': 'reset'})
        self.user.refresh_from_db()
        self.assertEqual(self.user.current_stage, 1)

    def test_retake_survey_deletes_answers(self):
        self.client.post(reverse('retake_survey'), {'reset': 'reset'})
        answers = SurveyAnswer.objects.filter(user=self.user)
        self.assertEqual(answers.count(), 0)

    def test_retake_survey_redirects(self):
        response = self.client.post(reverse('retake_survey'), {'reset': 'reset'})
        self.assertRedirects(response, reverse('intro_survey'))

class WatchlistModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.movie = Movie.objects.create(movie_id=1, name='Test Movie', description='description', year=2020,image='',rating=7.5, genre='comedy')
        self.watchlist = Watchlist.objects.create(user=self.user, movie=self.movie)

    def test_watchlist_creation(self):
        self.assertEqual(self.watchlist.user.username, 'testuser')
        self.assertEqual(self.watchlist.movie.name, 'Test Movie')
        self.assertEqual(Watchlist.objects.count(), 1)

    def test_watchlist_str(self):
        expected_str = "testuser's Watchlist"
        self.assertEqual(str(self.watchlist), expected_str)
