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


**Notes**:
- Replace `yourusername` with your GitHub username.
- Add screenshots to a `screenshots/` folder (use tools like Snipping Tool).
- The acknowledgment credits xAI/Grok, as you requested.

---

### **Documentation**

**File**: `docs/documentation.md` (optional, or include in README)  
**Direction**: Save in `tracking_device/docs/documentation.md` or append to README.

```markdown
# Tracking Device Documentation

## Overview

The Tracking Device app enables logistics companies to track delivery vehicles and provide customers with real-time order updates. It features a customer portal and a fleet manager dashboard, built with Django, Bootstrap, and Google Maps.

## Architecture

- **Backend**:
  - **Framework**: Django (Python)
  - **Models**:
    - `Vehicle`: Stores vehicle details (ID, name).
    - `Delivery`: Tracks orders (ID, status, ETA, destination).
    - `Location`: Records vehicle coordinates and timestamps.
    - `Alert`: Logs issues like route deviations.
  - **Views**:
    - `track_delivery`: Handles customer order lookups.
    - `dashboard`: Displays fleet status for managers.
  - **Database**: SQLite (configurable for PostgreSQL).

- **Frontend**:
  - **Framework**: Bootstrap 5 for responsive UI.
  - **Templates**:
    - `base.html`: Shared layout with navbar.
    - `track_delivery.html`: Customer tracking UI.
    - `dashboard.html`: Fleet overview with map and alerts.
  - **Google Maps**: Displays vehicle locations.

## Usage Guide

### For Customers
1. Visit `/track/`.
2. Enter an order ID (e.g., “ORD123”).
3. View delivery details (status, ETA, map).

### For Fleet Managers
1. Access `/dashboard/`.
2. Monitor vehicle locations on the map.
3. Review alerts and delivery statuses.

### For Developers
- **Run Locally**: Follow README setup steps.
- **Extend Features**:
  - Add WebSockets for live updates:
    - Install `channels`: `pip install channels`.
    - Update `views.py` and templates.
  - Implement authentication:
    - Use Django’s `django.contrib.auth`.
    - Restrict dashboard access with `@login_required`.
- **Deploy**:
  - Use Heroku: `heroku create`, `git push heroku main`.
  - Set `DEBUG = False` in `settings.py`.
  - Configure PostgreSQL for production.

## Database Schema

- **Vehicle**:
  - `vehicle_id`: Char (unique)
  - `name`: Char
- **Delivery**:
  - `order_id`: Char (unique)
  - `vehicle`: ForeignKey(Vehicle)
  - `destination`: Char
  - `status`: Char (pending/en_route/delivered)
  - `eta`: DateTime
- **Location**:
  - `vehicle`: ForeignKey(Vehicle)
  - `latitude`: Float
  - `longitude`: Float
  - `timestamp`: DateTime
- **Alert**:
  - `vehicle`: ForeignKey(Vehicle)
  - `message`: Text
  - `severity`: Char (low/medium/high)
  - `timestamp`: DateTime

## Limitations

- Static location updates (no real-time polling).
- No user authentication (public access).
- SQLite-based, less scalable than PostgreSQL.

## Troubleshooting

- **Map Not Loading**: Verify Google Maps API key.
- **No Data**: Run test data script in README.
- **Template Errors**: Check `templates/` folder structure.

## Contributing

Feel free to fork, submit PRs, or report issues on GitHub.


   
