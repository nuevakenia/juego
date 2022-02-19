from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class PersonajeDetalle(models.Model):

    nivel = models.IntegerField(default=1)
    exp = models.IntegerField(default=1)
    vida = models.IntegerField(default=1)
    energia = models.IntegerField(default=1)
    fuerza = models.IntegerField(default=1)
    destreza = models.IntegerField(default=1)
    inteligencia = models.IntegerField(default=1)





class ArbolDetalle(models.Model):
    suerte = models.IntegerField(default=1)
    agilidad = models.IntegerField(default=1)
    carisma = models.IntegerField(default=1)
    inteligencia = models.IntegerField(default=1)
    fuerza = models.IntegerField(default=1)
    percepcion = models.IntegerField(default=1)
    resistencia = models.IntegerField(default=1)
    
class Arbol(models.Model):
    detalle_arbol = models.OneToOneField(ArbolDetalle, related_name='arbol_detalles', on_delete=models.CASCADE)


class Personaje(models.Model):

    nombre = models.CharField(max_length=300)
    user = models.ForeignKey(User, related_name='personajes_users', on_delete=models.CASCADE)
    detalle = models.OneToOneField(PersonajeDetalle, related_name='personajes_detalles', on_delete=models.CASCADE)
    arbol = models.ForeignKey(Arbol, related_name='personajes_arbol', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}"


class ExtendUser(models.Model):
    r = models.OneToOneField(User, on_delete=models.CASCADE)
    pj_seleccionado = models.ForeignKey(Personaje, on_delete=models.CASCADE)

    def __str__(self):
        return self.r.username


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


class InventarioDetalle(models.Model):
    item = models.ForeignKey(Item, related_name='inventario_detalles', on_delete=models.CASCADE)
    posx = models.IntegerField(default=1)
    posy = models.IntegerField(default=1)
    posz = models.IntegerField(default=1)
    # guardar el tamaño de cada item con un numero de 3 digitos, cada digito significa una cordenada x y z ej;; 380.
    tam = models.IntegerField(default=1)


class Inventario(models.Model):
    personaje = models.ForeignKey(Personaje, related_name='inventarios_personaje', on_delete=models.CASCADE)
    arreglo = models.ForeignKey(InventarioDetalle, related_name='inventarios_arreglo', on_delete=models.CASCADE)
    numero_casilleros = models.IntegerField(default=1)


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


