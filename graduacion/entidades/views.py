from django.shortcuts import render
from .models import *

from .forms import *

# Create your views here.
def home(request):
    return render(request, "entidades/index.html")


def maestrias(request):
    contexto = {"maestrias": Maestrias.objects.all() }
    return render(request, "entidades/maestrias.html", contexto)

def alumno(request):
    return render(request, "entidades/alumno.html")

def trabajodegrado(request):
    return render(request, "entidades/trabajodegrado.html")

def sustentacion(request):
    return render(request, "entidades/sustentacion.html")

#Formularios
def maestriasForm(request):
    if request.method == "POST":
        miForm = MaestriasForm(request.POST)
        if miForm.is_valid():
            maestria_nombre = miForm.cleaned_data.get("nombre")
            maestria_modalidad = miForm.cleaned_data.get("modalidad")
            maestrias = Maestrias(nombre = maestria_nombre, modalidad = maestria_modalidad)
            maestrias.save()
            contexto = {"maestrias": Maestrias.objects.all() }
            return render(request, "entidades/maestrias.html", contexto)
        pass
    else:
        miForm = MaestriasForm()

    return render(request, "entidades/maestriasForm.html", {"form": miForm})

#Buscar
def buscarMaestrias(request):
    return render(request, "entidades/buscar.html")

def encontrarMaestrias(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        maestrias = Maestrias.objects.filter(nombre__icontains=patron)
        contexto = {'maestrias': maestrias}
    else:
        contexto = {'maestrias': Maestrias.objects.all() }


    return render(request, "entidades/maestrias.html", contexto)