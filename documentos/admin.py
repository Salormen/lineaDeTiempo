from django.contrib import admin
from documentos.models import Hito, Etiqueta
from documentos.admins.hito import HitoAdmin
from documentos.admins.etiqueta import EtiquetaAdmin

# Register your models here.


admin.site.register(Hito, HitoAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)