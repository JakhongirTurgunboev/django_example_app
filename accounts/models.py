from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username must be set')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        # Ensure that only superusers can be created using this method
        extra_fields.setdefault('type', 'S')

        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('S', 'Superuser'),
        ('E', 'Employer'),
        ('C', 'Candidate'),
    )
    objects = UserManager()

    REQUIRED_FIELDS = []
    type = models.CharField(choices=USER_TYPES, default='S', max_length=1)


class Profile(models.Model):
    account = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    experience = models.FloatField(default=0)
    location = models.CharField(max_length=250)
    min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    comf_salary = models.DecimalField(max_digits=10, decimal_places=2)
    birth_date = models.DateField()
    tags = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/images/', null=True, blank=True)


@receiver(post_save, sender=CustomUser)
def update_stock(sender, instance, **kwargs):
    if instance.type == 'C':
        try:
            profile = Profile.objects.get(pk=instance.profile)

            profile.account = instance,
            profile.title = 'Software Engineer',
            profile.location = 'Tashkent',
            profile.min_salary = '0',
            profile.comf_salary = '100',
            profile.birth_date = datetime.now().date()
            profile.save()

        except:
            pass
