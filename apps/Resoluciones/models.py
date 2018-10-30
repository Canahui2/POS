from django.db import models

# Creo mis modelos que representan una tabla de mi base de datos
class Operador(models.Model):
    Nombre = models.CharField(max_length=10)
    Apellido = models.CharField(max_length=10)
    Rol = models.CharField(max_length=20)

    def __str__(self):
        return '{} {}'.format(self.Nombre,self.Apellido)



class Resolucion(models.Model):
     NumeroResolucion = models.CharField(max_length=20, primary_key=True)
     FechaDeAutorizacion = models.DateField()
     Serie = models.CharField(max_length=2)
     NumeroInicial = models.IntegerField()
     NumeroFinal = models.IntegerField()
     TipoDeDocumento = models.CharField(max_length=15)
     Operador = models.ForeignKey(Operador, null =True, blank=True, on_delete = models.CASCADE)






