from django.shortcuts import render

from .models import DayEdition, Email


# Create your views here.
def email_visualizer(request):
    emails = Email.objects.all()
    return render(request, 'email_visualizer.html', {'emails': emails})


def homepage(request):
    editions = DayEdition.objects.all()
    return render(request, 'homepage.html', {'editions': editions})
