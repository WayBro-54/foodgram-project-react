from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserAccountViewset

router = DefaultRouter()
router.register('users', UserAccountViewset)

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
