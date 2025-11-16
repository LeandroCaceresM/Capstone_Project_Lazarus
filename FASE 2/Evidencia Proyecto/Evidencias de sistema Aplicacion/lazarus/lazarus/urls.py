"""
URL configuration for lazarus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.paginator),
    path('fail/', views.paginatorfail),
    path('introduccion/', views.introduccion, name='introduccion'),
    path('ingresar/', views.ingresar),
    path('crear/', views.paginator2),
    path('medico_vista/', views.medico_vista),
    path('recuperar_contraseña/', views.recuperar_contraseña, name='recuperar_contraseña'),
    path('mostrarCambioPassword/', views.mostrarCambioPassword, name='mostrarCambioPassword'),
    path('HacercambiarPassword/', views.HacercambiarPassword, name='HacercambiarPassword'), 
    path('usercreate/', views.usercreate),
    path('oficial/', views.oficial),
    path('phq9/', views.phq9, name='phq9'),
    path('phq9_enviar/', views.phq9_enviar, name='phq9_enviar'),
    path('gad7/', views.gad7, name='gad7'),
    path('gad7_enviar/', views.gad7_enviar, name='gad7_enviar'),
    path('Test_reconocimiento', views.Test_reconocimiento, name='Test_reconocimiento'),
    path('TestRecco_enviar/', views.TestRecco_enviar, name='TestRecco_enviar'),


    path('super_test/', views.super_test, name='super_test'),
    path('situacion_familiar_enviar/', views.situacion_familiar_enviar, name='situacion_familiar_enviar'),
    path('super_test_1/', views.super_test_1, name='super_test_1'),



    path('super_test_2/', views.super_test_2, name='super_test_2'),
    path('salud_fisica_enviar/', views.salud_fisica_enviar, name='salud_fisica_enviar'),

    path('super_test_3/', views.super_test_3, name='super_test_3'),
    path('salud_mental_enviar/', views.salud_mental_enviar, name='salud_mental_enviar'),

    path('super_test_4/', views.super_test_4, name='super_test_4'),
    path('vida_academica_enviar/', views.vida_academica_enviar, name='vida_academica_enviar'),
    
    path('super_test_5/', views.super_test_5, name='super_test_5'),
    path('estilo_vida_enviar/', views.estilo_vida_enviar, name='estilo_vida_enviar'),

    path('super_test_6/', views.super_test_6, name='super_test_6'),
    path('seguridad_autoestima_enviar/', views.seguridad_autoestima_enviar, name='seguridad_autoestima_enviar'),











    path('logout_view/', views.logout_view,),
    path('ver_test/', views.ver_test, name='ver_test'),
    path('ver_perfil/', views.ver_perfil, name='ver_perfil')
]




#lo que esta marcado como comentario son vistas con funcionas no hechas correctamente