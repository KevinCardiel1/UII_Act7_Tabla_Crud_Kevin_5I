from django.contrib import admin
from .models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'empresa', 'telefono', 'email', 'direccion', 'fecha_registro') if hasattr(Proveedor, 'empresa') else ('id', 'nombre', 'telefono', 'email', 'direccion', 'fecha_registro')
    search_fields = ('nombre', 'email', 'telefono')
