from django.urls import path

from . import views

urlpatterns = [
    path('summition', views.summition, name='summition'),
]