from collections import deque

metro = {
    "Portal Norte":   ["Toberín"],
    "Toberín":        ["Portal Norte", "Calle 142"],
    "Calle 142":      ["Toberín", "Calle 127"],
    "Calle 127":      ["Calle 142", "Pepe Sierra", "Alcalá"],
    "Pepe Sierra":    ["Calle 127", "Niza"],
    "Alcalá":         ["Calle 127", "Calle 100"],
    "Niza":           ["Pepe Sierra", "Calle 100"],
    "Calle 100":      ["Alcalá", "Niza", "Virrey"],
    "Virrey":         ["Calle 100", "Centro"],
    "Centro":         ["Virrey", "Portal Sur"],
    "Portal Sur":     ["Centro"],
}

def ruta_minima(grafo, origen, destino):
    cola = deque([[origen]])  # cada elemento es un camino completo
    visitados = set()

    while cola:
        camino = cola.popleft()
        nodo_actual = camino[-1]

        if nodo_actual == destino:
            return camino

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    nuevo_camino = camino + [vecino]
                    cola.append(nuevo_camino)

    return None

print(ruta_minima(metro, "Portal Norte", "Centro"))