from heap import Heap

class Proteina(object):
    def __init__(self, codigo, secuencia, estructura):
        # datos
        self.codigo = codigo[0:4]
        #self.largo_secuencia = len(secuencia)
        self.secuencia = {codigo[4]: secuencia}
        self.secuencia_est = {codigo[4]: estructura}
        # Cantidad de estructuras secuendarias
        self.cant_est_alfa = 0
        self.cant_est_beta = 0
        # Frecuencias
        self.aa_mas_frecuente = 0
        self.est_dominante = 0
        self.conteo = {}
        """
        self.peso_molecular = 0
        se calcularia multiplicando por un valor fijo cada aminoacido (puede ir
        se a la mierda si es que lo hacemos con los 5900)
        """
        #self.set_largo_secuencia()
        #self.set_aa_mas_frec()
        self.set_cant_est_alfa()
        self.set_cant_est_beta()


    # Get y Set
    def set_codigo(self, codigo):
        self.codigo = codigo

    """
    def set_largo_secuencia(self):
        largo = len(self.secuencia)
        self.largo_secuencia = largo
    """

    def set_secuencia(self, codigo, secuencia, estructura):
        self.secuencia[codigo[4]] = secuencia
        self.secuencia_est[codigo[4]] = estructura


    def set_aa_mas_frec(self):
        for secuencia in self.secuencia:
            if secuencia not in self.conteo:
                dic ={}
                contador = 0
                heap = Heap(len(self.secuencia[secuencia]))
                for letra in self.secuencia[secuencia]:
                    heap.agregar(letra)
                #heap.monticulizar()
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


    def set_cant_est_alfa(self):
        cantidad = 0
        alfa = False
        for letra in self.secuencia_est:
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
        for letra in self.secuencia_est:
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


    def get_codigo(self):
        return self.codigo


    def get_secuencia(self):
        return self.secuencia

    """
        def get_largo_secuencia(self):
            return self.largo_secuencia
    """

    def get_secuencia_aa(self):
        return self.secuencia_aa


    def get_secuencia_est(self):
        return self.secuencia_est


    def get_cant_estructuras(self):
        return self.cant_est_alfa, self.cant_est_beta


    def get_aa_mas_frecuente(self):
        return self.aa_mas_frecuente


    def get_estructura_dominante(self):
        return self.est_dominante


    def get_conteo(self):
        return self.conteo


    def imprimir_proteina(self):
        txt = (f"La proteina de codigo {self.get_codigo()}, tiene la siguietes "
                "caracteristicas:\n")
        for secuencia in self.secuencia:
            txt = f"{txt}secuencia {secuencia}:\n>{self.secuencia[secuencia]}\n"
            txt = f"{txt}sst3 {secuencia}:\n>{self.secuencia_est[secuencia]}\n"
        print(txt)
