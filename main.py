import csv
from proteina import Proteina



def main():
    proteinas = []
    with open("PDB.csv") as tsvF:
        for i in range(5878):
            reader = csv.reader(tsvF)
            linea = next(reader)
            if i > 0:
                proteina = Proteina(linea[1], linea[2], linea[3])
                proteina.set_largo_secuencia()
                proteina.set_aa_mas_frec()
                proteina.set_cant_est_alfa()
                proteina.set_cant_est_beta()
                proteinas.append(proteina)

    for i in range(5877):
        print(proteinas[i].get_conteo())


if __name__ == '__main__':
    main()