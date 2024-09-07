from django.db import models
from django.utils import timezone

# Create your models here.
class Sexo(models.Model):
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
        
class Acesso(models.Model):
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
    
class Dialise(models.Model):
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100,  null=True, blank=True)
    data_nascimento = models.DateField()
    sexo = models.ForeignKey(Sexo, on_delete=models.DO_NOTHING)
    contato = models.CharField(max_length=20)
    responsavel = models.CharField(max_length=100, null=True, blank=True)
    diagnostico_principal = models.CharField(max_length=200)
    comorbidades = models.TextField()
    data_inicio_dialise = models.DateField()
    tipo_dialise = models.ForeignKey(Dialise, on_delete=models.DO_NOTHING)
    tipo_acesso = models.ForeignKey(Acesso, on_delete=models.DO_NOTHING)
    medicamentos = models.TextField()
    alergias = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d')
    
    def __str__(self):
        return self.nome
    
