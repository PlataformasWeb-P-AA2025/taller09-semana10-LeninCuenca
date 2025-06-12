from django.contrib import admin
from .models import EquipoFutbol,Jugador, Campeonato, CampeonatoEquipos

# Register your models here.
@admin.register(EquipoFutbol)
class EquipoFutbolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'username_twitter')
    search_fields = ('nombre', 'siglas')

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion_campo', 'numero_camiseta', 'sueldo', 'equipo_futbol')
    list_filter = ('posicion_campo', 'equipo_futbol')
    search_fields = ('nombre',)

@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre_campeonato', 'nombre_auspiciante')
    search_fields = ('nombre_campeonato',)

@admin.register(CampeonatoEquipos)
class CampeonatoEquiposAdmin(admin.ModelAdmin):
    list_display = ('año', 'equipo_futbol', 'campeonato')
    list_filter = ('año', 'campeonato')
