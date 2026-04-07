class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(nodo.derecha, valor)

    # --- Método a) minimo() ---
    def minimo(self):
        actual = self.raiz

        if actual is None:
            return None

        while actual.izquierda is not None:
            actual = actual.izquierda

        return actual.valor


    # --- Método b) maximo() ---
    def maximo(self):
        actual = self.raiz

        if actual is None:
            return None

        while actual.derecha is not None:
            actual = actual.derecha

        return actual.valor


    # --- Método c) top_n(n) ---
    def top_n(self, n):
        resultado = []

        def recorrido_descendente(nodo):
            if nodo is None or len(resultado) >= n:
                return

            # derecha → raíz → izquierda
            recorrido_descendente(nodo.derecha)

            if len(resultado) < n:
                resultado.append(nodo.valor)

            recorrido_descendente(nodo.izquierda)

        recorrido_descendente(self.raiz)
        return resultado

torneo = BST()

puntos = [3200, 4100, 1800, 5000, 2700, 3900, 4600]

for p in puntos:
    torneo.insertar(p)

print("Mínimo:", torneo.minimo())
print("Máximo:", torneo.maximo())
print("Top 3:", torneo.top_n(3))