from rest_framework import serializers

from animals.models import Breed, Pet, Specie


class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = [
            "id",
            "name",
        ]


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = [
            "id",
            "name",
        ]


class PetSerializer(serializers.ModelSerializer):

    breed_name = serializers.SerializerMethodField(method_name="get_breed_name")

    def get_breed_name(self, obj):
        """Helper function to return breed name instead of id"""
        return obj.breed.name

    specie_name = serializers.SerializerMethodField(method_name="get_specie_name")

    def get_specie_name(self, obj):
        """Helper function to return specie name"""
        return obj.breed.specie.name

    class Meta:
        model = Pet
        fields = [
            "id",
            "name",
            "sex",
            "breed",  # write only
            "birth_date",
            "is_neutered",
            "color",
            "breed_name",  # read only
            "specie_name",  # read only
        ]
        read_only_fields = (
            "breed_name",
            "specie_name",
        )
        extra_kwargs = {
            "breed": {"write_only": True},
        }

        # extra_kwargs é um atributo das ModelSerializers para sobrescrever as mensagens
        # padrões do django rest framework.
        extra_kwargs = {
            "sex": {
                "error_messages": {
                    # 'invalid_choice': "Please provide a valid sex:  ('M', 'F')",
                    "invalid_choice": f"Please provide a valid sex: {Pet.get_valid_sex_options()}",
                }
            },
            "breed": {
                "error_messages": {
                    "null": "Please provide a valid breed ID",
                }
            },
        }
