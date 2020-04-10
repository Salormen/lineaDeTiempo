from django.contrib import admin
from linea.models import Hito, Etiqueta
from linea.admins.hito import HitoAdmin
from linea.admins.etiqueta import EtiquetaAdmin

# Register your models here.


admin.site.register(Hito, HitoAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)
