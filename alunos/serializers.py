from rest_framework.serializers import ModelSerializer
from .models import Estado, Cidade, Aluno

class EstadoSerializer(ModelSerializer): # Serializer é o responsável por transformar um objeto em um JSON
    class Meta: # Recebe metadados, ou seja, configurações sobre a classe principal
        model = Estado
        fields = '__all__'  # O faz em todos os campos possíveis dentro da model

class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'