from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.Resoluciones.Form import Formulario_Resolucion
from apps.Resoluciones.models import Resolucion
from django.views.generic import ListView,UpdateView
from django.urls import reverse_lazy

#Metodo para la impresion de datos en la tabla de resoluciones
class tabla_resolucion(ListView):
   model = Resolucion
   template_name = 'resolucion/tablaRE.html'


#Metodo para el ingreso de datos en el formulario resolucion
def vista_resolucion(request):
    if request.method == 'POST':
        form = Formulario_Resolucion(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Resoluciones:resolucion_vista')
    else:
        form = Formulario_Resolucion()
    
    return render (request, 'resolucion/formRE.html',{'form':form})  

#Clase para actualizar datos en resoluciones
class EditarResolucion(UpdateView):
    model = Resolucion
    form_class = Formulario_Resolucion
    template_name = 'resolucion/fromRE.html'
    succes_url = reverse_lazy('Resoluciones: resolucion_editar')