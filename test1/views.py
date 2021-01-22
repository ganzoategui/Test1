from django.http import HttpResponse
from django.template import Context, Template
from django.template.loader import get_template
from django.shortcuts import render
import datetime

def Vista1(request):
    return HttpResponse("Bienvenidos......")

def categoriaEdad(reqest, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera Edad"
        else:
            categoria = "Adulto"
    else:
        if edad < 10:
            categoria = "Infancia"
        else:
            categoria = "Adolecente"
    resultado = "<h1> Categoria de la edad : %s </h1>" %categoria
    return HttpResponse(resultado)

def contenidoHTML(request, nombre, edad):
    contenido = """
    <html>
    <body>
    <p> Nombre : %s / Edad : %s </p>
    </body>
    </html>
    """ % (nombre, edad)
    return HttpResponse(contenido)


def mostrarTemplate(request):
    nombre = "Gustavo"
    apellido = "Anzoategui"
    Materias = ["Matematicas","Fisica", "Quimica", "Biologia"]
    #doc_externo = open("/Users/gustavoanzoategui/Development/test1/Templates/Template1.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo = loader.get_template('Template1.html')
    #ctx = Context({"nom_per":nombre, "ape_per":apellido, "temas":Materias})
    #documento = doc_externo.render({"nom_per":nombre, "ape_per":apellido, "temas":Materias})
    return render(request, 'Template1.html', {"nom_per":nombre, "ape_per":apellido, "temas":Materias})

def Pag_Paciente(request):
    fec_hoy = datetime.datetime.now()
    return render(request, "Paciente.html", {"fec_actual":fec_hoy})    

def Pag_Medico(request):
    return render(request, "Medico.html")