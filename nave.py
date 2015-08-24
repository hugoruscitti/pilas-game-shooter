import pilasengine


class NaveProtagonista(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "imagenes/naveProtagonista.png"
        self.pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_tecla)
        self.pilas.eventos.suelta_tecla.conectar(self.cuando_suelta_tecla)

    def cuando_pulsa_tecla(evento, texto):
        print "evento:", evento, "texto:", texto

    def cuando_suelta_tecla(evento, texto):
        print "evento:", evento, "texto:", texto
