from rest_framework import serializers
from animals.models import Specie


class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = ['id', 'name',]
