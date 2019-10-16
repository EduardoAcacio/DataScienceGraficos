import matplotlib.pyplot as pyplot

x = [1,2,5]
y = [2,3,7]

pyplot.title("Meu primeiro grafico em Python usando Matplot")

pyplot.xlabel("Eixo X")
pyplot.ylabel("Eixo Y")

pyplot.plot(x, y)
pyplot.show()
