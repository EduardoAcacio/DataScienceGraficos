import matplotlib.pyplot as pyplot

x = [1,2,3,4,5]
y = [2,3,7,1,6]
z = [200, 25, 400, 1330, 100]

titulo = "Grafico de Scatterplot"
eixox = "Eixo X"
eixoy = "Eixo Y"

pyplot.title(titulo)
pyplot.xlabel(eixox)
pyplot.ylabel(eixoy)

pyplot.plot(x, y, color = "#F08080", linestyle = "--")
pyplot.scatter(x, y, label = "Meus Pontos", color = "k", marker = "h", s=z)
pyplot.legend()
pyplot.show()
