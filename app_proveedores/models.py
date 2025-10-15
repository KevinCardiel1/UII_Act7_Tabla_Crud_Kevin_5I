from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.CharField(max_length=150)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
