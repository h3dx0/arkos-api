"""arkos_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from rest_framework import routers
from contacto.views import ContactoViewSet
from recursos.views import RecursosViewSet
from quienes_somos.views import QuienesSomosViewSet
from proyectos.views import ProyectoViewSet

router = routers.DefaultRouter()
router.register(r'contacto', ContactoViewSet)
router.register(r'recursos', RecursosViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'quienes-somos', QuienesSomosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/inicio/', include('inicio.urls', namespace='inicio')),
    # path('api/quienes-somos/', include('quienes_somos.urls', namespace='quienes_somos')),
    # path('api/sistema-arkos/', include('sistema_arkos.urls', namespace='sistema_arkos')),
    # path('api/contacto/', include('contacto.urls', namespace='contacto')),
    # path('api/proyectos/', include('proyectos.urls', namespace='proyectos')),
    # path('api/recursos/', include('recursos.urls', namespace='recursos')),
    # path('api/aplicaciones/', include('aplicaciones.urls', namespace='aplicaciones')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)