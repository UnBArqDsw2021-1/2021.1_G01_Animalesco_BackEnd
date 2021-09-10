from rest_framework import serializers, viewsets

from vaccines.models import Vaccine
from vaccines.serializers import VaccineSerializer
from animals.models import Pet

class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializers = VaccineSerializer
    doc_tags = ["Vaccines"]