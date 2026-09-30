def creaciondb():
    meses= ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    vendedores = ["Julián", "Andrés", "Valentina"]
    productos = ["Remera", "Pantalón", "Campera"]
    precios =[10000,23333,12000]

    matriz_vendedores = [[0 for columna in range(12)] for fila in range(len(vendedores))]
    matriz_productos = [[0 for columna in range(12)] for fila in range(len(productos))]

    return matriz_vendedores, matriz_productos, precios, vendedores,productos

