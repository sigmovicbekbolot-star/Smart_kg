from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhoneViewSet

router = DefaultRouter()
router.register(r'phones', PhoneViewSet)  # 'phones' REST API path

urlpatterns = [
    path('', include(router.urls)),
]
