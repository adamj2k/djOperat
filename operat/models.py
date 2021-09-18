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
    data_aktu=models.CharField(max_length=10, null=True, default='RRRR-MM-DD')
    data_mat=models.CharField(max_length=10, null=True, default='RRRR-MM-DD')
    zmianaBDOT=models.BooleanField(default=False, null=True)
    zmianaGESUT=models.BooleanField(default=False, null=True)    
    zmianaEGIB=models.BooleanField(default=False, null=True)
    data_operat=models.CharField(max_length=10, null=True)
    obszar=models.CharField(max_length=50, null=True)
    status=models.CharField(max_length=10, null=True, default='w trakcie')
    def __str__(self):
        return f'{self.idpracy} - {self.obiekt}'

  
class Sprawozdanie(models.Model):
    idpracy=models.OneToOneField(Robota, on_delete=models.CASCADE, null=True)
    zakresMat=models.TextField(default='Po analizie materiałów pozyskanych z PZGiK do...')
    techMet1=models.TextField(default='Wykonano porównanie... ')
    techMet2=models.TextField(default='Założono osnowę pomiarową ...')
    techMet3=models.TextField(default='Wykonano pomiar kontrolny ...')
    techMet4=models.TextField(default='Wykonano pomiar systuacyjny metodą ...')
    techMet5=models.TextField(default='Wyniki uzyskano w układzie ...')
    zudpozwolenie=models.TextField(default='ZUD i pozwolenie na budowe ..')
    granice=models.TextField(default='Granice spełniają/nie spełniają ...')
    dokZamawiajacy=models.TextField(default='Dla zamawiającego przygotowano...')
    zasilenie=models.TextField(default='Przekazno pliki w formacie ...')
    egibzmiany=models.TextField(default='Kierownik prac stwierdził/nie stwierdził ...')
    def __str__(self):
        return f'Sprawozdanie {self.idpracy}'


class MapaPorownania(models.Model):
    idpracy=models.OneToOneField(Robota, on_delete=models.CASCADE)
    mpztPDF=models.FileField(upload_to='temp/')
    def __str__(self):
        return f'MPzT {self.idpracy}'

class DaneObsOsnPom(models.Model):
    idpracy=models.OneToOneField(Robota, on_delete=models.CASCADE, null=True)
    raport=models.TextField(default='Wynik wyrównania/raport z pomiaru GPS ...')
    def __str__(self):
        return f'Dane Obserwacyjne {self.idpracy}'

class SzkicOsnowyPom(models.Model):
    idpracy=models.OneToOneField(Robota, on_delete=models.CASCADE, null=True)
    szkicPDF=models.FileField(upload_to='temp/')
    def __str__(self):
        return f'Szkic Osnowy {self.idpracy}'

class WykazWspOsn(models.Model):
    idpracy=models.OneToOneField(Robota, on_delete=models.CASCADE, null=True)
    wykaz=models.TextField(default='Wykaz wsp')
    def __str__(self):
        return f'Wykaz wsp. osnowy {self.idpracy}'

class SzkicPolowy(models.Model):
    idpracy=models.OneToOneField(Robota, on_delete=models.CASCADE, null=True)
    szkicpolPDF=models.FileField(upload_to='temp/')
    def __str__(self):
        return f'Szkic polowy {self.idpracy}'

class WykazWspPom(models.Model):
    idpracy=models.OneToOneField(Robota, on_delete=models.CASCADE, null=True)
    wykazpom=models.TextField(default='Wykaz współrzędnych punktów pomierzonych ')
    def __str__(self):
        return f'Wykaz wsp. pomierzonych {self.idpracy}'