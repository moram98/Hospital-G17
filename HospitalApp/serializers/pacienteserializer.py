from HospitalApp.models.Paciente import paciente
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=paciente
        fields=('id_Psalud','username','direccion','ciudad',' Fecha_nacimiento')