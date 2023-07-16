from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class SiFiViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Science Fiction')
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Fantasy')
    serializer_class = BookSerializer


class MagicViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Magic')
    serializer_class = BookSerializer


class SuperheroViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Superheroes')
    serializer_class = BookSerializer


class ClassicsViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Classics')
    serializer_class = BookSerializer


class YoungAdultViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Young Adult')
    serializer_class = BookSerializer


class DystopiaViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Dystopia')
    serializer_class = BookSerializer


class HiFiViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Historical Fiction')
    serializer_class = BookSerializer


class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Mystery')
    serializer_class = BookSerializer


class EspionageViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Espionage')
    serializer_class = BookSerializer


class ContemporaryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Contemporary')
    serializer_class = BookSerializer
