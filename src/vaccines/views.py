from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from animals.models import Pet
from animals.permissions import IsPetOwner
from vaccines.models import Vaccine
from vaccines.serializers import VaccineSerializer


class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    doc_tags = ["Vaccines"]

    # Invés de verificar manualmente a permissão, em cada uma das controlers, criamos
    # uma classe que encapsula uma permissão e deixamos o Django realizar a checagem de
    # quem pode ou não pode acessar o recurso da url
    permission_classes = [ IsPetOwner ]

    def get_queryset(self):
        pet = get_object_or_404(Pet, pk=self.kwargs["pet_pk"])
        return pet.vaccines.all()

    def perform_create(self, serializer):
        pet = get_object_or_404(Pet, pk=self.kwargs["pet_pk"])
        serializer.save(pet=pet)
