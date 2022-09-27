from django.db import models
from .usuario import Usuario
from .Paciente import paciente

class Familiar(models.Model):
    id_familiar=models.AutoField(primary_key=True)
    username=models.ForeignKey(Usuario, related_name='familiar',on_delete=models.CASCADE)
    id_paciente=models.ForeignKey(paciente, related_name='familiar',on_delete=models.CASCADE)
    Parentesco=models.CharField('parentesco',max_length=35)
    correo=models.CharField('correo',max_length=35)