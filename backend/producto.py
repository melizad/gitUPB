from backend.hojaProducto import obtenerHojaProductos


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


def consultarProducto(idProducto):
    hoja = obtenerHojaProductos()

    for fila in hoja.iter_rows(
        min_row=2,
        max_row=hoja.max_row,
        min_col=1,
        max_col=4
    ):
        if str(fila[0].value) == str(idProducto):

            valores = []

            for celda in fila:
                valores.append(celda.value)

            return valores

    return None