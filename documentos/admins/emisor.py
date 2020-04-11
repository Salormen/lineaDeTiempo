'''
Created on 08/04/2020

@author: juancho-r
'''
from django.contrib import admin

class EmisorAdmin(admin.ModelAdmin):
    
    # Lista de elementos
    
    #define que mostrar la lista de elementos
    list_display = ['nombre']
    #define que campos pueden ser editados en la lista de elementos
    list_editable = []
    #define que campos se van a usar para buscar elementos
    search_fields = ['nombre']
    #define que campos pueden ser usados para filtros
    list_filter = []
    #define cuantos elementos se muestran por pagina
    list_per_page = 100
    
    pass
