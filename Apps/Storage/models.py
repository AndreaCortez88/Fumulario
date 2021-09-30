from django.db import models

# Create your models here.
class cliente(models.Model):
    pk_cliente = models.AutoField(primary_key=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    telefono=models.CharField(max_length=8, blank=False, null=False)

class animal(models.Model):
    pk_animal = models.AutoField(primary_key=True, blank=False, null=False)
    nombreani = models.CharField(max_length=50, blank=False, null=False)
    edadani = models.CharField(max_length=2, blank=False, null=False)
    razaani=models.CharField(max_length=15, blank=False, null=False)
