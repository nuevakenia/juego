from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Personaje(models.Model):
    '''Carreras de cada sede'''
    nombre = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.nombre}"


class PersonajeDetalle(models.Model):
    personaje = models.ForeignKey(Personaje, related_name='personaje_detalles', on_delete=models.CASCADE)
    nivel = models.IntegerField(default=1)
    exp = models.IntegerField(default=1)
    vida = models.IntegerField(default=1)
    energia = models.IntegerField(default=1)
    fuerza = models.IntegerField(default=1)
    destreza = models.IntegerField(default=1)
    inteligencia = models.IntegerField(default=1)


class Sala(models.Model):
    nombre = models.CharField(max_length=300)
    jugador1 = models.ForeignKey(Personaje, related_name='salas_jugador1', on_delete=models.CASCADE)
    jugador2 = models.ForeignKey(Personaje, related_name='salas_jugador2', on_delete=models.CASCADE)


class Tienda(models.Model):
    nombre = models.CharField(max_length=300)
    nivel = models.ForeignKey(Personaje, related_name='Tiendas', on_delete=models.CASCADE)
    dialogo = models.CharField(max_length=300)


class Item(models.Model):
    nombre = models.CharField(max_length=300)


class ItemDetalle(models.Model):
    item = models.ForeignKey(Item, related_name='items_detalles', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    nivel = models.IntegerField(default=1)
    sinergia1 = models.IntegerField(null=True, blank=True)
    sinergia2 = models.IntegerField(null=True, blank=True)
    sinergia3 = models.IntegerField(null=True, blank=True)


class TiendaPrecios(models.Model):
    tienda = models.ForeignKey(Tienda, related_name='tienda_precios_tiendas', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='tienda_precios_items', on_delete=models.CASCADE)
    precio = models.IntegerField(default=1)


class Inventario(models.Model):
    personaje = models.ForeignKey(Personaje, related_name='inventarios_personaje', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='inventarios_items', on_delete=models.CASCADE)
    posicion = models.IntegerField()


class Accion(models.Model):
    nombre = models.CharField(max_length=300)
    jugador1 = models.ForeignKey(Personaje, related_name='Acciones', on_delete=models.CASCADE)


class Arena(models.Model):
    nombre = models.CharField(max_length=300)
    jugador1 = models.ForeignKey(Personaje, related_name='Arenas', on_delete=models.CASCADE)


class AccionDetalle(models.Model):
    accion = models.ForeignKey(Accion, related_name='acciones_detalles_accion', on_delete=models.CASCADE)
    arena = models.ForeignKey(Arena, related_name='acciones_detalles_arenas', on_delete=models.CASCADE)


class Resultado(models.Model):
    puntaje1 = models.ForeignKey(Personaje, related_name='resultados_puntaje1', on_delete=models.CASCADE)
    puntaje2 = models.ForeignKey(Personaje, related_name='resultados_puntaje2', on_delete=models.CASCADE)
    tiempo = models.TimeField(null=True, blank=True)
    # ponerle fecha, detalles de puntos y tiempo duracion


class Partida(models.Model):
    jugador1 = models.ForeignKey(Personaje, related_name='partidas_jugador1', on_delete=models.CASCADE)
    jugador2 = models.ForeignKey(Personaje, related_name='partidas_jugador2', on_delete=models.CASCADE)
    arena = models.ForeignKey(Arena, related_name='partidas_arenas', on_delete=models.CASCADE)
    resultado = models.ForeignKey(Resultado, related_name='partidas_resultados', on_delete=models.CASCADE)
