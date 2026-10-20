from utils.terminal import limpiar
import backend.cliente as Cliente
from tabulate import tabulate

headers = ["Fila/ID", "Número de documento", "Nombre", "Celular", "Ciudad"]

def listarClientes():
    clientes = Cliente.listarClientes()
    # Si listarClientes() no incluye índice de fila, usa headers[1:]
    # Si la lista ya trae todas las columnas, usas headers
    print(tabulate(clientes, headers=["Número de documento", "Nombre", "Celular", "Ciudad"], tablefmt="rounded_grid"))

def consultarCliente():
    documento = input("Ingrese el documento del cliente: ").strip()
    cliente = Cliente.consultarCliente(documento)
    
    if cliente is None:
        print(f"\nCliente con documento '{documento}' no existe.\n")
        return
        
    headers = ["Número de documento", "Nombre", "Celular", "Ciudad"]
    print(tabulate([cliente[1:]], headers=headers, tablefmt="rounded_grid"))

def mostrarMenuDeClientes():
    separador = "------------------------------------"
    bienvenida = "CLIENTES"
    opciones = {
        "1": listarClientes,
        "2": consultarCliente,
    }
    
    solicitud = "Ingrese una opción: "
    salida = False

    while not salida:
        menu = f"{bienvenida if salida == False else separador}\n1. Listar clientes\n2. Buscar cliente\n3. Salir"
        print(menu)
        opcion = input(solicitud)
        print()
        
        if opcion == "3":
            salida = True
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción invalida. Intente nuevamente.")