from grafo import *

nodo1 = nodo(1,[1,2],2)
nodo2 = nodo(2,[1,2],4)

arista = aristas(nodo1,nodo2,2,2)

grafo = grafo()
grafo.addnodo(nodo1)

grafo.addnodo(nodo2)

grafo.addarista(arista)

grafo.findnodo(nodo1)