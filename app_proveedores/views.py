from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor

def index(request):
    proveedores = Proveedor.objects.all().order_by('-fecha_registro')
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        Proveedor.objects.create(
            nombre=nombre,
            telefono=telefono,
            email=email,
            direccion=direccion
        )
        return redirect('inicio')
    return render(request, 'agregar_proveedor.html')

def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.save()
        return redirect('inicio')
    return render(request, 'editar_proveedor.html', {'proveedor': proveedor})

def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('inicio')
    return render(request, 'borrar_proveedor.html', {'proveedor': proveedor})
