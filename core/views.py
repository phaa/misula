from django.http.response import HttpResponse
from django.shortcuts import render

# Todas as views do core aqui
def hello(request):
    return HttpResponse("Olá do core")

