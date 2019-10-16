import matplotlib.pyplot as pyplot

x = [1,2,3,4,5]
y = [2,3,7,1,6]

titulo = "Grafico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

pyplot.title(titulo)
pyplot.xlabel(eixox)
pyplot.ylabel(eixoy)

pyplot.bar(x, y)
pyplot.show()
