from gng import *
'''nodo1 = Nodo(1,[1,2],2)
nodo2 = Nodo(2,[1,2],4)

arista = Arista(nodo1,nodo2,2,2)

grafo = Grafo()
grafo.addNodo(nodo1)

grafo.addNodo(nodo2)

grafo.addArista(arista)

grafo.findNodo(nodo1)'''

grafo = Grafo()
mytopologia = topologia()
mygng = gng(mytopologia,grafo)

mygng.begin()