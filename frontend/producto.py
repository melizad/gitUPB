import backend.producto as Producto


def listarProductos():
    Producto.listarProductos()


def consultarProducto():
    idProducto = input("Ingrese el ID del producto: ").strip()
    Producto.consultarProducto(idProducto)


def mostrarMenuDeProductos():
    bienvenida = "PRODUCTOS"
    opciones = {
        "1": listarProductos,
        "2": consultarProducto,
    }

    while True:
        print(f"{bienvenida}\n1. Listar productos\n2. Buscar producto\n3. Salir")
        opcion = input("Ingrese una opción: ")
        print()

        if opcion == "3":
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción invalida. Intente nuevamente.")
