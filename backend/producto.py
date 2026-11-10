from backend.hojaProducto import obtenerHojaProductos
from backend.excel import guardar


def listarProductos():
    hoja = obtenerHojaProductos()

    filas = []

    for fila in hoja.iter_rows(
        min_row=2,
        max_row=hoja.max_row,
        min_col=1,
        max_col=4
    ):
        valores = []

        for celda in fila:
            valores.append(celda.value)

        filas.append(valores)

    return filas


def consultarProducto(idProducto, soloValores=True):
    hoja = obtenerHojaProductos()

    filas = hoja.iter_rows(
        min_row=2,
        max_row=hoja.max_row,
        min_col=1,
        max_col=4
    )

    for idx, fila in enumerate(filas):
        if str(fila[0].value) == str(idProducto):
            if soloValores:
                valores = [idx]

                for celda in fila:
                    valores.append(celda.value)

                return valores
            else:
                return fila

    return None


def actualizarProducto(idProducto, nombre, cantidad, precio):
    hoja = obtenerHojaProductos()
    nuevos_valores = (idProducto, nombre, cantidad, precio)
    refFila = consultarProducto(idProducto, False)

    if refFila is None:
        return False

    for celda, nuevo_valor in zip(refFila, nuevos_valores):
        celda.value = nuevo_valor

    guardar(hoja)
    return True