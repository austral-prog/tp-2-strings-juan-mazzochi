def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    nombre = input("Ingrese nombre completo: ")
    mail = input("Ingrese email: ")
    nota1 = int(input("Ingrese nota 1: "))
    nota2 = int(input("Ingrese nota 2: "))
    nota3 = int(input("Ingrese nota 3: "))
    print("""========================
    FICHA DEL ALUMNO
========================""")
    nombre = nombre.title()
    nombre = nombre.strip()
    mennombre = f"Nombre: {nombre}"
    mail = mail.lower()
    mail = mail.strip()
    menemail = f"Email: {mail}"
    print(mennombre)
    print(menemail)
    caracteres = len(nombre)
    mencaracteres = f"Caracteres: {caracteres}"
    print(mencaracteres)
    #iniciales = nombre.find          #falta
    espacio = nombre.find(" ")
    iniciales = nombre[0] + nombre[espacio + 1]
    print(f"Iniciales: {iniciales}")
    #usuario =                         #falta
    nombre_lower = nombre.lower()
    apellido = nombre_lower[espacio + 1:]
    nombre_solo = nombre_lower[:espacio]
    usuario = apellido + "." + nombre_solo
    print(f"Usuario: {usuario}")
    arroba = "@" in mail
    menarroba = f"Email Valido : {arroba}"
    print(menarroba)
    #dominio
    pos_arroba = mail.find("@")
    dominio = mail[pos_arroba + 1:]
    print(f"Dominio: {dominio}")
    #nombre de archivo
    nombre_archivo = nombre.replace(" ", "_")
    print(f"Nombre para archivo: {nombre_archivo}")
    cant_a = nombre.count("a")
    menas = f"Cantidad de as: {cant_a}"
    print(menas)
    codigo = nombre.upper()[::-1]
    mencodigo = f"Codigo secreto: {codigo}"
    print(mencodigo)
    mennota1 = f"Nota 1: {nota1}"
    print(mennota1)
    mennota2 = f"Nota 2: {nota2}"
    print(mennota2)
    mennota3 = f"Nota 3: {nota3}"
    print(mennota3)
    suma = nota1 + nota2 + nota3
    mensuma = f"Suma: {suma}"
    print(mensuma)
    promedio = suma / 3
    menpromedio = f"Promedio: {promedio}"
    print(menpromedio)
    prom_entero = int(promedio)
    print(f"Promedio entero: {prom_entero}")
    print("========================")
