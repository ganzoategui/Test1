"""test1 URL Configuration

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
from test1.views import Vista1, categoriaEdad, contenidoHTML, mostrarTemplate, Pag_Paciente, Pag_Medico

#from Ejemplo1.views import Bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Vista1/', Vista1),
    path('CategoriaEdad/<int:edad>', categoriaEdad),
    path('Contenido/<nombre>/<int:edad>', contenidoHTML),
    path('Template/', mostrarTemplate),
    path('Paciente/', Pag_Paciente),
    path('Medico/', Pag_Medico),
    #path('Welcome/', Bienvenida),
]
