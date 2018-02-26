# coding: utf-8
import pilasengine, random

pilas = pilasengine.iniciar()

class Menu(pilasengine.escenas.Escena):

    def iniciar(self):
        fondo = pilas.fondos.Fondo()
        fondo.imagen = pilas.imagenes.cargar("data/vecindad_fondo.jpg")
        self.Mi_Menu = pilas.actores.Menu(
        [
            (u'IR AL JUEGO', self.Ir_al_Juego),
            (u'SALIR DE PILAS', self.Salir_de_Pilas),
            (u'Ganaste', self.Ganaste),
            (u'Perdiste', self.Perdiste)
        ]
        )

    def actualizar(self):
        pass

    def Salir_de_Pilas(self):
        pilas.terminar()

    def Ir_al_Juego(self):
        pilas.escenas.Juego()

    def Ganaste(self):
        pilas.escenas.Ganaste()

    def Perdiste(self):
        pilas.escenas.Perdiste()

class Juego(pilasengine.escenas.Escena):

    def iniciar(self):
        fondo = pilas.fondos.Fondo()
        fondo.imagen = pilas.imagenes.cargar("data/vecindad_fondo.jpg")
        self.Boton_Volver = pilas.interfaz.Boton("Volver al Menu")
        self.Boton_Volver.y = 200
        self.Boton_Volver.x = 200

        self.Boton_Volver.conectar(self.Volver)
        pilas.tareas.siempre(1, crear_torta)
        pilas.tareas.siempre(2, crear_bruja)
        chavo = pilas.actores.Chavo()
        pilas.avisar(u"Intente atrapar la mayor cantidad de Tortas de Jamon")
        pilas.colisiones.agregar("chavo", "torta", cuando_toca_torta)
        pilas.colisiones.agregar("chavo", "bruja", cuando_toca_bruja)

    def actualizar(self):
        pass

    def Volver(self):
        pilas.escenas.Menu()

class Ganaste(pilasengine.escenas.Escena):

    def iniciar(self):
        self.fondo = pilas.fondos.Noche()

        self.Boton_Volver = pilas.interfaz.Boton("Volver al Menu")
        self.Boton_Volver.y = -100
        self.Boton_Volver.conectar(self.Volver)

    def actualizar(self):
        pass

    def Volver(self):
        pilas.escenas.Menu()

class Perdiste(pilasengine.escenas.Escena):

    def iniciar(self):
        fondo = pilas.fondos.Fondo()
        fondo.imagen = pilas.imagenes.cargar("data/perdiste.png")
        self.Boton_Volver = pilas.interfaz.Boton("Volver al Menu")
        self.Boton_Volver.y = -100
        self.Boton_Volver.conectar(self.Volver)

    def actualizar(self):
        pass

    def Volver(self):
        pilas.escenas.Menu()

#Creando actores

class Chavo(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "data/chavo.png"
        self.y = -144
        self.escala = 0.9
        self.etiquetas.agregar('chavo')
        self.figura_de_colision = pilas.fisica.Rectangulo(
            0, 0, 60, 170, sensor=True
        )
        self.aprender("LimitadoABordesDePantalla")

    def actualizar(self):

        if pilas.control.izquierda:
            self.x -= 5
            self.espejado = True

        if pilas.control.derecha:
            self.x += 5
            self.espejado = False

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

class Bruja(pilasengine.actores.Aceituna):

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


def crear_torta():
    actor = pilas.actores.Torta_de_Jamon()
    tortas.agregar(actor)

def crear_bruja():
    actor1 = pilas.actores.Bruja()
    brujas.agreagar(actor1)

puntaje = pilas.actores.Puntaje(-300, 200, color=pilas.colores.blanco)

def cuando_toca_torta(c, t):
    t.eliminar()
    puntaje.aumentar(1)
    puntaje.escala = 2
    puntaje.escala = [1], 0.2
    puntaje.rotacion = random.randint(30, 60)
    puntaje.rotacion = [0], 0.2

def cuando_toca_bruja(c, b):
    b.eliminar()
    puntaje.escala = 2
    puntaje.escala = [1], 2.0
    puntaje.rotacion = random.randint(30, 60)
    puntaje.rotacion = [0], 0.2
    c.eliminar()
    pilas.escenas.Perdiste()

tortas = pilas.actores.Grupo()
brujas = pilas.actores.Grupo()

pilas.escenas.vincular(Menu)
pilas.escenas.vincular(Juego)
pilas.escenas.vincular(Ganaste)
pilas.escenas.vincular(Perdiste)
pilas.actores.vincular(Chavo)
pilas.actores.vincular(Torta_de_Jamon)
pilas.actores.vincular(Bruja)
pilas.escenas.Menu()

pilas.ejecutar()
