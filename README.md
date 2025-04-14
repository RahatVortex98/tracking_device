# Tracking Device

A Django-based web application for real-time delivery tracking and fleet management. Customers can monitor their orders using a Google Maps-integrated portal, while fleet managers oversee vehicle locations and alerts through a dashboard. Built with Django, Bootstrap, and Google Maps API, this project demonstrates full-stack development and user-focused design.

## Features

- **Customer Portal**: Enter an order ID to view delivery status, ETA, destination, and live vehicle location on Google Maps.
- **Fleet Dashboard**: Displays vehicle locations, recent alerts (e.g., route deviations), and delivery statuses for logistics management.
- **Responsive Design**: Mobile-friendly UI powered by Bootstrap 5.
- **Real-World Use Case**: Solves logistics challenges like delayed deliveries and customer uncertainty.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: Bootstrap 5, Google Maps JavaScript API
- **Database**: SQLite (default, supports PostgreSQL)
- **Deployment**: Ready for Heroku or similar platforms

## Prerequisites

- Python 3.8+
- Django (`pip install django`)
- Google Maps API key ([Google Cloud Console](https://console.cloud.google.com/))

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RahatVortex98/tracking-device.git
   cd tracking-device
2.Install Dependencies:
pip install -r requirements.txt

3.Access the App:
Customer Portal: http://127.0.0.1:8000/track/?order_id=ORD123
Fleet Dashboard: http://127.0.0.1:8000/dashboard/

Customer Portal:

![interface](https://github.com/user-attachments/assets/2ea223a4-19e9-475d-b406-9c12acee1801)

Fleet Dashboard:

![dashborad interface](https://github.com/user-attachments/assets/28abf4c0-666c-4cd7-86f1-ae91bf64b599)



   
