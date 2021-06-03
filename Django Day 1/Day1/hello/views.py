from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def homepageView(request):
    return HttpResponse('Hello the fucking world of django')
