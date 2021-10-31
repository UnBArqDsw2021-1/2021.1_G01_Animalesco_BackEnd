from rest_framework import serializers

from vet_visits.models import VetVisit


class VetVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = VetVisit
        fields = ["id", "vet_clinic", "description", "visit_date", "next_visit_date"]

    def validate(self, attrs):
        visit_date = attrs.get("visit_date", None)
        next_visit_date = attrs.get("next_visit_date", None)

        if next_visit_date and (next_visit_date <= visit_date):
            raise serializers.ValidationError(
                {
                    "next_visit_date": (
                        "A data da próxima visita não pode ser igual ou anterior à "
                        + "data de visita ao veterinário."
                    )
                }
            )

        return attrs
