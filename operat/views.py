from django.http.response import HttpResponseRedirect
from operat.forms import RobotaForm
from operat.models import Robota
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Robota
from .forms import RobotaForm

# strona główna lista robót
def index(request):
    listaRobot = Robota.objects.order_by('data_operat')[:5]
    context={
        "listaRobot": listaRobot,
    }
    return render(request, 'operat/index.html', context)

# zestawienie robót
def zestawienie(request):
    listaRobot = Robota.objects.order_by('data_operat')[:10]
    context={
        "listaRobot": listaRobot,
    }
    return render(request, 'operat/zestawienie.html', context)

# szczegóły pracy
def szczegoly(request, idpracy):
    idPracy=get_object_or_404(Robota, pk=idpracy)
    return render(request, 'operat/szczegoly.html', {"Robota":idPracy})

#dokumentacja - wybór dokumentu do edycji i generowania
def dokumentacja(request, idpracy):
    idPracy=get_object_or_404(Robota, pk=idpracy)
    return render(request, 'operat/generowanie.html', {"Robota":idPracy})

#dokumentacja - edycja
def edycja(request, idpracy):
    idPracy=get_object_or_404(Robota, pk=idpracy)
    robotaForm=RobotaForm()
    return render(request, 'operat/edycja.html', {
        "Robota":idPracy,
        "form":robotaForm,
    })

#dokumentacja - wprowadzenie nowej pracy
def nowa(request):
    #robota_obiekt=get_object_or_404(Robota)
    if request.method == 'POST':
        robotaForm=RobotaForm(request.POST)
        if robotaForm.is_valid():
            robotaForm.save()
            return redirect('zestawienie')
    else:
        robotaForm=RobotaForm()
    return render(request, 'operat/nowa.html', {
        "form":robotaForm,
          })


# generowanie dokumentacji
def generowanie(request):
    listaRobot = Robota.objects.order_by('data_operat')[:10]
    context={
        "listaRobot": listaRobot,
    }
    return render(request, 'operat/generowanie.html', context)