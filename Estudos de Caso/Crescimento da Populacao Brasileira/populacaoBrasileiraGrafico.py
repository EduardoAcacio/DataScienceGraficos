# Crescimento da População Brasileira 1980-2016
# Fonte: DataSus

import matplotlib.pyplot as pyplot

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

pyplot.bar(x,y, color = "#e4e4e4")
pyplot.plot(x,y, color = "k", linestyle = "--")
pyplot.title("Crescimento da População Brasileira 1980-2016")
pyplot.xlabel("Ano")
pyplot.ylabel("População x100.000.000")

#pyplot.show()
pyplot.savefig("crescimentoBrasileiro.png", dpi = 300)