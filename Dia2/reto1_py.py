def es_seguro(informe):
    niveles = list(map(int, informe.split()))
    n = len(niveles)

    # Verificar si los niveles están aumentando o disminuyendo gradualmente
    aumentando = all(1 <= niveles[i] - niveles[i - 1] <= 3 for i in range(1, n))
    disminuyendo = all(1 <= niveles[i - 1] - niveles[i] <= 3 for i in range(1, n))
    
    # El informe es seguro si cumple alguna de estas condiciones
    return aumentando or disminuyendo

def contar_informes_seguros(nombre_fichero):
    try:
        with open(nombre_fichero, 'r') as archivo:
            lineas = archivo.readlines()
        
        # Contar informes seguros
        return sum(es_seguro(informe.strip()) for informe in lineas)
    except FileNotFoundError:
        print(f"El fichero '{nombre_fichero}' no existe.")
        return 0

# Programa principal
if __name__ == "__main__":
    nombre_fichero = input("Introduce el nombre del fichero con los datos: ")
    cantidad_seguros = contar_informes_seguros(nombre_fichero)
    print(f"Número de informes seguros: {cantidad_seguros}")
