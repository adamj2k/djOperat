from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Robota(models.Model):
    idpracy=models.CharField(max_length=25, null=True, default='XX.6640.XXXX.RRRR')
    wojew=models.CharField(max_length=50, null=True, default='zachodniopomorskie')
    powiat=models.CharField(max_length=50, null=True)
    jew=models.CharField(max_length=50, null=True)
    obr=models.CharField(max_length=50, null=True)
    obiekt=models.CharField(max_length=100, null=True)
    dzialki=models.CharField(max_length=50, null=True)
    data_operat=models.CharField(max_length=10, null=True)
    obszar=models.CharField(max_length=50, null=True)
    def __str__(self):
        return f'{self.idpracy} - {self.obiekt}'

  
class Sprawozdanie(models.Model):
    idpracy=models.ForeignKey(Robota, on_delete=models.CASCADE)
    zakresMat=models.TextField(default='Po analizie materiałów pozyskanych z PZGiK do...')
    techMet1=models.TextField(default='Wykonano pomiar ... ')
    techMet2=models.TextField(default='elementy zostały pomierzone metodą ...')
    def __str__(self):
        return f'Sprawozdanie {self.idpracy}'
