from django.db import models


# Create your models here.
class Person(models.Model):
    nome = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    titolo = models.CharField(max_length=100)
    immagine = models.CharField(max_length=200, default='no')

    def __str__(self):
        return self.nome
