from django.db import models

# Create your models here.


class Point(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank =True, null=True)

    def __str__(self):
        return self.name


class Route(models.Model):

    starting_point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name="starting_point")
    ending_point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name="ending_point")

    fair = models.IntegerField()

    distance = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)


