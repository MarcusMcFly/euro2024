"""
URL configuration for mi_proyecto_futbol project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# urls.py
from django.contrib import admin
from django.conf import settings
from django.urls import path  # Importa la función path
from futboledos import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Página de inicio
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('equipos/<int:equipo_id>/', views.detalle_equipo, name='detalle_equipo'),
    path('partidos/', views.lista_partidos, name='lista_partidos'),
    path('partidos/<int:partido_id>/', views.detalle_partido, name='detalle_partido'),
    path('partidos/<int:partido_id>/apuesta/', views.realizar_apuesta, name='realizar_apuesta'),
    path('apuestas/', views.lista_apuestas, name='lista_apuestas'),
    path('apuestas/<int:apuesta_id>/', views.detalle_apuesta, name='detalle_apuesta'),
    path('apuestas/<int:apuesta_id>/editar/', views.editar_apuesta, name='editar_apuesta'),
    path('apuestas/<int:apuesta_id>/borrar/', views.borrar_apuesta, name='borrar_apuesta'),
    path('resultados/', views.lista_resultados, name='lista_resultados'),
    path('resultados/<int:resultado_id>/', views.detalle_resultado, name='detalle_resultado'),
    path('resultados/<int:resultado_id>/editar/', views.editar_resultado, name='editar_resultado'),
    path('resultados/<int:resultado_id>/borrar/', views.borrar_resultado, name='borrar_resultado'),
    path('fase-de-grupos/', views.fase_de_grupos, name='fase_de_grupos'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

