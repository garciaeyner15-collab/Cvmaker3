from django.db import models

# Create your models here.
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre





        cliente = Cliente.objects.create(
    nombre="Juan Pérez",
    email="juan@gmail.com"
)


# Obtener todos los clientes
clientes = Cliente.objects.all()

# Obtener un cliente específico
cliente = Cliente.objects.get(id=1)

# Filtrar clientes activos
clientes_activos = Cliente.objects.filter(activo=True)


cliente = Cliente.objects.get(id=1)
cliente.nombre = "Carlos López"
cliente.save()


cliente = Cliente.objects.get(id=1)
cliente.delete()



