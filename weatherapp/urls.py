from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

URLPatterns = [
    path('', views.index),
]