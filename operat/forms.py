from django import forms
from .models import Robota

class RobotaForm(forms.ModelForm):
    class Meta:
        model=Robota
        fields=['idpracy', 'wojew', 'powiat','jew', 'obr', 'obiekt', 'dzialki', 'data_aktu', 'data_mat', 'zmianaBDOT', 'zmianaGESUT', 'zmianaEGIB', 'data_operat', 'obszar', 'status']
        