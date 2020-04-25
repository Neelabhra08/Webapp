from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')

def work(request):
    return render(request, 'Homework.html')

def report(request):
    return render(request, 'previous class report.html')

def profile(request):
    return render(request, 'my profile.html')

def routine(request):
    return render(request, 'my routine.html')



