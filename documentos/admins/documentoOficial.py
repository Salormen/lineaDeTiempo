'''
Created on 08/04/2020

@author: juancho-r
'''
from django.contrib import admin
from django.http import HttpResponse


class DocumentoOficialAdmin(admin.ModelAdmin):
    
    # Lista de elementos
    
    #define que mostrar la lista de elementos
    list_display = ['tema', 'fecha', 'tipo_de_publicacion', 'emisor']
    #define que campos pueden ser editados en la lista de elementos
    list_editable = []
    #define que campos se van a usar para buscar elementos
    search_fields = ['tema', 'fecha', 'tipo_de_publicacion', 'emisor']
    #define que campos pueden ser usados para filtros
    list_filter = ['fecha', 'tipo_de_publicacion', 'emisor']
    #define las acciones
    actions = ['descargar_archivos_seleccionados']
    #define cuantos elementos se muestran por pagina
    list_per_page = 100
    
    
    def descargar_archivos_seleccionados(self, request, documentos):
        for doc in documentos:
            extension = str(doc.archivo).split(".")[1]
            response = HttpResponse(doc.archivo, content_type='application/'+extension+'')
            print(doc.archivo)
            response['Content-Disposition'] = 'attachment; filename="'+str(doc.archivo).split("/")[1]+'"'
            return response
    
    pass
