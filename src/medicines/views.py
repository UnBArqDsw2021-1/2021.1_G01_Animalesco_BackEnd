from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from animals.models import Pet
from animals.permissions import IsPetOwner

from medicines.models import Medicine
from medicines.serializers import MedicineSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    doc_tags = ["Medicines"]

    permission_classes = [ IsPetOwner ]

    def get_queryset(self):
        pet = get_object_or_404(Pet, pk=self.kwargs["pet_pk"])
        return pet.medicines.all()

    def perform_create(self, serializer):
        pet = get_object_or_404(Pet, pk=self.kwargs["pet_pk"])
        serializer.save(pet=pet)
