import pilasengine


class NaveProtagonista(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "imagenes/naveProtagonista.png"
        self.pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_tecla)
        self.pilas.eventos.suelta_tecla.conectar(self.cuando_suelta_tecla)
        self.pilas.eventos.click_de_mouse.conectar(self.cuando_hace_click_2)
        self.dx = 0
        self.dy = 0
        self.ir_izquierda = False
        self.ir_derecha = False
        self.ir_arriba = False
        self.ir_abajo = False
        self.aprender('rotarConMouse')

    def cuando_pulsa_tecla(self, evento):
        if evento['texto'] == 'd':
            self.ir_derecha = True

        if evento['texto'] == 'a':
            self.ir_izquierda = True

        if evento['texto'] == 'w':
            self.ir_arriba = True

        if evento['texto'] == 's':
            self.ir_abajo = True

    def cuando_suelta_tecla(self, evento):
        if evento['texto'] == 'd':
            self.ir_derecha = False

        if evento['texto'] == 'a':
            self.ir_izquierda = False

        if evento['texto'] == 'w':
            self.ir_arriba = False

        if evento['texto'] == 's':
            self.ir_abajo = False

    def actualizar(self):
        self.dx *= 0.9
        self.dy *= 0.9

        if self.ir_izquierda:
            self.dx = -3
        if self.ir_derecha:
            self.dx = 3

        if self.ir_arriba:
            self.dy = 3
        if self.ir_abajo:
            self.dy = -3

        self.x += self.dx
        self.y += self.dy


    def cuando_hace_click_2(self, evento):
        print evento
