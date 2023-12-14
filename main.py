import csv
from heap import Heap
from proteina import Proteina


def busqueda_bin(lista, elem, izq, der):
    mitad = (der + izq) // 2
    if izq > der:
        return None
    elif elem == lista[mitad].get_codigo():
        return mitad
    elif elem > lista[mitad].get_codigo():
        return busqueda_bin(lista, elem, mitad + 1, der)
    elif elem < lista[mitad].get_codigo():
        return busqueda_bin(lista, elem, izq, mitad - 1)


def ordenar(proteinas):
    heap = Heap(len(proteinas))
    for proteina in proteinas:
        heap.arribo(proteina, proteina.get_codigo())
    heap.heapsort_prioridad()
    for i in range(len(heap.get_vector())):
        proteinas[i] = heap.get_vector()[i][1]


def crear_lista():
    # Lista de proteinas
    proteinas = []
    # Abre el archivo
    with open("PDB.csv") as tsvF:
        reader = csv.reader(tsvF)
        cont = 0
        for row in reader:
            if cont > 0:
                if (len(proteinas) > 0) and (proteinas[len(proteinas) - 1]
                                            .get_codigo() == row[1][0:4]):
                    proteinas[len(proteinas) - 1].set_secuencias(row[1],
                                                                row[2],
                                                                row[3])
                    proteinas[len(proteinas) - 1].set_aa_mas_frec()
                    proteinas[len(proteinas) - 1].set_cant_est_alfa()
                    proteinas[len(proteinas) - 1].set_cant_est_beta()
                else:
                    # Genera el objeto y lo añande a la lista
                    proteina = Proteina(row[1], row[2], row[3])
                    proteina.set_aa_mas_frec()
                    proteina.set_cant_est_alfa()
                    proteina.set_cant_est_beta()
                    proteinas.append(proteina)
            cont += 1
    return proteinas


def agregar(proteinas):
    # Datos iniciales
    AMINOACIDOS = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N",
                    "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    # Mencion del codigo de la proteina a agregar
    codigo = ""
    while len(codigo) != 4:
        print("\tIngrese acontinuacion un codigo de 4 caracteres, de los "
                "cuales el primero debe ser un numero")
        codigo = input("\t> ").lower()
        if len(codigo) == 4:
            indice = busqueda_bin(proteinas, codigo, 0, len(proteinas) - 1)
            if not codigo[0].isnumeric():
                print("\tEste codigo no es aceptable, coloque un numero en "
                        "en el primer caracter")
            elif busqueda_bin(proteinas, codigo, 0, len(proteinas) - 1) == None:
                print("\tSe ha guardado el codigo. "
                        "Se creara una nueva proteina")
                # Mencion de la cadena a crear
                cadena = ""
                while cadena.isnumeric() or len(cadena) != 1:
                    print("\tIngrese acontinuacion un una letra, la cual hace "
                            "refencia a cadena de la proteina")
                    cadena = input("\t> ").upper()
                    if not cadena.isnumeric():
                        print("\tSe ha guardado la cadena")
                        break
                    else:
                        print("\tVuelva a intentarlo.")
                break
            else:
                # Mencion de la cadena a crear
                cadena = ""
                while cadena.isnumeric() or len(cadena) != 1:
                    print("\tIngrese acontinuacion un una letra, la cual hace "
                            "refencia a cadena de la proteina")
                    cadena = input("\t> ").upper()
                    if not cadena.isnumeric() or len(cadena) != 1:
                        existe = False
                        indice = busqueda_bin(proteinas, codigo, 0,
                                                len(proteinas) - 1)
                        for letra_cadena in proteinas[indice].get_secuencia():
                            if letra_cadena == cadena:
                                existe = True
                        if not existe:
                            print("\tSe a guardado la cadena. Se añadira a la "
                                    "proteina")
                            break
                        else:
                            print("\tSu cadena en la proteina ya existe, "
                                    "elija un caracter distinto")
                    else:
                        print("\tVuelva a intentarlo.")
        else:
            print("\tEste código no tiene 4 dígitos, "
                    "por favor ingrese otro.")
        codigo = ""
    # Mencion de la secuencia a agregar
    secuencia = ""
    correcto = True
    while secuencia not in AMINOACIDOS:
        print("\tIngrese acontinuacion el secuencia de la proteina que quiere "
                "ingresar")
        secuencia = input("\t> ").upper()
        for letra in secuencia:
            if letra not in AMINOACIDOS:
                correcto = False
                break
        if correcto:
            print("\tSe a guardado la secuencia.")
            break
        else:
            print("\tVuelva a intentarlo.")
        secuencia = ""
    # Mencion de la estrctura que tomara la secuencia de la proteina
    estructura = ""
    correcto = True
    while estructura not in ["C", "E", "H"]:
        print("\tIngrese acontinuacion el estructura de la proteina que quiere "
                "ingresar")
        estructura = input("\t> ").upper()
        for letra in estructura:
            if letra not in ["C", "E", "H"]:
                correcto = False
                break
        if correcto and len(estructura) == len(secuencia):
            print("\tSe a guardado la estructura.")
            break
        else:
            print("\tVuelva a intentarlo. Puede que la longitud de la "
                    "estructura sea distinta a la de la secuencia")
        estructura = ""
    # creacion del objeto y agregado al la lista
    codigo = f"{codigo}{cadena}"
    new_proteina = Proteina(codigo, secuencia, estructura)
    proteinas.append(new_proteina)

def editar(proteinas):
    codigo = ""
    while len(codigo) != 4:
        print("\tIngrese acontinuacion el codigo de PDB, de la proteina que "
                "desea modificar:")
        codigo = input("\t> ").lower()
        if len(codigo) == 4:
            if not codigo[0].isnumeric():
                print("\tEste codigo no es aceptable, coloque un numero en "
                        "en el primer caracter")
            elif busqueda_bin(proteinas, codigo,
                                0, len(proteinas) - 1) == None:
                print("\tEste código no existe, vuelva a intentarlo.")
            else:
                indice = busqueda_bin(proteinas, codigo, 0, len(proteinas) - 1)
                print("\tCodigo aceptado")
            break
        else:
            print("\tEste código no tiene 4 dígitos, "
                    "por favor ingrese otro.")
        codigo = ""
    opcion3 = ""
    # Menu 3
    while opcion3 != 'x':
        print("\tSeleccione alguna de las opciones por favor")
        print("\tOpciones a editar:")
        print("\t1) Codigo")
        print("\tx) Salir")
        opcion3 = input("\t> ").lower()
        # Seleccion del menu
        match opcion3:
            case "1":
                print("\tHa seleccionado codigo\n")
                proteinas[indice].set_codigo(codigo)
                proteinas[indice].imprimir_proteina_resumen()
                ordenar(proteinas)
                break
            case "x":
                print("\t\tVolviendo al menu anterior\n")
                break
            case _:
                print("_______________________________\n"
                        "|¡Ingrese un valor pertinente!|\n"
                        "_______________________________\n")


def busca_codigo(proteinas, eliminar):
    codigo = ""
    # Bandera para que se busque solo codigos de 4 caracteres
    while len(codigo) != 4:
        print("\tIngrese acontinuacion el codigo de la proteina que busca, "
                "de lo contrario seleccione 'x' para salir")
        codigo = input("\t> ").lower()
        # Codigo valido
        if len(codigo) == 4:
            indice = busqueda_bin(proteinas, codigo, 0, len(proteinas) - 1)
            # Se revisa si la proteina existe
            if busqueda_bin(proteinas, codigo, 0, len(proteinas) - 1) != None:
                # Dependiendo de la funcion elegida antes se decide si se
                # elimina o muestra la proteina buscada
                if eliminar:
                    print("\t¿Desea eliminar la siguiente proteína? s/n")
                    proteinas[indice].imprimir_proteina_completa()
                    respuesta = ""
                    while len(respuesta) != 1:
                        respuesta = input("> ").lower()
                        if respuesta == 's':
                            proteinas.pop(indice)
                            break
                        elif respuesta == 'n':
                            break
                        else:
                            print("\tCaracter inválido, por favor ingrese "
                                    "s(si) o n(no).")
                else:
                    print("\tLa proteina que busco es:")
                    proteinas[indice].imprimir_proteina_completa()
                break
            else:
                print("\tEste código no se encuentra en la base de datos, "
                        "por favor ingrese otro.")
        # Salida
        elif codigo == "x":
            print("\t\tVolviendo al menu anterior")
            break
        # Otro intento
        else:
            print("\tVuelva a intentarlo.")



def busca_aa(proteinas, respuestas):
    AMINOACIDOS = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N",
                    "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    amino_acido = ""
    # Bandera para que solo ingrese 1 caracter
    while len(amino_acido) != 1:
        print("\tIngrese acontinuacion un aminoacido en codigo de 1 letra, de "
                "lo contrario seleccione 0 para salir\n\tLas opciones son: A, "
                "C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z")
        amino_acido = input("\t> ").upper()
        # Aminoacido valido
        if amino_acido in AMINOACIDOS and len(respuestas) == 0:
            heap = Heap(len(proteinas))
            for proteina in proteinas:
                heap.arribo(proteina, proteina.get_aa_mas_frecuente()[0])
            heap.heapsort_prioridad()
            for elem in heap.get_vector():
                if elem[0] == amino_acido:
                    respuestas.append(elem[1])
                elif (elem[0] != amino_acido and len(respuestas) > 0):
                    break
            break
        elif amino_acido in AMINOACIDOS and len(respuestas) > 0:
            heap = Heap(len(respuestas))
            for proteina in respuestas:
                heap.arribo(proteina, proteina.get_aa_mas_frecuente()[0])
            heap.heapsort_prioridad()
            respuestas = []
            for elem in heap.get_vector():
                if elem[0] == amino_acido:
                    respuestas.append(elem[1])
                elif (elem[0] != amino_acido and len(respuestas) > 0):
                    break
            if len(respuestas) == 0:
                respuestas = heap.get_vector()[0:len(heap.get_vector())]
            break
        # Salida
        elif amino_acido == "0":
            print("\t\tVolviendo al menu anterior")
            break
        # Otro intento
        else:
            print("\tVuelva a intentarlo.")
    return respuestas


def filtrar(proteinas):
    opcion = ""
    respuestas = []
    while opcion != 'x':
        print("\tSeleccione alguna de las opciones por favor")
        print("\tOpciones:")
        print("\t1) Filtrar según el aa más común")
        print("\t2) Filtrar según la estructura secundaria más común")
        print("\t3) Mostrar resultados")
        print("\t4) Borrar filtros")
        print("\tx) Salir")
        opcion = input("\t> ").lower()
        match opcion:
            case '1':
                respuestas = busca_aa(proteinas, respuestas)
            case '2':
                respuestas = busca_est(proteinas, respuestas)
            case '3':
                for respuesta in respuestas:
                    respuesta.imprimir_proteina_resumen()
            case '4':
                respuestas = []
            case 'x':
                pass
            case '_':
                print("\n_______________________________\n"
                        "|¡Ingrese un valor pertinente!|\n"
                        "_______________________________\n")

    # Datos iniciales


def busca_est(proteinas, respuestas):
    opcion2 = ""
    # Menu 2
    while opcion2 != 'x':
        print("\tSeleccione alguna de las opciones por favor")
        print("\tOpciones:")
        print("\t1) Buscar proteina con mas alfa helices")
        print("\t2) Buscar proteina con mas laminas beta")
        print("\t3) Buscar proteina con ambas estrucuras")
        print("\tx) Salir")
        opcion2 = input("\t> ").lower()
        # Seleccion del menu
        match opcion2:
            case "1":
                print("\t>Ha seleccionado buscar las proteinas con mas "
                        "alfa helices")
                respuestas = determinar_estructura(proteinas,"Alfa", respuestas)
                break
            case "2":
                print("\t>Ha seleccionado buscar las proteinas con mas "
                        "laminas beta")
                respuestas = determinar_estructura(proteinas,"Beta", respuestas)
                break
            case "3":
                print("\t>Ha seleccionado buscar las proteinas con la misma "
                        "cantidad de alfa helices y laminas beta")
                respuestas = determinar_estructura(proteinas, "Ambas", respuestas)
                break
            case "x":
                print("\t\tVolviendo al menu anterior")
                break
            case _:
                print("\n_______________________________\n"
                        "|¡Ingrese un valor pertinente!|\n"
                        "_______________________________\n")
    return respuestas


def determinar_estructura(proteinas, estructura, respuestas):
    if len(respuestas) == 0:
        heap = Heap(len(proteinas))
        for proteina in proteinas:
            heap.arribo(proteina, proteina.get_est_dominante())
        heap.heapsort_prioridad()
        for elem in heap.get_vector():
            if elem[0] == estructura:
                respuestas.append(elem[1])
            elif (elem[0] != estructura and len(respuestas) > 0):
                break
    if len(respuestas) > 0:
        heap = Heap(len(respuestas))
        for proteina in respuestas:
            heap.arribo(proteina, proteina.get_est_dominante())
        heap.heapsort_prioridad()
        respuestas = []
        for elem in heap.get_vector():
            if elem[0] == estructura:
                respuestas.append(elem[1])
            elif (elem[0] != estructura and len(respuestas) > 0):
                break
    return respuestas


def edicion(proteinas):
    opcion2 = ""
    # Menu 2
    while opcion2 != 'x':
        print("\tSeleccione alguna de las opciones por favor")
        print("\tOpciones:")
        print("\t1) Agregar")
        print("\t2) Eliminar")
        print("\t3) Editar")
        print("\tx) Salir")
        opcion2 = input("\t> ").lower()
        # Seleccion del menu
        match opcion2:
            case "1":
                print("\tHa seleccionado agregar\n")
                agregar(proteinas)
                print(f"Se ha agregardo la proteina "
                        f"{proteinas[len(proteinas)- 1].
                        imprimir_proteina_completa()}")
                ordenar(proteinas)
                for proteina in proteinas:
                    print(proteina.get_codigo())
                break
            case "2":
                print("\tHa seleccionado eliminar\n")
                busca_codigo(proteinas, True)
                break
            case "3":
                print("\tHa seleccionado editar\n")
                editar(proteinas)
                ordenar(proteinas)
                break
            case "x":
                print("\t\tVolviendo al menu anterior\n")
                break
            case _:
                print("_______________________________\n"
                        "|¡Ingrese un valor pertinente!|\n"
                        "_______________________________\n")


def main():
    # Generacion de lista
    proteinas = crear_lista()
    # Menu
    print("Hola, bienvenido a un pequeño proyecto del modulo "
            "Algoritmo y Estrucura de datos")
    opcion = ""
    while opcion != 'x':
        print("Seleccione alguna de las opciones por favor")
        print("\tOpciones:")
        print("\t1) Buscar proteina por codigo")
        print("\t2) Aplicar filtros de búsquda")
        print("\t3) Editar datos")
        print("\tx) Salir")
        opcion = input("\t> ").lower()
        # Seleccion del menu
        match opcion:
            case "1":
                print("\tHa seleccionado busqueda por codigo")
                busca_codigo(proteinas, False)
            case "2":
                print("\tHa seleccionado busqueda por AA")
                filtrar(proteinas)
            case "3":
                print("\tHa seleccionado edicion")
                edicion(proteinas)
            case "x":
                print("\t\tAdiós, vuelva pronto")
            case _:
                print("\n_______________________________\n"
                        "|¡Ingrese un valor pertinente!|\n"
                        "_______________________________\n")


def prueba():
    for i in range(10):
        pass


if __name__ == '__main__':
    main()
