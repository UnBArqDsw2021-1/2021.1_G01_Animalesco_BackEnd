from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import authentication
from animals.serializers import SpecieSerializer
from animals.models import Specie


class SpecieViewSet(viewsets.ModelViewSet):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer

