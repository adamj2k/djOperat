from django import forms
from django.forms import fields
from .models import DaneObsOsnPom, Robota, Sprawozdanie, MapaPorownania

class RobotaForm(forms.ModelForm):
    class Meta:
        model=Robota
        fields=['idpracy', 'wojew', 'powiat','jew', 'obr', 'obiekt', 'dzialki', 'data_aktu', 'data_mat', 'zmianaBDOT', 'zmianaGESUT', 'zmianaEGIB', 'data_operat', 'obszar', 'status']

class SprawozdanieForm(forms.ModelForm):
    class Meta:
        model=Sprawozdanie
        fields=['idpracy', 'zakresMat', 'techMet1', 'techMet2', 'techMet3',
        'techMet4', 'techMet5', 'zudpozwolenie', 'granice', 'dokZamawiajacy',
        'zasilenie', 'egibzmiany']

class MapaPorownaniaForm(forms.ModelForm):
    class Meta:
        model=MapaPorownania
        fields=['idpracy', 'mpztPDF']

class DaneObsOsnPomForm(forms.ModelForm):
    class Meta:
        model=DaneObsOsnPom
        fields=['idpracy', 'raport']
        