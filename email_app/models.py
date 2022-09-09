from tkinter import CASCADE
from django.db import models


# Create your models here.
class Email(models.Model):
    email_title = models.CharField(max_length=200)
    email_text = models.TextField()

    def __str__(self):
        return self.email_title


class Subscribers(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Jornal(models.Model):
    title = models.CharField(max_length=200)
    users_destiny = models.ForeignKey(Subscribers, on_delete=models.DO_NOTHING)
