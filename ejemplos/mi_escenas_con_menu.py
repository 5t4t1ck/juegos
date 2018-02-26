# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

class EscenaMenu(pilasengine.escenas.Escena):

    def iniciar(self):
        self.fondo_menu = pilas.fondos.Volley()
        self.Mi_Menu = pilas.actores.Menu(
        [
            (u'IR AL JUEGO', self.Ir_al_Juego),
            (u'SALIR DE PILAS', self.Salir_de_Pilas)
        ]
        )

        Texto = pilas.actores.Texto(u'MI GRAN JUEGO')
        Texto.color = pilas.colores.rojo
        Texto.y = 170

    def actualizar(self):
        pass

    def Salir_de_Pilas(self):
        pilas.terminar()

    def Ir_al_Juego(self):
        pilas.escenas.EscenaJuego()

class EscenaJuego(pilasengine.escenas.Escena):

    def iniciar(self):
        self.fondo = pilas.fondos.Tarde()

        self.Mi_actor = pilas.actores.Mono()
        self.Mi_actor.decir("Hola, estamos en la escenas del Juego!!!")

        self.Boton_Volver = pilas.interfaz.Boton("Volver al Menu")
        self.Boton_Volver.y = -100
        self.Boton_Volver.conectar(self.Volver)

    def actualizar(self):
        pass

    def Volver(self):
        pilas.escenas.EscenaMenu()

pilas.escenas.vincular(EscenaMenu)
pilas.escenas.vincular(EscenaJuego)

pilas.escenas.EscenaJuego()

pilas.ejecutar()
