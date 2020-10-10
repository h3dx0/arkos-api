from django.urls import path
from aplicaciones import  views
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'aplicaciones'

urlpatterns = [
    path('detalle/<int:pk>/', views.AplicacionDetalle.as_view(), name='aplicacion_detalle'),

]
urlpatterns = format_suffix_patterns(urlpatterns)