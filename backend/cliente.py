from backend.hoja_cliente import obtenerHojaDeClientes

def listarClientes():
    hoja = obtenerHojaDeClientes()
    filas = []

    # Recorremos todas las filas y filtramos las que están completamente vacías
    for refFila in hoja.iter_rows(min_row=2, min_col=1, max_col=4):
        valores = [celda.value for celda in refFila]
        if any(valores):
            filas.append(valores)

    return filas

def consultarCliente(documento):
    hoja = obtenerHojaDeClientes()
    refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
    
    doc_buscado = str(documento).strip()

    for idx, refFila in enumerate(refFilas, start=2):
        val_celda = refFila[0].value
        
        if val_celda is None:
            continue
            
        if str(val_celda).strip() == doc_buscado:
            valores = [idx] 
            
            for celda in refFila:
                valores.append(celda.value)

            return valores 
            
    return None 