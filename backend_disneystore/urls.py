from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_proveedores.urls')),  # 👈 conecta con las rutas de tu app
]
