from django.contrib import admin
from django.urls import path

from accounts.views import post_login, registration, logout_view

urlpatterns = [
    path('login/', post_login),
    path('', registration),
    path('logout/', logout_view)
]