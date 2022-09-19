from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppQatar.models import Seleccion, Estadio, Copas
from AppQatar.forms import SelForm, EstForm, CopForm

# Create your views here.
"""""
def seleccion(request):

      seleccion =  Seleccion(pais="Desarrollo web", continente="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)
"""""

def inicio(request):

      return render(request, "AppQatar/inicio.html")

"""""

def estadio(request):

      return render(request, "AppQatar/estadio.html")


def copas(request):

      return render(request, "AppQatar/copas.html")
"""

def seleccion(request):

      if request.method == 'POST':

            miForm = SelForm(request.POST) #aquí mellega toda la información del html

            print(miForm)

            if miForm.is_valid:   #Si pasó la validación de Django

                  informacion = miForm.cleaned_data

                  seleccion = Seleccion (pais=informacion['pais'], continente=informacion['continente']) 

                  seleccion.save()

                  return render(request, "AppQatar/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miForm = SelForm() #Formulario vacio para construir el html

      return render(request, "AppQatar/seleccion.html", {"miForm":miForm})
      

def estadio(request):

      if request.method == 'POST':

            miForm = EstForm(request.POST) #aquí mellega toda la información del html

            print(miForm)

            if miForm.is_valid:   #Si pasó la validación de Django

                  informacion = miForm.cleaned_data

                  estadio = Estadio (nombre=informacion['nombre'], ciudad=informacion['ciudad']) 

                  estadio.save()

                  return render(request, "AppQatar/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miForm = EstForm() #Formulario vacio para construir el html

      return render(request, "AppQatar/estadio.html", {"miForm":miForm})


def copas(request):

      if request.method == 'POST':

            miForm = CopForm(request.POST) #aquí mellega toda la información del html

            print(miForm)

            if miForm.is_valid:   #Si pasó la validación de Django

                  informacion = miForm.cleaned_data

                  copas = Copas(selecc=informacion['selecc'], cantCopas=informacion['cantCopas'], ultimaCopa=informacion['ultimaCopa']) 

                  copas.save()

                  return render(request, "AppQatar/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miForm = CopForm() #Formulario vacio para construir el html

      return render(request, "AppQatar/copas.html", {"miForm":miForm})


def buscar(request):

      if  request.GET["selecc"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            selecc = request.GET['selecc'] 
            copas = Copas.objects.filter(selecc__icontains=selecc)
            
            return render(request, "AppQatar/inicio.html", {"selecc":selecc, "copas":copas})

      else: 

	      respuesta = "No enviaste datos"

      return HttpResponse(respuesta)