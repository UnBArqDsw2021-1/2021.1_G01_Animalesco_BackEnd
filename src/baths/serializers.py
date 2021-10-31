from rest_framework import serializers

from animals.models import Pet
from baths.models import Bath


class BathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bath
        fields = [
            "id",
            "bath_date",
            "next_bath_date",
            "location_bath",
        ]

    def validate(self, data):
        bath_date = data.get("bath_date", None)
        next_bath_date = data.get("next_bath_date", None)

        if next_bath_date <= bath_date:

            raise serializers.ValidationError(
                {
                    "next_bath_date": (
                        "A data do próximo banho não pode ser anterior à data atual."
                    )
                }
            )

        return data
