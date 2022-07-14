lst_nombre_frutas = ["Manzana", "Uva", "Mandarina", "Platano"]
lst_precio_frutas = [1200, 600, 500, 45]
lst_indice_cantidad = [[0, 0], [1, 0], [2, 0], [3, 0]]
lst_monto_frutas = [[0, 0], [1, 0], [2, 0], [3, 0]]


def mostrar_productos_comprados():
    for i in range(len(lst_indice_cantidad)):

        if lst_indice_cantidad[i][1] != 0:
            print(f"FRUTA --> {lst_nombre_frutas[lst_indice_cantidad[i][0]]} | CANTIDAD --> {lst_indice_cantidad[i][1]}"
                  f" MONTO --> {lst_monto_frutas[i][1]}")


def mostrar_menu():
    print("---- MENU ----\n" + "\n".join(f"{i}. {fruta}" for i, fruta in enumerate(lst_nombre_frutas, 1)))
    print(f"{len(lst_nombre_frutas) + 1}. Mostrar Productos")
    print(f"{len(lst_nombre_frutas) + 2}. Salir")


def comprar_proucto(opcion, aq_fruta):
    if aq_fruta.lower() == "a":
        cantidad = int(input(f"Cuantas unidades de {lst_nombre_frutas[opcion]} deseas agregar: "))
        lst_indice_cantidad[opcion][1] += cantidad
        lst_monto_frutas[opcion][1] += (cantidad * lst_precio_frutas[opcion])
    elif aq_fruta.lower() == "q":
        lst_indice_cantidad[opcion][1] = 0


def carrito_compra():
    while True:
        mostrar_menu()
        e_opcion = int(input("Elija una opción: "))
        if 1 <= e_opcion <= 4:
            e_opcion = e_opcion - 1
            agregar_quitar_producto = input(f"Desea Agregar o Quitar {lst_nombre_frutas[e_opcion]} (a - q): ")
            if agregar_quitar_producto == "a" or agregar_quitar_producto == "q":
                comprar_proucto(e_opcion, agregar_quitar_producto)
            else:
                print("Opcion no valida, vuelva a intentar")
        elif e_opcion == 5:
            mostrar_productos_comprados()
        elif e_opcion == 6:
            break
        else:
            print("Opcion no valida.")


def calcular_monto():
    monto = 0
    for i in range(len(lst_monto_frutas)):

        if lst_monto_frutas[i][1] != 0:
            monto += lst_monto_frutas[i][1]

    return monto


def main():
    tipo_tarjeta = input("Con que vas a pagar CREDITO, DEBITO, EFECTIVO (c - d - e): ")
    carrito_compra()
    monto = calcular_monto()
    if tipo_tarjeta.lower() == "c" or tipo_tarjeta.lower() == "credito":
        monto_final = monto - (monto * 0.15)
        print(f"TU DESCUENTO ES DE 15%")
        print(f"MONTO FINAL A PAGAR {monto_final}")
    elif tipo_tarjeta.lower() == "d" or tipo_tarjeta.lower() == "debito":
        monto_final = monto - (monto * 0.10)
        print(f"TU DESCUENTO ES DE 10%")
        print(f"MONTO FINAL A PAGAR {monto_final}")
    elif tipo_tarjeta.lower() == "e" or tipo_tarjeta.lower() == "efectivo":
        print(f"MONTO FINAL A PAGAR {monto}")


if __name__ == "__main__":
    main()
