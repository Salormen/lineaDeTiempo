from django.contrib import admin
from documentos.models import DocumentoOficial, Etiqueta, Emisor
from documentos.admins.etiqueta import EtiquetaAdmin
from documentos.admins.emisor import EmisorAdmin
from documentos.admins.documentoOficial import DocumentoOficialAdmin

# Register your models here.


admin.site.register(DocumentoOficial, DocumentoOficialAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(Emisor, EmisorAdmin)


