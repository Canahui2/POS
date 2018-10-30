from django import forms
from apps.Resoluciones.models import Resolucion

class Formulario_Resolucion(forms.ModelForm):

    class Meta:
        model = Resolucion

        fields = [
            'NumeroResolucion',
            'FechaDeAutorizacion', 
            'Serie', 
            'NumeroInicial',
            'NumeroFinal',
            'TipoDeDocumento', 
            'Operador',
        ]

        labels = {
            'NumeroResolucion': 'Numero de Resolucion',
            'FechaDeAutorizacion': 'Fecha de autorizacion',
            'Serie': 'Serie del documento',
            'NumeroInicial': 'Numero inicial',
            'NumeroFinal': 'Numero final',
            'TipoDeDocumento': 'Tipo de documento',
            'Operador': 'Empleado'
        }

        widgets ={
            'NumeroResolucion' : forms.TextInput(attrs={'class':'form-control'}),
            'FechaDeAutorizacion': forms.TextInput(attrs={'class':'form-control'}), 
            'Serie': forms.TextInput(attrs={'class':'form-control'}),
            'NumeroInicial': forms.TextInput(attrs={'class':'form-control'}),
            'NumeroFinal': forms.TextInput(attrs={'class':'form-control'}),
            'TipoDeDocumento': forms.TextInput(attrs={'class':'form-control'}),
            'Operador': forms.Select(attrs={'class':'form-control'}),
        }