# Generated by Django 4.0.2 on 2023-02-23 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='route_id',
        ),
    ]
