from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from proyectos import  views
app_name = 'proyectos'

urlpatterns = [
    path('detalle/<int:pk>/', views.ProyectoDetalle.as_view(), name='proyecto_detalle'),

]
urlpatterns = format_suffix_patterns(urlpatterns)