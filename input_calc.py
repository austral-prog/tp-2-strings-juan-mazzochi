def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = int(input("Base: "))
    altura = int(input("Altura: "))
    mbase = f"Base: {base}"
    print(mbase)
    maltura = f"Altura: {altura}"
    print(maltura)
    area = f"Area: {base * altura}"
    print(area)
    perimetro = f"Perimetro: {(base + altura)*2}"
    print(perimetro)
