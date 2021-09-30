from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    if request.method=='POST':
        nombre = request.POST.get('nombre')
        apellido=request.POST.get('apellido')
        telefono=request.POST.get('telefono')



        print(nombre + ' ' + apellido + ' ' + telefono)

        model_cliente = cliente(nombre=nombre,
                                  apellido=apellido,
                                  telefono=telefono)



        model_cliente.save()
        return redirect('Storage:index')

    elif request.method == 'GET':
        return render(request, 'index.html')