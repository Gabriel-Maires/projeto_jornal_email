from django.db import models


class Email(models.Model):
    email_title = models.CharField(max_length=200)
    email_text = models.TextField()

    def __str__(self):
        return self.email_title


class Subscribers(models.Model):
    subscriber_email = models.EmailField()

    def __str__(self):
        return self.email


class DayEdition(models.Model):
    title = models.CharField(max_length=300)
    emails = models.ForeignKey(Email, on_delete=models.DO_NOTHING)
    send_to = models.ForeignKey(Subscribers, on_delete=models.DO_NOTHING)
    data = models.DateField()

    def __str__(self):
        return self.title
