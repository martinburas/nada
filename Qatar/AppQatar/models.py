from django.db import models

# Create your models here.
class Seleccion(models.Model):
    pais=models.CharField(max_length=60)
    continente= models.CharField(max_length=60)

class Estadio(models.Model):
    nombre= models.CharField(max_length=60)
    ciudad= models.CharField(max_length=60)

class Copas(models.Model):
    selecc= models.CharField(max_length=60)
    cantCopas= models.IntegerField()
    ultimaCopa= models.IntegerField()
    
