from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Country)
admin.site.register(models.City)
admin.site.register(models.Plane)
admin.site.register(models.Airport)
admin.site.register(models.Pilot)
admin.site.register(models.Flight)
admin.site.register(models.Customer)
admin.site.register(models.Ticket)
