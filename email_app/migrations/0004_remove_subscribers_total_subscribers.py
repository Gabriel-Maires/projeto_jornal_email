# Generated by Django 4.1.1 on 2022-09-12 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_app', '0003_alter_subscribers_total_subscribers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribers',
            name='total_subscribers',
        ),
    ]