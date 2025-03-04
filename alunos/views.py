from rest_framework.viewsets import ModelViewSet
from .models import Estado, Cidade, Aluno # Este . antes do lugar de onde importamos é para indicar que está na mesma pasta atual
from .serializers import EstadoSerializer, CidadeSerializer, AlunoSerializer

class EstadoViewSet(ModelViewSet): # ViewSets são classes que permitem executar um CRUD
    queryset = Estado.objects.all() # QuerySet significa um conjunto de busca em determinado modelo
    serializer_class = EstadoSerializer

class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer