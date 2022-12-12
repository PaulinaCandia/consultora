from django.db import models

# Create your models here.

class Equipo(models.Model):
    # https://stackoverflow.com/a/59199143/6292472
    class Estado(models.TextChoices):
        BODEGA = "BODEGA", "Bodega"
        ASIGNADO = "ASIGNADO", "Asignado"
        MANTENCION = "MANTENCION", "Mantencion"

    class Condicion(models.TextChoices):
        OPERATIVO = "OPERATIVO", "Operativo"
        INOPERATIVO = "INOPERATIVO", "Inoperativo"
        FALLANDO = "FALLANDO", "Fallando"

    ide = models.IntegerField()
    nombre = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=256)
    estado = models.CharField(max_length=256, choices=Estado.choices, default=Estado.BODEGA)
    ubicacion = models.CharField(max_length=256)
    fecha_mantencion = models.DateField()
    condicion = models.CharField(max_length=256, choices=Condicion.choices, default=Condicion.OPERATIVO)
    observaciones = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f"{self.ide} - {self.nombre}"
