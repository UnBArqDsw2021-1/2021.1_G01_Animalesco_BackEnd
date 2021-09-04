from django.db.models import fields
from rest_framework import serializers

from animals.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'birth_date', 'weight_kg', 'tricks']
