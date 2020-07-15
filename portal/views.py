from django.shortcuts import render


def home(request):
    # renderiza um template
    return render(request, 'portal/home.html', {'name': 'Erickson'})
