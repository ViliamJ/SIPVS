import datetime

from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class MyCar(models.Model):
    CAR_GROUP = (("TRUCK", "TRUCK"), ("PERSONAL", "PERSONAL"), ("BUS", "BUS"), ("CYCLE", "CYCLE"))
    first_name = models.CharField(max_length=50, blank=True, null=True)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    ID_number = models.CharField(max_length=8, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True,
                              validators=[RegexValidator(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                                                         message="Enter valid email")])
    car_brand = models.CharField(max_length=30, blank=True, null=True)
    car_type = models.CharField(max_length=30, choices=CAR_GROUP, blank=False, null=True)
    spz = models.CharField(max_length=7, blank=True, null=True)
    registration_date = models.DateField(default=datetime.date.today())
    vin = models.IntegerField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name
