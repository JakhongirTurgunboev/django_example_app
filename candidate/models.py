from django.db import models

# Create your models here.
from accounts.models import CustomUser, Profile
from vacancy.models import Vacancy


class Click(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)