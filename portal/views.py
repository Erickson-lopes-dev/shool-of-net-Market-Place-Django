from django.shortcuts import render


def home(request):
    return render(request, 'portal/home.html', {'name': 'Erickson'})
