from django.db import models

class Estado(models.Model): # Criamos a classe "Estado", que herda de models (importado) .Model, para que o Django a reconheça como Model e disponibilize as ferramentas necessárias
    nome = models.CharField(max_length=20) # Campo string de nome do estado com máximo de 20 caracteres
    sigla = models.CharField(max_length=2) # Campo string de UF do estado com máximo de 2 caracteres
    def __str__(self): # Método de __str__ retornará o nome do estado no Django Admin
        #return self.nome
        return f'{self.nome} ({self.sigla})'
    
class Cidade(models.Model):
    nome = models.CharField(max_length=58)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT) # a model estado é do tipo ForeignKey, para relacionar a cidade ao estado; se excluirmos esta variável, a cidade não será perdida por causa do on_delete
    def __str__(self):
        #return self.nome
        return f'{self.nome} - {self.estado}'
    
class Aluno(models.Model):
    nome = models.CharField(max_length=895)
    nascimento = models.DateField() # O tipo desta model é um campo de data
    email = models.EmailField() # O tipo desta model é um campo de email
    telefone = models.CharField(max_length=15)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome} ({self.cidade} - {self.cidade.estado}) - {self.email}'