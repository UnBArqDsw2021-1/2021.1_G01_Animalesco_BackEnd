from rest_framework import serializers, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError

from vaccines.models import Vaccine
from vaccines.serializers import VaccineSerializer
from animals.models import Pet

class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    doc_tags = ["Vaccines"]

    def get_queryset(self):
        pet = get_object_or_404(Pet, pk=self.kwargs["pet_pk"])
        user = self.request.user
        if (pet.owner == user):
            queryset = pet.vaccines.all()
            return queryset
        else:
            raise ValidationError("Este animal não é seu.")


    def perform_create(self, serializer):
        pet = get_object_or_404(Pet, pk=self.kwargs["pet_pk"])
        serializer.save(pet=pet)

    