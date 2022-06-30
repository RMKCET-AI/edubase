from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'eduapp/index.html')


def blog(request):
    return render(request, 'eduapp/blog.html')


def material(request):
    return render(request, 'eduapp/material.html')


def ai(request):
    return render(request, 'eduapp/ai.html')


def cse(request):
    return render(request, 'eduapp/cse.html')

def ece(request):
    return render(request, 'eduapp/ece.html')

def mech(request):
    return render(request, 'eduapp/mech.html')
