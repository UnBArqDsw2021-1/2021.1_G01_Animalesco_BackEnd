from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from medicines.models import Medicine
from animals.models import Pet


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'id',
            'name',
            'start_date',
            'finish_date',
            'aplication_time',
        ]

    def create(self, validated_data):
        if not validated_data['next_application_date']:
            validated_data['is_finished'] = True
        return super().create(validated_data)

    def validate(self, data):
        start_date = data.get('start_date', None)
        finish_date = data.get('finish_date', None)

        if finish_date and (finish_date <= start_date):

            raise serializers.ValidationError({
                "finish_date": (
                    "A data do inicio da medicação não pode ser anterior à data atual ou da data de término."
                )
            })

        return data

    def unique_together_validation(self, data):
        """
        Função auxiliar para verificar se os dados passados no json são unique_together
        """
        view = self.context.get('view')
        url_pet_pk = view.kwargs.get('pet_pk')
        pet = get_object_or_404(Pet, pk=url_pet_pk)

        queryset = Medicine.objects.filter(
            name=data.get('name'),
            application_date=data.get('application_date'),
            pet=pet,
        )

        return queryset.count() == 0
