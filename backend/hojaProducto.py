from backend.excel import obtenerLibro

libro = obtenerLibro()

TITULO_HOJA = "Productos"


def inicializarHoja():
    hoja = libro.create_sheet(title=TITULO_HOJA)

    hoja.column_dimensions["A"].width = 15
    hoja.column_dimensions["B"].width = 30
    hoja.column_dimensions["C"].width = 15
    hoja.column_dimensions["D"].width = 15

    cabeceras = (
    "ID",
    "Nombre",
    "Cantidad",
    "Precio"
)

    hoja.append(cabeceras)

    return hoja


def obtenerHojaProductos():
    if TITULO_HOJA in libro.sheetnames:
        return libro[TITULO_HOJA]

    return inicializarHoja()