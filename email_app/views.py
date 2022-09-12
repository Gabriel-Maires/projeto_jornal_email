from django.shortcuts import render, redirect

from .models import DayEdition, Email, Subscribers


# Create your views here.
def email_visualizer(request):
    emails = Email.objects.all()
    return render(request, 'email_visualizer.html', {'emails': emails})


def homepage(request):
    editions = DayEdition.objects.all()
    return render(request, 'homepage.html', {'editions': editions})


def newsletter_subscribe(request):
    if request.method == "GET":
        return render(request, 'subscribe_page.html')
    if request.method == "POST":
        email = request.POST.get('email')

        subscriber = Subscribers(subscriber_email=email)
        subscriber.save()

        return redirect('/newsletter/')
