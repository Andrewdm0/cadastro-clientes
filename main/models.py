from django.db import models

class Cliente(models.Model):
    STATUS = [
        ('Pago','Pago'),
        ('Devendo','Devendo'),
    ]
    nome = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=7,
        choices=STATUS,
        )
    def __str__(self):
        return self.nome
