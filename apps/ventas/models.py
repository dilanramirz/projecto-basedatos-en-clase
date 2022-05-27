from django.db import models
from django.contrib.auth.models import User
from apps.vehiculos.models import Vehiculo

# Create your models here.


class Venta(models.Model):
    fecha = models.DateField()
    valortotal = models.BigIntegerField()
    tipopago = models.CharField(max_length=60)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Vehiculo = models.ManyToManyField(Vehiculo, through='VehiculoVenta')



class VehiculoVenta(models.Model):
    Vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, blank=False, null=False)
    Venta = models.ForeignKey(Venta, on_delete=models.CASCADE, blank=False, null=False)
    cantidad = models.BigIntegerField()
    precio = models.BigIntegerField()

