from rest_framework import serializers

from medicines.models import Medicine


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            "id",
            "name",
            "start_date",
            "finish_date",
            "aplication_time",
        ]

    def validate(self, attrs):
        start_date = attrs.get("start_date", None)
        finish_date = attrs.get("finish_date", None)

        if finish_date and (finish_date <= start_date):

            raise serializers.ValidationError(
                {
                    "finish_date": ((
                        "A data do inicio da medicação não pode ser anterior à "
                        "data atual ou da data de término."
                    ))
                }
            )

        return attrs
