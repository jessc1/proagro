from rest_framework import serializers
from ..models import Perda


class ProdutorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perda
        fields = [
            'id',
            'produtor_nome',
            'produtor_email',
            'produtor_cpf',
            'produtor_data_colheita',
            'evento',
            'lavoura',
    ]

class ProdutorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perda
        fields = [
            'id',
            'produtor_nome',
            'produtor_email',
            'produtor_cpf',
            'produtor_data_colheita',
            'evento',
            'lavoura',
    ]
    

