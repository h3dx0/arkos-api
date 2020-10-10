from django.contrib import admin

# Register your models here.
from sistema_arkos.models import BeneficiosSistema, SistemaArkos

admin.site.register(BeneficiosSistema)
admin.site.register(SistemaArkos)