from django.contrib import admin
from .models import Estado, Cidade, Aluno

admin.site.register(Estado) # Após criar o app com Admin e fazer a model Estado, aqui relacionamos ambos para que possa ser acessível na interface
admin.site.register(Cidade)
admin.site.register(Aluno)