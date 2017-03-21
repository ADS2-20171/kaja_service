from django.db import models

# Create your models here.


class Cliente(models.Model):

    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre
