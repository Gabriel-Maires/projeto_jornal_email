from django.shortcuts import render

from .models import Email


# Create your views here.
def email_visualizer(request):
    emails = Email.objects.all()
    return render(request, 'email_visualizer.html', {'emails': emails})
