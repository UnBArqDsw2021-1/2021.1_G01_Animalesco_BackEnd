from rest_framework import viewsets

from animals.models import Animal
from animals.serializers import AnimalSerializer


# CRUD
class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer

    def get_queryset(self):
        return Animal.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        owner = self.request.user
        serializer.save(owner=owner)
