from django.db import models

class Professor(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    matricula = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    objetos = models.Manager()
