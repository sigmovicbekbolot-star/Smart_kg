from django.shortcuts import render

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer


class BookVeiwSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer