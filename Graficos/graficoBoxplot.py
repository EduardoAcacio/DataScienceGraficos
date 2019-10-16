import matplotlib.pyplot as pyplot
import random

vetor = []

for i in range(10):
    numero_aleatorio = random.randint(0,1000)
    vetor.append(numero_aleatorio)

titulo = "Boxplot"

pyplot.boxplot(vetor)
pyplot.title(titulo)
pyplot.show()
