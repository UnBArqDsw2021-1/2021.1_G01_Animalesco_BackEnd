from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from animals.models import Pet

from vet_visits.models import VetVisit
from vet_visits.permissions import VetVisitPetOwner
from vet_visits.serializers import VetVisitSerializer


class VetVisitViewSet(viewsets.ModelViewSet):
    queryset = VetVisit.objects.all()
    serializer_class = VetVisitSerializer
    doc_tags = ["Vet visits"]

    permission_classes = [ VetVisitPetOwner ]

    def get_queryset(self):
        pet = get_object_or_404(Pet, pk=self.kwargs["pet_pk"])
        return pet.vet_visits.all()

    def perform_create(self, serializer):
        pet = get_object_or_404(Pet, pk=self.kwargs["pet_pk"])
        serializer.save(pet=pet)
