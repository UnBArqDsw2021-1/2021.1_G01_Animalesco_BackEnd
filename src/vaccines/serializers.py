from rest_framework import serializers

from vaccines.models import Vaccine

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = [
            'id',
            'name',
            'application_date',
            'next_application_date',
            'is_finished',
            # 'pet'
        ]