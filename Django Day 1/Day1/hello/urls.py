from django.urls import path
from django.urls.resolvers import URLPattern

from .views import homepageView
urlpatterns =[
    path('',homepageView,name='Hello'),
]