from decouple import config

from django.shortcuts import render
from .models import Delivery, Location, Vehicle, Alert

def track_delivery(request):
    order_id = request.GET.get('order_id', '')
    delivery = None
    latest_location = None

    if order_id:
        try:
            delivery = Delivery.objects.get(order_id=order_id)
            latest_location = Location.objects.filter(vehicle=delivery.vehicle).order_by('-timestamp').first()
        except Delivery.DoesNotExist:
            delivery = None

    return render(request, 'track_delivery.html', {
        'delivery': delivery,
        'latest_location': latest_location,
        'google_maps_api_key': config('GOOGLE_MAPS_API_KEY')  
    })

def dashboard(request):
    vehicles = Vehicle.objects.all()
    alerts = Alert.objects.order_by('-timestamp')[:5]  # Last 5 alerts
    locations = {v.id: Location.objects.filter(vehicle=v).order_by('-timestamp').first() for v in vehicles}
    return render(request, 'dashboard.html', {
        'vehicles': vehicles,
        'alerts': alerts,
        'locations': locations,
        'google_maps_api_key': config('GOOGLE_MAPS_API_KEY')  # Replace with your key
    })