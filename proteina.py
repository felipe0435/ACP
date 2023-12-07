class Proteina(object):
    def __init__(self):
        # datos
        self.codigo = None
        self.cadena = None
        self.largo_secuencia = 0
        # secuencias
        self.secuencia_aa = None
        self.secuencia_est = None
        # Cantidad de estructuras secuendarias
        self.cant_est_alfa = 0
        self.cant_est_beta = 0
        # Frecuencias
        self.aa_mas_frecuente = None
        self.est_dominante = None
        
        """
        self.peso_molecular = 0
        se calcularia multiplicando por un valor fijo cada aminoacido (puede ir
        se a la mierda si es que lo hacemos con los 5900)
        """
        
        # Get y Set
        def get_proteina(self):
            return self.codigo, self.cadena
        
        def get_largo_secuencia(self):
            return self.largo_secuencia
        
        def get_secuencia_aa(self):
            return self.secuencia_aa
        
        def get_secuencia_est(self):
            return self.secuencia_est
        
        def get_cant_estructuras(self):
            return self.cant_est_alfa, self.cant_est_beta
        
        def get_aa_mas_frecuente(self):
            return self.aa_mas_frecuente
        
        def get_estructura_frecuente(self):
            return self.est_dominante
        
        def set_codigo(self, codigo):
            self.codigo = codigo
        
        def set_cadena(self, cadena):
            self.cadena = cadena
        
        def set_largo_secuencia(self, largo):
            self.largo_secuencia = largo
        
        def set_secuencia_aa(self, secuencia):
            self.secuencia_aa = secuencia
        
        def set_secuencia_est(self, secuencia):
            self.secuencia_est = secuencia
        
        def set_cant_est_alfa(self, cantidad):
            self.cant_est_alfa = cantidad
            if self.cant_est_beta != 0:
                set_est_dominante()
        
        def set_cant_est_beta(self, cantidad):
            self.cant_est_beta = cantidad
            if self.cant_est_alfa != 0:
                set_est_dominante()
        
        """
        self.aa_mas_frecuente = None
        """
        
        def set_est_dominante(self):
            if self.cant_est_alfa > self.cant_est_beta:
                self.est_dominante = "Alfa"
            if self.cant_est_beta > self.cant_est_alfa:
                self.est_dominante = "Beta"
            else:
                self.est_dominante = "Ambas"
