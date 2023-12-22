from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Carlos'})


def sobre(request):
    return HttpResponse("Sobre")
    # Return http response


def contato(request):
    return HttpResponse("Contato")
    # Return http response
