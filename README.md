# 📅 Community Event Management App

A mobile and web platform to **discover, create, and manage community events** with ease.  
Built using **React+Vite** for the frontend and **Django + PostgreSQL** for the backend.  

---

## 🚀 Features

### 👨‍💻 User Features
- **Discover Events** – Browse concerts, workshops, sports, and local meetups nearby.
- **Create Events** – Add title, description, date/time, location (Google Maps), and ticket limit.
- **Register & Get Tickets** – Generate unique **QR code tickets** for easy entry.
- **Real-time Chat** – Connect with participants before the event using WebSockets.
- **Event Reviews** – Share feedback after attending.
- **Search & Filter** – Find events by category, location, or date.

### 🖥️ Admin/Backend Features
- **Authentication** – Secure login/signup (JWT or session-based).
- **Event Management API** – CRUD operations for events.
- **Ticket System** – Unique QR codes for each participant.
- **Chat System** – Real-time messaging with Django Channels + Redis.
- **Geospatial Search** – Location-based event discovery.

---

## 🛠️ Tech Stack

### Frontend (React+Vite)
- Google Maps integration
- QR Code Generator
- WebSocket Client

### Backend (Django + PostgreSQL)
- Django REST Framework (API)
- Django Channels (Real-time features)
- PostgreSQL (with PostGIS for geolocation)
- Redis (for WebSocket communication)
- JWT Authentication

---

## 📂 Database Models

### User
- Default Django Auth User

### Event
- `title` (string)
- `description` (text)
- `host` (FK to User)
- `location` (geospatial field)
- `date_time` (datetime)
- `category` (string)
- `ticket_limit` (integer)

### Ticket
- `user` (FK to User)
- `event` (FK to Event)
- `qr_code` (string)
- `status` (enum: active/used)

### Message
- `user` (FK to User)
- `event` (FK to Event)
- `message_text` (text)
- `timestamp` (datetime)

---

## 📦 Installation

### Backend (Django)
```bash
# Clone repository
git clone https://github.com/Muflih-uk/Agora.git
cd Agora/backend

# Create virtual environment
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Migrate database
python manage.py migrate

# Run development server
python manage.py runserver
