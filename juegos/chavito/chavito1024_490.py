# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
Autor: @Statick_ds
Objetivo del Juego: Atrapar la mayor cantidad de Tortas de Jamon que caen
y evitar tocar las fotografias de la Bruja del 71
"""

# Importamos la Biblioteca de Pilas-Engine y el módulo random
import random
import sys

import pilasengine

# Iniciando PilasEngine en un sola variable para facilitar la programación
pilas = pilasengine.iniciar(800, 490)

try:
    pilas.reiniciar_si_cambia(sys.argv[0])
except OSError:
    pilas.reiniciar_si_cambia(__file__)

# Declarando la clase Chavo


class Chavo(pilasengine.actores.Actor):

    # Creando la función iniciar del actor chavo
    def iniciar(self):
        self.imagen = "data/chavo.png"
        self.y = -144
        self.escala = 0.9
        self.etiquetas.agregar('chavo')
        self.figura_de_colision = pilas.fisica.Rectangulo(
            0, 0, 60, 170, sensor=True
        )

    # Creando la función actualizar del actor chavo
    def actualizar(self):
        # Haciendo que el actor chavo se mueva a la derecha con tecla derecha
        if pilas.control.izquierda:
            self.x -= 5
            self.espejado = True

        if self.x <= -370:
            self.x = -370

        # Haciendo que el actor chavo se mueva a la
        # izquierda con la tecla izquierda
        if pilas.control.derecha:
            self.x += 5
            self.espejado = False

        if self.x >= 370:
            self.x = 370

        # Haciendo que el actor chavo se mueva hacia arriba con la tecla arriba
        if pilas.control.arriba:
            self.y += 5

            self.y -= 5

# Creando la clase Torta de Jamon


class Torta_de_Jamon(pilasengine.actores.Aceituna):

    # Inicializando la clase Torta de Jamon
    def iniciar(self):
        self.imagen = "data/torta_de_jamon.png"
        self.aprender(pilas.habilidades.PuedeExplotarConHumo)
        self.x = pilas.azar(-370, 370)
        self.y = 290
        self.velocidad = pilas.azar(5, 30) / 10.0
        self.etiquetas.agregar('torta')
        self.figura_de_colision = pilas.fisica.Rectangulo(
            0, 0, 60, 40, sensor=True
        )

    # Creando función actualizar
    def actualizar(self):
        self.rotacion += 5
        self.y -= self.velocidad

        # Eliminar el objeto cuando sale de la pantalla.
        if self.y < -300:
            self.eliminar()

# Creando la clase Bruja del 71


class Bruja_del_71(pilasengine.actores.Aceituna):

    # Inicializando la clase Torta de Jamon
    def iniciar(self):
        self.imagen = "data/bruja_del_71.png"
        self.aprender(pilas.habilidades.PuedeExplotarConHumo)
        self.x = pilas.azar(-370, 370)
        self.y = 290
        self.velocidad = pilas.azar(5, 30) / 10.0
        self.etiquetas.agregar('bruja')
        self.figura_de_colision = pilas.fisica.Rectangulo(
            0, 0, 60, 86, sensor=True
        )

    # Creando función actualizar
    def actualizar(self):
        self.rotacion += 5
        self.y -= self.velocidad

        # Eliminar el objeto cuando sale de la pantalla.
        if self.y < -300:
            self.eliminar()

# Agregando Fondo
fondo = pilas.fondos.Fondo()
fondo.imagen = pilas.imagenes.cargar("data/vecindad_fondo.jpg")

# Creando el grupo tortas y bruja
tortas = pilas.actores.Grupo()
brujas = pilas.actores.Grupo()

# Creando la función crear_torta, esta función permite crear los enemigos


def crear_torta():
    actor = Torta_de_Jamon(pilas)
    tortas.agreagar(actor)


def crear_bruja():
    actor1 = Bruja_del_71(pilas)
    tortas.agreagar(actor1)

# Agregar la tarea de crear el tortas cada segundo
pilas.tareas.siempre(1, crear_torta)

# Agregar la tarea de crear brujas cada 2 segundos
pilas.tareas.siempre(2, crear_bruja)

# crear el objeto chavo
chavo = Chavo(pilas)

# Agregando el Puntaje
puntaje = pilas.actores.Puntaje(-365, 200, color=pilas.colores.blanco)

# Crear la función que permite al objeto chavo comer las Tortas de Jamon


def cuando_toca_torta(v, i):
    i.eliminar()
    puntaje.aumentar(1)
    puntaje.escala = 2
    puntaje.escala = [1], 0.2
    puntaje.rotacion = random.randint(30, 60)
    puntaje.rotacion = [0], 0.2

# Crear la función que permite al objeto chavo
# eliminarse cuando toca las Brujas del 71


def cuando_toca_bruja(v, i):
    i.eliminar()
    puntaje.reducir(1)
    puntaje.escala = 2
    puntaje.escala = [1], 2.0
    puntaje.rotacion = random.randint(30, 60)
    puntaje.rotacion = [0], 0.2

# Se crea las colisiones entre los actores torta y chavo,
# se llama a la función cuanto_toca_torta
pilas.colisiones.agregar("chavo", "torta", cuando_toca_torta)

# Se crea las colisiones entre los actores bruja y chavo,
# se llama a la funcion cuando_toca_bruja
pilas.colisiones.agregar("chavo", "bruja", cuando_toca_bruja)

# Muestra un mensaje en pantalla con indicaciones de que se trata el Juego
pilas.avisar(u"Intente atrapar la mayor cantidad de Tortas de Jamon")

# Permite al motor de pilas ejecutarse
pilas.ejecutar()
