from django.db.models.fields.related import ForeignKey
from django.http.response import HttpResponseRedirect
from operat.models import Robota
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .models import DaneObsOsnPom, MapaPorownania, Robota, Sprawozdanie, WykazWspOsn, WykazWspPom
from .forms import DaneObsOsnPomForm, MapaPorownaniaForm, RobotaForm, SprawozdanieForm, WykazWspOsnForm, WykazWspPomForm

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
    robota=get_object_or_404(Robota, pk=idpracy)
    return render(request, 'operat/szczegoly.html', {"Robota":robota, })

#dokumentacja - wybór dokumentu do edycji i generowania
def dokumentacja(request, idpracy):
    robota=get_object_or_404(Robota, pk=idpracy)
    return render(request, 'operat/generowanie.html', {"Robota":robota})

#dokumentacja - edycja danych dotyczących roboty
def edycja(request, idpracy):
    listaRobot = Robota.objects.order_by('data_operat')[:10]
    idPracy=get_object_or_404(Robota, pk=idpracy)
    if request.method == 'POST':
        robotaForm=RobotaForm(request.POST, instance=idPracy)
        if robotaForm.is_valid():
            robotaForm.save()
            messages.success(request, 'Dane dotyczące roboty zostały zaktualizowane')
            return render(request, 'operat/zestawienie.html', {
                "listaRobot": listaRobot
            })
    else:
        robotaForm=RobotaForm(instance=idPracy)
    return render(request, 'operat/edycja.html', {
        "Robota":idPracy,
        "form":robotaForm,
    })
# edycja danych dotyczących sprawozdania
def edycjaSprawozdanie(request, idpracy):
    listaRobot = Robota.objects.order_by('data_operat')[:10]
    robota=get_object_or_404(Robota, pk=idpracy)
    try:
        spr=robota.sprawozdanie
    except:
        spr=Sprawozdanie()
        spr.save()
    if request.method == 'POST':
        sprawozdanieForm=SprawozdanieForm(request.POST, instance=spr)
        if sprawozdanieForm.is_valid():
            sprawozdanieForm.save()
            messages.success(request, 'Dane dotyczące Sprawozdania zostały zaktualizowane')
            return render(request, 'operat/zestawienie.html', {
                "listaRobot": listaRobot
            })
    else:
        sprawozdanieForm=SprawozdanieForm(instance=spr)
    return render(request, 'operat/edycjaspr.html', {
        "Robota":robota,
        "form":sprawozdanieForm,
    })
# edycja danych dotyczących MPzT
def edycjaMpzt(request, idpracy):
    listaRobot = Robota.objects.order_by('data_operat')[:10]
    robota=get_object_or_404(Robota, pk=idpracy)
    try:
        mpzt=robota.mapaporownania
    except:
        mpzt=MapaPorownania()
        mpzt.save()
    if request.method == 'POST':
        mpztForm=MapaPorownaniaForm(request.POST, instance=mpzt)
        if mpztForm.is_valid():
            mpztForm.save()
            messages.success(request, 'Dane dotyczące Mapy porównania zostały zaktualizowane')
            return render(request, 'operat/zestawienie.html', {
                "listaRobot": listaRobot
            })
    else:
        mpztForm=MapaPorownaniaForm(instance=mpzt)
    return render(request, 'operat/edycjaspr.html', {
        "Robota":robota,
        "form":mpztForm,
    })    
# edycja danych dotyczących Danych obserwacyjnych osnowy pomiarowej
def edycjaDaneObs(request, idpracy):
    listaRobot = Robota.objects.order_by('data_operat')[:10]
    robota=get_object_or_404(Robota, pk=idpracy)
    try:
        daneobs=robota.daneobsosnpom
    except:
        daneobs=DaneObsOsnPom()
        daneobs.save()
    if request.method == 'POST':
        daneobsForm=DaneObsOsnPomForm(request.POST, instance=daneobs)
        if daneobsForm.is_valid():
            daneobsForm.save()
            messages.success(request, 'Dane dotyczące Dane obserwacyjne osnowy zostały zaktualizowane')
            return render(request, 'operat/zestawienie.html', {
                "listaRobot": listaRobot
            })
    else:
        daneobsForm=DaneObsOsnPomForm(instance=daneobs)
    return render(request, 'operat/edycjaspr.html', {
        "Robota":robota,
        "form":daneobsForm,
    })

# edycja danych dotyczących Współrzędnych osnowy
def edycjaWykazWspOsn(request, idpracy):
    listaRobot = Robota.objects.order_by('data_operat')[:10]
    robota=get_object_or_404(Robota, pk=idpracy)
    try:
        wykazwsposn=robota.wykazwsposn
    except:
        wykazwsposn=WykazWspOsn()
        wykazwsposn.save()
    if request.method == 'POST':
        wykazwsposnForm=WykazWspOsnForm(request.POST, instance=wykazwsposn)
        if wykazwsposnForm.is_valid():
            wykazwsposnForm.save()
            messages.success(request, 'Dane dotyczące Wykazu Współrzednych Osnowy zaktualizowane')
            return render(request, 'operat/zestawienie.html', {
                "listaRobot": listaRobot
            })
    else:
        wykazwsposnForm=WykazWspOsnForm(instance=wykazwsposn)
    return render(request, 'operat/edycjaspr.html', {
        "Robota":robota,
        "form":wykazwsposnForm,
    })

# edycja danych dotyczących współrzędnyc punktów pomierzonych
def edycjaWykazWspPom(request, idpracy):
    listaRobot = Robota.objects.order_by('data_operat')[:10]
    robota=get_object_or_404(Robota, pk=idpracy)
    try:
        wykazwsppom=robota.wykazwsppom
    except:
        wykazwsppom=WykazWspPom()
        wykazwsppom.save()
    if request.method == 'POST':
        wykazwsppomForm=WykazWspPomForm(request.POST, instance=wykazwsppom)
        if wykazwsppomForm.is_valid():
            wykazwsppomForm.save()
            messages.success(request, 'Dane dotyczące wykazu współrzędnych punktów pomierzony zaktualizowano')
            return render(request, 'operat/zestawienie.html', {
                "listaRobot": listaRobot
            })
    else:
        wykazwsppomForm=WykazWspPomForm(instance=wykazwsppom)
    return render(request, 'operat/edycjaspr.html', {
        "Robota":robota,
        "form":wykazwsppomForm,
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

#usunięcie roboty
def usuniecie(request, idpracy):
    robota=get_object_or_404(Robota, pk=idpracy)
    robota.delete()
    messages.success(request, 'Dane dotyczące roboty zostały zaktualizowane')
    return redirect('zestawienie')

# generowanie dokumentacji
def generowanie(request):
    listaRobot = Robota.objects.order_by('data_operat')[:10]
    context={
        "listaRobot": listaRobot,
    }
    return render(request, 'operat/generowanie.html', context)