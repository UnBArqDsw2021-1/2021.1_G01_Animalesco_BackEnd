
from rest_framework import serializers

from animals.models import Pet, Breed, Specie


class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = [ 'id', 'name', ]


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = [ 'id', 'name', ]


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            'id',
            'name',
            'sex',
            'breed',
            'birth_date',
            'is_neutered',
            'color',
        ]

        # extra_kwargs é um atributo das ModelSerializers para sobrescrever as mensagens
        # padrões do django rest framework.
        extra_kwargs = {
            'sex': {
                'error_messages': {
                    # 'invalid_choice': "Please provide a valid sex:  ('M', 'F')",
                    'invalid_choice': f"Please provide a valid sex: {Pet.get_valid_sex_options()}",
                }
            },
            'breed': {
                'error_messages': {
                    'null': "Please provide a valid breed ID",
                }
            },
        }
