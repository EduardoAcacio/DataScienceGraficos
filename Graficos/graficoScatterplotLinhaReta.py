import matplotlib.pyplot as pyplot

x1 = [1,100]
y1 = [1,100]

x2 = [1,2,3,22,5,3,32,52,2,5,3,32,5]
y2 = [2,3,4,1,16,4,13,23,4,1,16,4,45]

titulo = "Grafico de Scatterplot"
eixox = "Eixo X"
eixoy = "Eixo Y"

pyplot.title(titulo)
pyplot.xlabel(eixox)
pyplot.ylabel(eixoy)

pyplot.scatter(x2, y2, label = "Dispersão", color = "r")
pyplot.plot(x1, y1)
pyplot.legend()
pyplot.show()
