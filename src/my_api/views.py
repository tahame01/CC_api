from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CharacterSerializer

# Create your views here.
class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('name')
    serializer_class = CharacterSerializer