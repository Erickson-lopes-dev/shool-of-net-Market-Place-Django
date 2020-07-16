from django.shortcuts import render

from login.form import RegistrationForm


def register(request):
    form = RegistrationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def register_sucess(request):
    pass
