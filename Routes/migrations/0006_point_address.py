# Generated by Django 4.0.2 on 2023-02-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Routes', '0005_rename_endingpoint_route_ending_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
