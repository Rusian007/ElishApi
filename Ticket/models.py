from django.db import models

# Create your models here.


class ShortRouteTicket(models.Model):
    starting_point = models.CharField(max_length=100)
    ending_point = models.CharField(max_length=100)

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    fair = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    booked_by = models.CharField(max_length=50)
    counterman_metadata = models.JSONField()

    class Meta:
       indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['booked_by', 'date']),
    ]