from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    last_maintenance = models.DateField(null=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

class Delivery(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=50)
    destination = models.CharField(max_length=200)
    eta = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('en_route', 'En Route'), ('delivered', 'Delivered')])

class Alert(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    message = models.TextField()
    severity = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    timestamp = models.DateTimeField(auto_now_add=True)