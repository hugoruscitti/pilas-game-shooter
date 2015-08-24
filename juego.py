import pilasengine
import ufo
import nave

pilas = pilasengine.iniciar()


# Vinculando actores
pilas.actores.vincular(ufo.UFO)
pilas.actores.vincular(nave.NaveProtagonista)

# Creación de actores
pilas.actores.UFO() * 2
pilas.actores.NaveProtagonista()

pilas.ejecutar()
