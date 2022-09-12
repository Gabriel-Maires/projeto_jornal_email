from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('edicoes/', views.email_visualizer, name='email_visualizer'),
    path('newsletter/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('edicoes/<str:id>', views.email_visualizer, name='email_visualizer'),

]
