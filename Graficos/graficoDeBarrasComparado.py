import matplotlib.pyplot as pyplot

x1 = [1,3,5,7,9]
y1 = [2,3,7,1,6]

x2 = [2,4,6,8,10]
y2 = [5,1,3,7,4]

titulo = "Grafico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

pyplot.title(titulo)
pyplot.xlabel(eixox)
pyplot.ylabel(eixoy)

pyplot.bar(x1, y1, label = "Orçado")
pyplot.bar(x2, y2, label = "Realizado")
pyplot.legend()
pyplot.show()
