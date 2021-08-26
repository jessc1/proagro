from rest_framework import serializers
from isencao.models import Perda

class ProdutorListSerializer(serializers.ModelSerializer):
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
    

