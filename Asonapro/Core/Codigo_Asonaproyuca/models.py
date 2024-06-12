from django.db import models

# Create your models here.


class Codigo(models.Model):
    codigo = models.IntegerField(
        max_length=20, unique=True, verbose_name="Codigo Asonaproyuca")

    def __str__(self):
        return self.codigo
