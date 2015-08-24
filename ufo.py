import pilasengine

class UFO(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "imagenes/ufo1.png"
        self.radio_de_colision = 40
        self.dx = self.pilas.azar(-1, 1) / 2.0
        self.dy = self.pilas.azar(-1, 1) / 2.0
        self.aprender('seMantieneEnPantalla')

    def actualizar(self):
        self.rotacion -= 5
        self.x += self.dx
        self.y += self.dy
