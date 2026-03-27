def slice_simple():
    """Dado el texto 'Awesome', imprime distintos substrings
    usando slicing y lower().
    """
    texto = "Awesome"
    textomin = texto.lower()
    print(textomin[ :3])
    print(textomin[2:5])
    print(textomin)
