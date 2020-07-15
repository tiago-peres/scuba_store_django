from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text_var = 'This is a Django app web page.'
    return HttpResponse(text_var)