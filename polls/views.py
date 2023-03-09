from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><h1>Xandinho é otário</h1></html>")
