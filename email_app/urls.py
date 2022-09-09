from django.urls import path

from . import views

urlpatterns = [
    path('', views.email_visualizer, name='email_visualizer'),
]
