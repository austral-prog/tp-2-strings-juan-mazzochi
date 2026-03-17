def change():
    gasto = float(input("Ingresar gasto:\n"))
    dinero_recibido = int(input("Dinero recibido\n"))

    vuelto = dinero_recibido - gasto

    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
