from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from animals.models import Pet
from animals.permissions import IsRelatedPetOwner
from baths.models import Bath
from baths.serializers import BathSerializer


class BathViewSet(viewsets.ModelViewSet):
    queryset = Bath.objects.all()
    serializer_class = BathSerializer
    doc_tags = ["baths"]

    permission_classes = [IsRelatedPetOwner]

    def get_queryset(self):
        pet = get_object_or_404(Pet, pk=self.kwargs["pet_pk"])
        return pet.baths.all()

    def perform_create(self, serializer):
        pet = get_object_or_404(Pet, pk=self.kwargs["pet_pk"])
        serializer.save(pet=pet)
