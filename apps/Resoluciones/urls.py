from django.conf.urls import url,include
from apps.Resoluciones.views import vista_resolucion, tabla_resolucion,EditarResolucion

app_name= 'Resoluciones'

urlpatterns = [
    url(r'^nuevo$', vista_resolucion, name= 'resolucion_vista'),
    url(r'^tabla$', tabla_resolucion.as_view(), name= 'tabla_resolucion'),
    url(r'^editar/(?P<pk>\d+)/$', EditarResolucion.as_view(), name='resolucion_editar')
]