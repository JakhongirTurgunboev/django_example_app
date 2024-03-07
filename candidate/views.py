from django.shortcuts import render

# Create your views here.
from vacancy.models import Vacancy


def candidate_view(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'candidate.html', context={'jobs': vacancies})