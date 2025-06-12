from django.db import models

# Create your models here.
# Entidad Equipo de Futbol
class EquipoFutbol(models.Model):
    nombre = models.CharField("Nombre del equipo", max_length=50)
    siglas = models.CharField("Siglas", max_length=10)
    username_twitter = models.CharField("Usuario de Twitter", max_length=30)

    def __str__(self):
        return f"{self.nombre} ({self.siglas})"

# Entidad Jugador
class Jugador(models.Model):
    POSICIONES = (
        ('arquero', 'Arquero'),
        ('defensa', 'Defensa'),
        ('mediocampo', 'Mediocampo'),
        ('delantero', 'Delantero'),
    )
    nombre = models.CharField("Nombre del jugador", max_length=50)
    posicion_campo = models.CharField("Posición en el campo", max_length=20, choices=POSICIONES)
    numero_camiseta = models.IntegerField("Número de camiseta")
    sueldo = models.DecimalField("Sueldo", max_digits=10, decimal_places=2)
    equipo_futbol = models.ForeignKey(EquipoFutbol, related_name='jugadores', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.posicion_campo} - #{self.numero_camiseta}"

# Entidad Campeonato
class Campeonato(models.Model):
    nombre_campeonato = models.CharField("Nombre del campeonato", max_length=50)
    nombre_auspiciante = models.CharField("Nombre del auspiciante", max_length=50)

    def __str__(self):
        return f"{self.nombre_campeonato} ({self.nombre_auspiciante})"

# Entidad CampeonatoEquipos
class CampeonatoEquipos(models.Model):
    año = models.IntegerField("Año")
    equipo_futbol = models.ForeignKey(EquipoFutbol, related_name='campeonatos', on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='equipos', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.año} - {self.equipo_futbol} en {self.campeonato}"