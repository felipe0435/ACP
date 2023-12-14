from heap import Heap

class Proteina(object):
    def __init__(self, codigo, secuencia, estructura):
        # datos
        self.codigo = codigo[0:4]
        self.secuencia = {codigo[4]: secuencia}
        self.secuencia_est = {codigo[4]: estructura}
        # Cantidad de estructuras secuendarias
        self.cant_est_alfa = 0
        self.cant_est_beta = 0
        # Frecuencias
        self.aa_mas_frecuente = []
        self.conteo = {}
        self.est_dominante = 0

        self.set_cant_est_alfa()
        self.set_cant_est_beta()


    # SET
    def set_codigo(self, codigo):
        self.codigo = codigo


    def set_secuencias(self, codigo, secuencia, estructura):
        self.secuencia[codigo[4]] = secuencia
        self.secuencia_est[codigo[4]] = estructura


    def set_aa_mas_frec(self):
        mayor = []
        for secuencia in self.secuencia:
            if secuencia not in self.conteo:
                dic ={}
                contador = 0
                heap = Heap(len(self.secuencia[secuencia]))
                for letra in self.secuencia[secuencia]:
                    heap.agregar(letra)
                heap.HeapSort()
                ordenado = heap.get_vector()
                actual = ordenado[0]
                for i in range(len(ordenado)):
                    if ordenado[i] == actual:
                        contador += 1
                    else:
                        dic[actual] = contador
                        actual = ordenado[i]
                        contador = 1
                self.conteo[secuencia] = dic
        existe = False
        for cadena in self.conteo:
            for aa in self.conteo[cadena]:
                (existe, indice) = self.busqueda_bin(mayor, aa,
                                                        0, len(mayor) - 1)
                if existe:
                    mayor[indice][1] += self.conteo[cadena][aa]
                else:
                    mayor.append([aa, self.conteo[cadena][aa]])
        m = ["", 0]
        for elem in mayor:
            if elem[1] > m[1]:
                m = elem[0:2]
        self.aa_mas_frecuente = m[0:2]


    def set_cant_est_alfa(self):
        cantidad = 0
        alfa = False
        for secuencia in self.secuencia_est:
            for letra in self.secuencia_est[secuencia]:
                if letra == "H" and not alfa:
                    cantidad += 1
                    alfa = True
                elif letra != "H" and alfa:
                    alfa = False
        self.cant_est_alfa = cantidad
        self.set_est_dominante()


    def set_cant_est_beta(self):
        cantidad = 0
        beta = False
        for secuencia in self.secuencia_est:
            for letra in self.secuencia_est[secuencia]:
                if letra == "E" and not beta:
                    cantidad += 1
                    beta = True
                elif letra != "E" and beta:
                    beta = False
        self.cant_est_beta = cantidad
        self.set_est_dominante()


    def set_est_dominante(self):
        if self.cant_est_alfa > self.cant_est_beta:
            self.est_dominante = "Alfa"
        if self.cant_est_beta > self.cant_est_alfa:
            self.est_dominante = "Beta"
        elif self.cant_est_alfa == self.cant_est_beta:
            self.est_dominante = "Ambas"


    # GET
    def get_codigo(self):
        return self.codigo


    def get_secuencia(self):
        return self.secuencia


    def get_secuencia_est(self):
        return self.secuencia_est


    def get_cant_estructuras(self):
        return self.cant_est_alfa, self.cant_est_beta


    def get_aa_mas_frecuente(self):
        return self.aa_mas_frecuente


    def get_est_dominante(self):
        return self.est_dominante


    def get_conteo(self):
        return self.conteo


    # Imprimir
    def imprimir_proteina_completa(self):
        txt = (f"Codigo: {self.get_codigo()}, tiene la siguietes "
                "caracteristicas:\n")
        for secuencia in self.secuencia:
            txt = (f"{txt}secuencia {secuencia}:\n"
                    f">>> {self.secuencia[secuencia]}\n")
            txt = (f"{txt}sst3 {secuencia}:\n"
                    f">>> {self.secuencia_est[secuencia]}\n")
        print(txt)


    def imprimir_proteina_resumen(self):
        txt = (f"Codigo: {self.get_codigo()}\n")
        for secuencia in self.secuencia:
            txt = (f"{txt}secuencia {secuencia}:\n"
                    f">>> {self.aa_mas_frecuente[0]}"
                    f":{self.aa_mas_frecuente[1]}\n")
            txt = (f"{txt}sst3 {secuencia}:\n"
                    f">>> {self.est_dominante}\n")
        print(txt)


    # Otros
    def busqueda_bin(self, lista, elem, izq, der):
        mitad = (der + izq) // 2
        if izq > der:
            return False, mitad
        elif elem == lista[mitad][0]:
            return True, mitad
        elif elem > lista[mitad][0]:
            return self.busqueda_bin(lista, elem, mitad + 1, der)
        elif elem < lista[mitad][0]:
            return self.busqueda_bin(lista, elem, izq, mitad - 1)
