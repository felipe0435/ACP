# padre mayor que hijos
class Heap(object):
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio


    def get_vector(self):
        return self.vector


    def intercambio(self, a, b):
        aux = self.vector[a]
        self.vector[a] = self.vector[b]
        self.vector[b] = aux


    def flotar(self, indice):
        while indice > 0 and self.vector[indice] > self.vector[(indice - 1) // 2]:
            padre = (indice - 1) // 2
            self.intercambio(indice, padre)
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
                self.intercambio(indice, aux)
                indice = aux
                hijo_izq = (indice * 2) + 1
            else:
                control = False


    def agregar(self, dato):
        self.vector[self.tamanio] = dato
        self.flotar(self.tamanio)
        self.tamanio += 1


    def quitar(self):
        self.intercambio(0, self.tamanio - 1)
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


    def flotar_prioridad(self, indice):
        while indice > 0 and (self.vector[(indice - 1) // 2] == None or self.vector[indice][0] > self.vector[(indice - 1) // 2][0] or self.vector[indice - 1] == None):
            padre = (indice - 1) // 2
            if self.vector[indice - 1] == None:
                self.intercambio(indice, indice - 1)
                indice -= 1
            else:
                self.intercambio(indice, padre)
                indice = padre


    def hundir_prioridad(self, indice):
            hijo_izq = (indice * 2) + 1
            control = True
            while control and hijo_izq < self.tamanio:
                hijo_der = hijo_izq + 1
                aux = hijo_izq
                if hijo_der < self.tamanio:
                    if self.vector[hijo_der][0] > self.vector[hijo_izq][0]:
                        aux = hijo_der
                if self.vector[indice][0] < self.vector[aux][0]:
                    self.intercambio(indice, aux)
                    indice = aux
                    hijo_izq = (indice * 2) + 1
                else:
                    control = False


    def agregar_prioridad(self, dato):
        self.vector[self.tamanio - 1] = dato
        self.flotar_prioridad(self.tamanio - 1)
        self.tamanio += 1


    def quitar_prioridad(self):
        self.intercambio(0, self.tamanio - 1)
        dato = self.vector[self.tamanio - 1]
        self.tamanio -= 1
        self.hundir_prioridad(0)
        return dato


    def arribo(self, dato, prioridad):
        self.agregar_prioridad([prioridad, dato])


    def atencion(self):
        return self.quitar()[1]


    def cambiar_prioridad(self, indice, prioridad):
        prioridad_anterior = self[indice][0]
        self[indice][0] = prioridad
        if prioridad > prioridad_anterior:
            self.flotar(indice)
        elif prioridad < prioridad_anterior:
            self.hundir(indice)


    def heapsort_prioridad(self):
        aux = self.tamanio
        for _ in range(self.tamanio):
            self.quitar_prioridad()
        self.tamanio = aux

    # para ordenar un vector


    def monticulizar(self):
        for i in range(len(self.vector)):
            self.flotar(i)


    def HeapSort(self):
        aux = self.tamanio
        for _ in range(self.tamanio):
            self.quitar()
        self.tamanio = aux


    def HeapSort_aa(self):
        aux = self.tamanio
        for _ in range(self.tamanio):
            self.quitar_aa()
        self.tamanio = aux


    def busqueda_secu(self, elem):
        for i in range(self.tamanio):
            if elem == self.vector[i]:
                print(i)
                return i
        return None