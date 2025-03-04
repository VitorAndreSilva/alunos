from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from alunos.views import EstadoViewSet, CidadeViewSet, AlunoViewSet

router = DefaultRouter() # Roteador padrão, gerando as urls necessárias para uma ViewSet
router.register(r'estados', EstadoViewSet) # Registra EstadoViewSet no roteador para criar endpoint onde executar o CRUD
router.register(r'cidade', CidadeViewSet)
router.register(r'aluno', AlunoViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('admin/', admin.site.urls),
]