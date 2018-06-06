from gng import *
'''nodo1 = Nodo(1,[1,2],2)
nodo2 = Nodo(2,[1,2],4)

arista = Arista(nodo1,nodo2,2,2)

grafo = Grafo()
grafo.addNodo(nodo1)

grafo.addNodo(nodo2)

grafo.addArista(arista)

grafo.findNodo(nodo1)'''
nodo1= Nodo(1,[5,7],0)
grafo = Grafo()
mytopologia = topologia()
posiciones=[(66, 111), (462, 98), (94, 405), (454, 406)]
print posiciones
for i in range(len(posiciones)):
    mytopologia.addNodo(i,posiciones[i],0)

mygng = gng(mytopologia,grafo)

mygng.begin()
