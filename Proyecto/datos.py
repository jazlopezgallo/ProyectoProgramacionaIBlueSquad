def creaciondatos():
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    vendedores = ["Julián", "Andrés", "Valentina"]
    vendedores_id_inicial = [201, 202, 203]
    vendedores_comision_inicial = [0.05, 0.05, 0.05]
    objetivo_mensual = 500000
    productos = ["Remera", "Pantalón", "Campera"]
    productos_id_inicial = [101, 102, 103]
    precios = [10000, 23333, 12000]
    matriz_vendedores = [[0 for _ in meses] for _ in range(len(vendedores))]
    matriz_productos = [[0 for _ in meses] for _ in range(len(productos))]
    return matriz_vendedores, matriz_productos, precios, vendedores, productos, meses, vendedores_id_inicial, vendedores_comision_inicial, objetivo_mensual, productos_id_inicial