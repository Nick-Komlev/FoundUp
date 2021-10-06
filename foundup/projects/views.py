from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница приложения Projects")

def pageNotFound(request, exception):
    return HttpResponseNotFound("Заблудился!")