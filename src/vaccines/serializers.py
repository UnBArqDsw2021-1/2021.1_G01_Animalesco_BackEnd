from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from vaccines.models import Vaccine
from animals.models import Pet


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = [
            'id',
            'name',
            'application_date',
            'next_application_date',
            'is_finished',
        ]

    # Essa função é responsável por fazer o controle da finalização da
    # vacina a partir da informação, ou falta de, da data da próxima dose
    def create(self, validated_data):
        if not validated_data['next_application_date']:
            validated_data['is_finished'] = True
        return super().create(validated_data)

    # Essa função é responsável por fazer a validação das datas de aplicação
    # das doses de vacinas, uma vacina não pode ter a próxima dose marcada para o mesmo
    # dia ou dias anteriores a primeira dose
    def validate(self, data):
        application_date = data.get('application_date', None)
        next_application_date = data.get('next_application_date', None)

        if next_application_date and (next_application_date <= application_date):

            # O padrão rest para comunicar erros, é a chave ser o campo que gerou erros,
            # e o valor o erro em si.
            raise serializers.ValidationError({
                "next_application_date": (
                    "A data da próxima dose não pode ser igual ou anterior à data " +
                    "de aplicação atual da aplicação."
                )
            })

        if self.unique_together_validation(data) == False:
            raise serializers.ValidationError({
                "unique_together_validation": (
                    "Duplicate vaccination detected! It is not allowed to register the "
                    "same vaccine, in the same pet, on the same day, twice."
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

        queryset = Vaccine.objects.filter(
            name=data.get('name'),
            application_date=data.get('application_date'),
            pet=pet,
        )

        return queryset.count() == 0
