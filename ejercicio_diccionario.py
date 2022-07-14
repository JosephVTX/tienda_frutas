def dict_productos():
    # Formato dict_productos():
    # {opcion:["producto", precio, cantidad, monto]}
    return {1: ["Manzana", 240, 0, 0],
            2: ["Naranja", 200, 0, 0],
            3: ["Platano", 180, 0, 0],
            4: ["Mango", 160, 0, 0],
            5: ["Papaya", 10, 0, 0],
            6: ["Granadilla", 177, 0, 0],
            7: ["Pera", 120, 0, 0],
            8: ["Refresco", 100, 0, 0],
            9: ["Bebida", 170, 0, 0],
            10: ["Coco Rayado", 40, 0, 0]}


def mostar_menu():
    print("-------- M E N Ú --------")
    productos = dict_productos()
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {productos[i][0]} - S/. {productos[i][1]}")

    omp = len(productos) + 1  # Opcion Mostrar Productos
    osl = len(productos) + 2  # Opcion Salir
    print(f"{omp}. Mostrar Productos")
    print(f"{osl}. Salir")
    print("-------------------------")


def mpago_descuento():
    while True:
        tarjeta = input("Con que metodo de pago va comprar T. Credito, T. Debito o Efectivo (c - d - e): ")
        if tarjeta.lower() == "c":
            return 0.15
        elif tarjeta.lower() == "d":
            return 0.10
        elif tarjeta.lower() == "e":
            return 0
        else:
            print("Error vuelva a intentarlo.")


def mostrar_productos_comprados(productos_):
    for producto in productos_:
        if productos_[producto][2] != 0:
            print(f"{productos_[producto][0]} | CANTIDAD ---> {productos_[producto][2]}")


def verificar_cantidad_productos(productos_):
    cantidad = 0
    for producto in productos_:
        cantidad += productos_[producto][2]

    return cantidad


def obtener_monto(productos_):
    monto = 0

    for producto in productos_:
        monto += productos_[producto][3]
    return monto


def comprar_productos():
    descuento = mpago_descuento()
    productos = dict_productos()
    while True:
        mostar_menu()
        try:
            opcion = int(input(f"Elija una opción (1 - {len(productos) + 2}): "))
        except ValueError:
            print("Solo se permiten números.")
            continue

        if 1 <= opcion <= (len(productos)):

            aq_producto = input(f"Deseas añadir o quitar {productos[opcion][0]} (a - q): ")
            if aq_producto.lower() == "a":
                try:
                    cantidad = int(input(f"Cuantas unidades de {productos[opcion][0]} deseas agregar: "))
                    productos[opcion][2] = productos[opcion][2] + cantidad
                    productos[opcion][3] = productos[opcion][3] + (cantidad * productos[opcion][1])
                except ValueError:
                    print("Solo se permiten números.")
                    continue
            elif aq_producto.lower() == "q":
                productos[opcion][2] = 0
                productos[opcion][3] = 0
                print(f"SE ELIMINO {productos[opcion][0]} de tu carrito.")
            else:
                print("OPCION NO VALIDA.")
        elif opcion == (len(productos) + 1):
            print("---- SUS PRODUCTOS ----")
            if verificar_cantidad_productos(productos) != 0:
                mostrar_productos_comprados(productos)
            else:
                print("No tienes ningun producto, por favor agrega productos.")

        elif opcion == (len(productos) + 2):

            print("\n---- TOTAL A PAGAR ----\n")
            print(f"SUS PRODUCTOS: \n")
            mostrar_productos_comprados(productos)
            monto = obtener_monto(productos)
            total_pagar = monto - (monto * descuento)
            print(f"\nS/. {total_pagar}")
            # print(productos)
            break
        else:
            print("OPCION NO VALIDA")


if __name__ == "__main__":

    try:
        comprar_productos()
    except Exception as e:
        print(e)
        print("\nUPS!, AL PARECER UNOS PARAMETROS ESTAN MAL.\n")
        print("Lo mas probable es que el error sea de tu funcion dict_productos.")
