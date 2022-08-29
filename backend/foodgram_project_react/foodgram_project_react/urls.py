from re import template
from django.contrib import admin
from django.urls import path, include

import api.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
