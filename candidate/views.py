from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from vacancy.models import Vacancy


def candidate_view(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'candidate.html', context={'jobs': vacancies})


def job_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        return HttpResponse("Bunday vakansiya yo'q", status=404)
    return render(request, 'vacancy.html', context={'job': vacancy})