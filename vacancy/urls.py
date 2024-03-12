from django.contrib import admin
from django.urls import path

from .views import employer_view, employer_detail, new_job

urlpatterns = [
    path('', employer_view),
    path('<int:id>/', employer_detail),
    path('new-job/<int:id>/', new_job),
]