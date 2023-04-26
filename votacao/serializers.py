from rest_framework import serializers
from .models import Questao, Opcao
class QuestaoSerializer(serializers.ModelSerializer):
    class Meta: #(1)
        model = Questao
        fields = ('pk', 'questao_texto', 'pub_data')
class OpcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcao
        fields = ('pk', 'questao', 'opcao_texto', 'votos')