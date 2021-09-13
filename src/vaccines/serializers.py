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

        return data
