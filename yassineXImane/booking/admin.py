from django.contrib import admin
from .models import Ride

class RideAdmin(admin.ModelAdmin):
    list_display="PickUpLocation","DropLocation","PriceMAD"

admin.site.register(Ride,RideAdmin)