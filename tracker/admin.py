from django.contrib import admin
from .models import Vehicle,Delivery,Location
# Register your models here.


admin.site.register(Vehicle)
admin.site.register(Delivery)
admin.site.register(Location)