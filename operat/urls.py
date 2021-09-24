from django.http.response import HttpResponseRedirect
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zestawienie', views.zestawienie, name='zestawienie'),
    path('generowanie', views.generowanie, name='generowanie'),
    path('nowa', views.nowa, name='nowa'),
    path('<idpracy>/edycja',views.edycja, name='edycja'),
    path('<idpracy>/dokumentacja', views.dokumentacja, name="dokumentacja"),
    path('<idpracy>/usuniecie', views.usuniecie, name='usuniecie'),
    path('<idpracy>/', views.szczegoly, name="szczegoly"),
    path('<idpracy>/edycjaspr',views.edycjaSprawozdanie, name='edycjaspr'),
    path('<idpracy>/edycjampzt',views.edycjaMpzt, name='edycjampzt'),
    path('<idpracy>/edycjadaneobs',views.edycjaDaneObs, name='edycjadaneobs'),
    #path('operat/<slug:idpracy>', views.szczegoly, name="slug szczegoly")
    ]