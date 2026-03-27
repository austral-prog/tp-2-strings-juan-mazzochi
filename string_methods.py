def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""
    nombre_noespacios = nombre.strip()
    mennombre_noespacios = f"Strip: {nombre_noespacios}"
    print(mennombre_noespacios)
    nombre_lstrip = nombre.lstrip()
    mennombre_lstrip = f"LStrip: {nombre_lstrip}"
    print(mennombre_lstrip)
    nombre_rstrip = nombre.rstrip()
    mennombre_rstrip = f"RStrip: {nombre_rstrip}"
    print(mennombre_rstrip)
    frase_mayus = frase.upper()
    menfrase_mayus = f"Upper: {frase_mayus}"
    print(menfrase_mayus)
    frase_minus = frase.lower()
    menfrase_minus = f"Lower: {frase_minus}"
    print(menfrase_minus)
    frase_title = frase.title()
    menfrase_title = f"Title: {frase_title}"
    print(menfrase_title)
    frase_find = (frase.find("gran"))
    menfrase_find = f"Find: {frase_find}"
    print(menfrase_find)
    replace = frase.replace("programacion", "desarrollo")
    menfrase_replace = f"Replace: {replace}"
    print(menfrase_replace)
    Count = frase.count("a")
    menfrase_count = f"Count: {Count}"
    print(menfrase_count)
    haypython = "python" in frase.lower()
    menfrase_haypython = f"Contiene Python: {haypython}"
    print(menfrase_haypython)
    hayjava = "java" in frase.lower()
    menfrase_hayjava = f"Contiene Java: {hayjava}"
    print(menfrase_hayjava)
    slice = frase[:6]
    menslice = f"Slice: {slice}"
    print(menslice)
    paso = frase[:6:2]
    menpaso = f"Paso: {paso}"
    print(menpaso)
    reverso ="Python"[::-1]
    menreverso = f"Reverso: {reverso}"
    print(menreverso)
    combinar = nombre_noespacios+" "+"sabe"+" "+frase[:6]
    mencombinar = f"Formato: {combinar}"
    print(mencombinar)
    print(multilinea)
