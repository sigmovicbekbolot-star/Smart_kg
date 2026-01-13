from rest_framework.viewsets import ModelViewSet
from .models import Phone
from .serializers import PhoneSerializer

class PhoneViewSet(ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer