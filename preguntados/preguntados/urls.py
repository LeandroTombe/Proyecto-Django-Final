"""preguntados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('login/',views.loginPage, name='login'),
    path('registro/', views.pagina_registro, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('inicio_juego/', views.inicio_juego, name='inicio_juego'),
    path('estadisticas/', views.Usuario, name='estadisticas'),
    path('juego/', views.Juego, name='juego'),
    path('actualizar_usuario//<str:pk>/', views.Actualizar_Usuario, name='actualizar_usuario'),
    path('account/', views.Perfil_usuario, name="Perfil_usuario"),
    path('delete/<str:pk>/', views.deleteUser, name='delete_user'),
    path('tablero/', views.tablero, name='tablero'),
	path('jugar/', views.jugar, name='jugar'),
	path('resultado/<int:pregunta_respondida_pk>/', views.resultado_pregunta, name='resultado'),
    path('inicio_juego/', views.inicio_juego, name='inicio_juego'),
    path('crear_preguntas/', views.crear_pregunta, name='crear_preguntas'),
    path('crear_respuesta/',views.crear_respuesta, name='crear_respuesta'),
    path('volver_jugar/', views.volver_jugar, name='volver_jugar'),
]
