def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    menpalabra = f"Palabra: {palabra}"
    print(menpalabra)
    longitud = len(palabra)
    menlongitud = f"Longitud: {longitud}"
    print(menlongitud)
    pletra = palabra[0]
    menpletra = f"Primera Letra: {pletra}"
    print(menpletra)
    uletra = palabra[-1]
    menuletra = f"Ultima Letra: {uletra}"
    print(menuletra)
    repetido = palabra[:]*3
    menrepetido = f"Repetida: {repetido}"
    print(menrepetido)
    decoracion = "***"+palabra+"***"
    mendecoracion = f"Decoracion: {decoracion}"
    print(mendecoracion)
