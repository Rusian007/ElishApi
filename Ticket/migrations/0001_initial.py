# Generated by Django 4.0.2 on 2023-02-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_point', models.CharField(max_length=100)),
                ('ending_point', models.CharField(max_length=100)),
                ('route_id', models.PositiveIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('fair', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(default=0)),
                ('booked_by', models.CharField(max_length=50)),
                ('counterman_metadata', models.JSONField()),
            ],
        ),
        migrations.AddIndex(
            model_name='ticket',
            index=models.Index(fields=['date'], name='Ticket_tick_date_9430a5_idx'),
        ),
        migrations.AddIndex(
            model_name='ticket',
            index=models.Index(fields=['booked_by', 'date'], name='Ticket_tick_booked__3cd09d_idx'),
        ),
    ]
