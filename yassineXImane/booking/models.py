from django.db import models

# Create your models here.
class Ride(models.Model):
    status_choices = (
        ('Pending','Pending'),
        ('Declined','Declined'),
        ('Accepted','Accepted')
    )
    PickUpLocation=models.CharField(max_length=100)
    DropLocation=models.CharField(max_length=100)
    PriceMAD=models.IntegerField()
    status = models.CharField(max_length=20, choices=status_choices,default='Pending')