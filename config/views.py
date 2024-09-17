from django.shortcuts import render
from django.http import HttpResponse
from django .views.generic import View

# Create your views here.
def mainpage(request):
    return render(request, "mainpage.html")