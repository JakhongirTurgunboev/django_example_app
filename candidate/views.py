from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProfileForm
# Create your views here.
from accounts.models import CustomUser
from candidate.models import Click, Profile
from vacancy.models import Vacancy


def candidate_view(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'candidate.html', context={'jobs': vacancies})


@login_required(login_url='/login')
def job_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        return HttpResponse("Bunday vakansiya yo'q", status=404)
    if request.method == 'POST':
        click_text = request.POST.get('click_text')
        try:
            profile = Profile.objects.filter(account=request.user).first()

        except Profile.DoesNotExist:
            return HttpResponse("Bunday profil yo'q", status=404)
        if profile:
            Click.objects.create(
                vacancy=vacancy,
                text=click_text,
                profile=profile
            )
            messages.add_message(request, messages.INFO, "Your application submitted successfully!")
        else:
            messages.add_message(request, messages.INFO, "First, complete your profile, before submitting application!")
    return render(request, 'vacancy.html', context={'job': vacancy, 'messages': messages})


@login_required(login_url='login/')
def complete_profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            experience = form.cleaned_data["experience"]
            location = form.cleaned_data["location"]
            min_salary = form.cleaned_data["min_salary"]
            comf_salary = form.cleaned_data["comf_salary"]
            birth_date = form.cleaned_data["birth_date"]
            tags = form.cleaned_data["tags"]
            image = form.cleaned_data["image"]
            user = request.user
            try:
                profile = Profile.objects.get(account=user)
                profile.title = title
                profile.experience = experience
                profile.location = location
                profile.min_salary = min_salary
                profile.comf_salary = comf_salary
                profile.birth_date = birth_date
                profile.tags = tags
                profile.image = image
                profile.save()
            except Profile.DoesNotExist:

                Profile.objects.create(
                    account=user,
                    title = title,
                    experience = experience,
                    location = location,
                    min_salary = min_salary,
                    comf_salary = comf_salary,
                    birth_date = birth_date,
                    tags = tags,
                    image=image
                )
        else:
            print("Form validation failed")
    return render(request, "profile.html", {"form": form})


@receiver(post_save, sender=Click)
def my_handler(sender, instance, **kwargs):
    vacancy = Vacancy.objects.get(pk=instance.vacancy.id)
    current_one = vacancy.number_of_clicks
    vacancy.number_of_clicks = current_one + 1
    vacancy.save()
