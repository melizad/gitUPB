from frontend.cliente import mostrarMenuDeClientes
from frontend.producto import mostrarMenuDeProductos


def mostrarMenuPrincipal():
    opciones = {
        "1": mostrarMenuDeClientes,
        "2": mostrarMenuDeProductos,
    }

    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Módulo de clientes")
        print("2. Módulo de productos")
        print("3. Salir")

        opcion = input("Ingrese una opción: ").strip()
        print()

        if opcion == "3":
            print("Hasta luego.")
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    mostrarMenuPrincipal()
