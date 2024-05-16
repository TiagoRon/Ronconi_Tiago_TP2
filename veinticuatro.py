from pila import Stack

pila = Stack()

def crear_pila(personajes):
    for nombre, peliculas in personajes.items():
        pila.push((nombre, peliculas))
    return pila

def encontrar_posicion(pila, personaje_buscado):
    posicion = None
    temp_stack = Stack()

    while pila.size() > 0:
        datos = pila.pop()
        nombre = datos[0]
        temp_stack.push(datos)
        if nombre == personaje_buscado:
            posicion = temp_stack.size()
            break

    while temp_stack.size() > 0:
        pila.push(temp_stack.pop())

    return posicion

def personajes_mas_peliculas(pila):
    personajes_con_mas_peliculas = []
    temp_stack = Stack()

    while pila.size() > 0:
        personaje = pila.pop()
        temp_stack.push(personaje)

        if isinstance(personaje, tuple) and len(personaje) == 2:
            nombre, peliculas = personaje
            if peliculas > 5:
                personajes_con_mas_peliculas.append((nombre, peliculas))

    while temp_stack.size() > 0:
        pila.push(temp_stack.pop())

    return personajes_con_mas_peliculas


personajes = {
    "Iron Man": 9,
    "Thor": 4,
    "Rocket Raccoon": 5,
    "Black Widow": 6,
    "Groot": 4,
}

pj_abcd = []

for personaje in personajes:
    if personaje.startswith("C") or personaje.startswith("D") or personaje.startswith("G"):
        pj_abcd.append(personaje)
    if personaje == "Black Widow":
        print(f"Black Widow participo en {personajes['Black Widow']} peliculas")

pila_personajes = crear_pila(personajes)

posicion_rocket = encontrar_posicion(pila_personajes, "Rocket Raccoon")
posicion_groot = encontrar_posicion(pila_personajes, "Groot")


print(f"Rocket Raccoon está en la posición {posicion_rocket}")
print(f"Groot está en la posición {posicion_groot}")


personajes_con_mas_de_cinco_peliculas = personajes_mas_peliculas(pila_personajes)
print(f"Los personajes con más de 5 películas son: {personajes_con_mas_de_cinco_peliculas}")

print("Personajes que empiezan con C,D O G:")
print(pj_abcd)
