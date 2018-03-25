from django.urls import path

from . import views

urlpatterns = [
    path('prajapati', views.summition, name='summition'),
    path('prajapatip', views.index, name='index'),
]