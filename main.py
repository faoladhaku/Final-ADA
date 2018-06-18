from gng import gng
'''nodo1 = Nodo(1,[1,2],2)
nodo2 = Nodo(2,[1,2],4)

arista = Arista(nodo1,nodo2,2,2)

grafo = Grafo()
grafo.addNodo(nodo1)

grafo.addNodo(nodo2)

grafo.addArista(arista)

grafo.findNodo(nodo1)'''

topologia=[[482, 232], [257, 404], [119, 321], [268, 229], [123, 155], [186, 40], [110, 273]]

mygng = gng(topologia)


mygng.start()
