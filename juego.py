import pilasengine
import ufo
import nave
import disparo

pilas = pilasengine.iniciar()


# Vinculando actores
pilas.actores.vincular(ufo.UFO)
pilas.actores.vincular(nave.NaveProtagonista)
pilas.actores.vincular(disparo.Disparo)

# Creación de actores
pilas.actores.UFO() * 4
nave = pilas.actores.NaveProtagonista()


pilas.ejecutar()
