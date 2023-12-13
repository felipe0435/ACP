import csv
from proteina import Proteina
import random


def busqueda_bin(lista, elem, izq, der):
    mitad = (der + izq) // 2
    print("mitad:", mitad, "izq:", izq, "der:", der)
    print(lista[mitad].get_codigo())
    if izq > der:
        return None
    elif elem == lista[mitad].get_codigo():
        print("CORRECTO")
        return lista[mitad]
    elif elem > lista[mitad].get_codigo():
        return busqueda_bin(lista, elem, mitad + 1, der)
    elif elem < lista[mitad].get_codigo():
        return busqueda_bin(lista, elem, izq, mitad - 1)


def crear_lista():
    proteinas = []
    with open("PDB.csv") as tsvF:
        reader = csv.reader(tsvF)
        cont = 0
        for row in reader:
            if cont > 0:
                if (len(proteinas) > 0) and (proteinas[len(proteinas) - 1]
                                            .get_codigo() == row[1][0:4]):
                    proteinas[len(proteinas) - 1].set_secuencia(row[1],
                                                                row[2],
                                                                row[3])
                    proteinas[len(proteinas) - 1].set_aa_mas_frec()
                else:
                    proteina = Proteina(row[1], row[2], row[3])
                    proteina.set_aa_mas_frec()
                    proteinas.append(proteina)
            cont += 1
    return proteinas


def busca_codigo(proteinas):
    codigo = ""
    while len(codigo) != 4:
        print("\tIngrese acontinuacion el codigo de la proteina, de lo "
                "contrario seleccione 'x' para salir")
        codigo = input("\t> ").lower()
        if len(codigo) == 4:
            proteina = busqueda_bin(proteinas, codigo, 0, len(proteinas) - 1)
            print(proteina)
            proteina.imprimir_proteina()
            break
        elif codigo == "x":
            print("\t\tVolviendo al menu anterior")
            break
        else:
            print("Vuelva a intentarlo.")
            print("Si quiere volver presione 'x'")


def busca_tamanio(proteinas):
    opcion2 = ""
    while opcion2 != 'x':
        print("\tSeleccione alguna de las opciones por favor")
        print("\tOpciones:")
        print("\t1) Buscar proteina mas grande")
        print("\t2) Buscar proteina mas pequeña")
        print("\tx) Salir")
        opcion2 = input("\t> ").lower()
        match opcion2:
            case "1":
                print("\t>Ha seleccionado la proteina mas grande")
                opcion3 = ""
                while opcion3 != "x":
                    opcion3 = input("\t>Indiquie la cantidad de proteinas a"
                                    " buscar, sino marque 'x'")
                    if isinstance(opcion3, int):
                        if int(opcion3) > 0:
                            #Aqui va una funcion
                            opcion3 = "x"
                        else:
                            print("Ingrese un digito valido")
                    elif opcion3.lower() == "x":
                        print("\t\tVolviendo al menu anterior")
                    else:
                        print("Ingrese un valor valido")
            case "2":
                print("\t>Ha seleccionado la proteina mas pequeña")
                opcion3 = ""
                while opcion3 != "x":
                    opcion3 = input("\t>Indiquie la cantidad de proteinas a"
                                    " buscar, sino marque 'x'")
                    if isinstance(opcion3, int):
                        if int(opcion3) > 0:
                            #Aqui va una funcion
                            opcion3 = "x"
                        else:
                            print("Ingrese un digito valido")
                    elif opcion3.lower() == "x":
                        print("\t\tVolviendo al menu anterior")
                    else:
                        print("Ingrese un valor valido")
            case "x":
                print("\t\tVolviendo al menu anterior")
            case _:
                print("_______________________________\n"
                        "|¡Ingrese un valor pertinente!|\n"
                        "_______________________________")


def busca_aa(proteinas):
    AMINOACIDOS = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N",
                    "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    amino_acido = ""
    while len(amino_acido) != 1:
        print("\tIngrese acontinuacion un aminoacido en codigo de 1 letra, de "
                "lo contrario seleccione O para salir")
        amino_acido = input("\t> ").upper()
        if amino_acido in AMINOACIDOS:
            # Aqui va la funcion
            break
        elif amino_acido == "O":
            print("\t\tVolviendo al menu anterior")
            break
        else:
            print("Vuelva a intentarlo.")
            print("Si quiere volver presione 'O'")


def main():
    proteinas = crear_lista()
    indices = []
    while len(indices) < len(proteinas):
        indice = random.randint(0, len(proteinas) - 1)
        if indice not in indices:
            indices.append(indice)

    for indice in indices:
        proteina = proteinas[indice]
        proteina2 = busqueda_bin(proteinas, proteina.get_codigo(), 0, len(proteinas)- 1)
        print(proteina2)
        proteinas[1484].imprimir_proteina()
    print(len(indices))
    """
    for i in range(len(proteinas)):
    print(proteinas[i].get_conteo())
    """

    print("Hola, bienvenido a un pequeño proyecto del modulo "
            "Algoritmo y Estrucura de datos")
    opcion = ""
    while opcion != 'x':
        print("Seleccione alguna de las opciones por favor")
        print("\tOpciones:")
        print("\t1) Buscar proteina por codigo")
        print("\t2) Buscar proteinas por tamanio")
        print("\t3) Buscar proteinas con mas AA especifico")
        print("\t4) Buscar proteinas por estructura secundaria")
        print("\t5) Editar datos")
        print("\tx) Salir")
        opcion = input("\t> ").lower()

        match opcion:
            case "1":
                print("\t>Ha seleccionado busqueda por codigo")
                busca_codigo(proteinas)
            case "2":
                print("\t>Ha seleccionado busqueda por tamanio")
                busca_tamanio(proteinas)
            case "3":
                print("\t>Ha seleccionado busqueda por AA")
                busca_aa(proteinas)
            case "4":
                print("\t>Ha seleccionado busqueda por estructura")
            case "5":
                print("\t>Ha seleccionado edicion")
            case "x":
                print("\t\t정말 감사합니다. 곧 다시 오세요")
            case _:
                print("_______________________________"
                        "|¡Ingrese un valor pertinente!|"
                        "_______________________________")


if __name__ == '__main__':
    main()
