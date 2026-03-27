def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input("Ingrese nombre: ")
    nombremin = nombre.lower()
    tienea = "a" in nombremin
    mensajea = f"Tiene a: {tienea}"
    print(mensajea)
    tienee = "e" in nombremin
    mensajee = f"Tiene e: {tienee}"
    print(mensajee)
    tienei = "i" in nombremin
    mensajei = f"Tiene i: {tienei}"
    print(mensajei)
    tieneo = "o" in nombremin
    mensajeo = f"Tiene o: {tieneo}"
    print(mensajeo)
    tieneu = "u" in nombremin
    mensajeu = f"Tiene u: {tieneu}"
    print(mensajeu)
