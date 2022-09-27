from django.contrib import admin
from .models.usuario import Usuario
from .models.Psalud import Personal_salud
from .models.Paciente import paciente
from .models.familiar import Familiar

admin.site.register(Usuario)
admin.site.register(Personal_salud)
admin.site.register(paciente)
admin.site.register(Familiar)