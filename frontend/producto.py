from utils.terminal import limpiar
import backend.producto as Producto
from tabulate import tabulate

headers = ["Id", "Nombre", "Cantidad", "Precio"]


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


def actualizarProducto():
    idProducto = input("Ingrese el ID del producto que desea actualizar: ").strip()

    if Producto.consultarProducto(idProducto) is None:
        print(f"\nProducto con ID '{idProducto}' no existe.\n")
        return

    nombre = input("Ingrese el nuevo nombre: ").strip()
    cantidad = input("Ingrese la nueva cantidad: ").strip()
    precio = input("Ingrese el nuevo precio: ").strip()

    actualizado = Producto.actualizarProducto(
        idProducto,
        nombre,
        cantidad,
        precio
    )

    if actualizado:
        print(f"\nProducto con ID '{idProducto}' actualizado exitosamente.\n")
    else:
        print(f"\nError, no existe el producto con ID '{idProducto}'.\n")


def mostrarMenuDeProductos():
    separador = "------------------------------------"
    bienvenida = "TIENDA"
    opciones = {
        "1": listarProductos,
        "2": consultarProducto,
        "3": guardarProducto,
        "4": eliminarProducto,
        "5": actualizarProducto,
    }

    solicitud = "Ingrese una opción: "
    salida = False

    while not salida:
        menu = f"{bienvenida if salida == False else separador}\n1. Listar productos\n2. Buscar producto\n3.Guardar producto\n4. Eliminar producto\n5. Actualizar producto\n6. Salir\n"
        print(menu)
        opcion = input(solicitud)

        if opcion == "6":
            salida = True
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción invalida. Intente nuevamente.")
def guardarProducto():
    idProducto = input("Ingrese el ID del producto: ").strip()

    if Producto.consultarProducto(idProducto) is not None:
        print(f"\nYa existe un producto con ID '{idProducto}'.\n")
        return

    nombre = input("Ingrese el nombre: ").strip()
    cantidad = input("Ingrese la cantidad: ").strip()
    precio = input("Ingrese el precio: ").strip()

    Producto.guardarProducto(
        idProducto,
        nombre,
        cantidad,
        precio
    )

    print(f"\nProducto con ID '{idProducto}' guardado exitosamente.\n")
def eliminarProducto():
    idProducto = input("Ingrese el ID del producto a eliminar: ").strip()

    eliminado = Producto.eliminarProducto(idProducto)

    if eliminado:
        print(f"\nProducto con ID '{idProducto}' eliminado exitosamente.\n")
    else:
        print(f"\nNo existe un producto con ID '{idProducto}'.\n")