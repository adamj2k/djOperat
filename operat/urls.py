from django.conf.urls import url
from django.conf import settings
from django.http.response import HttpResponseRedirect
from django.views.generic import RedirectView
from django.urls import include, re_path, path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
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
    path('<idpracy>/edycjawsposn', views.edycjaWykazWspOsn, name='edycjawsposn'),
    path('<idpracy>/edycjawsppom', views.edycjaWykazWspPom, name='edycjawsppom'),
    path('<idpracy>/edycjaszkicpol', views.edycjaSzkicPolowy, name='edycjaszkicpol'),
    path('<idpracy>/edycjaszkicosn', views.edycjaSzkicOsnowyPom, name='edycjaszkicosn'),
    #path('operat/<slug:idpracy>', views.szczegoly, name="slug szczegoly")
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
