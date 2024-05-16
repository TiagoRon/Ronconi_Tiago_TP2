from pila import Stack

episodio_v = ["Luke Skywalker","Princesa leia Organa","Han Solo","Darth Vader","Yoda","Finn","Rey Skywalker"]
episodio_vii = ["Rey Skywalker","Finn","Poe dameron","Han Solo","Capital Phasma","Luke Skywalker"]

interseccion = Stack()

for personajes in episodio_v:
    if personajes in episodio_vii:
        interseccion.push(personajes)

print("Personajes en ambos episodios:")
while interseccion.size() > 0:
    print(interseccion.pop())


