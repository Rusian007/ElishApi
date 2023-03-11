from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.core.validators import RegexValidator
phone_no_regex = RegexValidator(
        regex=r"^01(7|8|3|6)[0-9]{8}", message="phone no format = 8801xxxxxxxxx"
)
class CustomUser(AbstractUser):
    phone_no = models.CharField(
        validators=[phone_no_regex], max_length=17, unique=True, default=None
    )
    route_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100, null=False)
    assigned_counter = models.CharField(max_length=100, null=True)
    

    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('COUNTERMAN', 'CounterMan'),
    )
    role = models.CharField(max_length = 50, choices=ROLE_CHOICES)
    REQUIRED_FIELDS = ["address", "phone_no", "role"]