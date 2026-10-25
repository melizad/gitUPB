from utils.terminal import limpiar
import backend.producto as Producto
from tabulate import tabulate

headers = ["Id", "Nombre", "Precio", "Cantidad"]


def listarProductos():
    productos = Producto.listarProductos()
    print(tabulate(productos, headers=headers, tablefmt="rounded_grid"))


def consultarProducto():
    idProducto = input("Ingrese el ID del producto: ").strip()
    producto = Producto.consultarProducto(idProducto)

    if producto is None:
        print(f"\nProducto con ID '{idProducto}' no existe.\n")
        return

    print(tabulate([producto[1:]], headers=headers, tablefmt="rounded_grid"))


def mostrarMenuDeProductos():
    separador = "------------------------------------"
    bienvenida = "TIENDA"
    opciones = {
        "1": listarProductos,
        "2": consultarProducto,
    }

    solicitud = "Ingrese una opción: "
    salida = False

    while not salida:
        menu = f"{bienvenida if salida == False else separador}\n1. Listar productos\n2. Buscar producto\n3. Salir\n"
        print(menu)
        opcion = input(solicitud)

        if opcion == "3":
            salida = True
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción invalida. Intente nuevamente.")
