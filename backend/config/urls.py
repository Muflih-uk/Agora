
from django.contrib import admin
from django.urls import path, include

url_patterns = [
    path('admin/', admin.site.urls),

    path('api/', include('users.urls')),
    path('api/', include('events.urls'))
]
