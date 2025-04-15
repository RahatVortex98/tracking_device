from django.urls import path
from tracker.views import track_delivery, dashboard

urlpatterns = [
    path('track/', track_delivery, name='track_delivery'),
    path('dashboard/', dashboard, name='dashboard'),
]