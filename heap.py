# padre mayor que hijos
class Heap(object):
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio


    def get_vector(self):
        return self.vector


    def intercambio(self, vector, a, b):
        aux = vector[a]
        vector[a] = vector[b]
        vector[b] = aux


    def flotar(self, indice):
        while indice > 0 and self.vector[indice] > self.vector[(indice - 1) // 2]:
            padre = (indice - 1) // 2
            self.intercambio(self.vector, indice, padre)
            indice = padre


    def hundir(self, indice):
        hijo_izq = (indice * 2) + 1
        control = True
        while control and hijo_izq < self.tamanio:
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if hijo_der < self.tamanio:
                if self.vector[hijo_der] > self.vector[hijo_izq]:
                    aux = hijo_der

            if self.vector[indice] < self.vector[aux]:
                self.intercambio(self.vector, indice, aux)
                indice = aux
                hijo_izq = (indice * 2) + 1
            else:
                control = False


    def agregar(self, dato):
        self.vector[self.tamanio] = dato
        self.flotar(self.tamanio)
        self.tamanio += 1


    def quitar(self):
        self.intercambio(self.vector, 0, self.tamanio - 1)
        dato = self.vector[self.tamanio - 1]
        self.tamanio -= 1
        self.hundir(0)
        return dato


    def cantidad_elementos(self):
        return self.tamanio


    def heap_vacio(self):
        return self.tamanio == 0


    def heap_lleno(self):
        return self.tamanio == len(self.vector)


    def monticulizar(self):
        for i in range(len(self.vector)):
            self.flotar(i)


    # para colas con prioridad


    def arribo(self, dato, prioridad):
        self.agregar([prioridad, dato])


    def atencion(self):
        return self.quitar()[1]


    def cambiar_prioridad(self, indice, prioridad):
        prioridad_anterior = self[indice][0]
        self[indice][0] = prioridad
        if prioridad > prioridad_anterior:
            self.flotar(indice)
        elif prioridad < prioridad_anterior:
            self.hundir(indice)


    # para ordenar un vector


    def monticulizar(self):
        for i in range(len(self.vector)):
            self.flotar(i)


    def HeapSort(self):
        aux = self.tamanio
        for _ in range(self.tamanio):
            self.quitar()
        self.tamanio = aux


    def busqueda_secu(self, elem):
        for i in range(self.tamanio):
            if elem == self.vector[i]:
                print(i)
                return i
        return None