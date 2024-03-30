from django.test import TestCase

# Create your tests here.
from accounts.models import CustomUser
from vacancy.models import Vacancy


class VacancyTestCase(TestCase):
    def setUp(self):
        user = CustomUser.objects.create(
            username='google',
            password='1234'
        )
        Vacancy.objects.create(job_poster=user,
                               location="London",
                               title="Python developer",
                               description="Middle Python developer",
                               tags="#python#django")

    def test_animals_can_speak(self):
        vacancies = Vacancy.objects.filter(title="Python developer")
        vacancy = vacancies[0]
        self.assertEqual(vacancy.location, "London")
