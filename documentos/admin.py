from django.contrib import admin
from documentos.models import Hito, Etiqueta, Emisor
from documentos.admins.hito import HitoAdmin
from documentos.admins.etiqueta import EtiquetaAdmin
from documentos.admins.emisor import EmisorAdmin

# Register your models here.


admin.site.register(Hito, HitoAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(Emisor, EmisorAdmin)


