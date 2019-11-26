from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, '../templates/index.html')

def programming(request):
    return render(request, '../templates/programming.html')
