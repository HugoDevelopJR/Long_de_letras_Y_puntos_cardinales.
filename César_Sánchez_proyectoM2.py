        #PROYECTO 1

    # Un saludo de bienvenida
print(" \n            VALIDADOR DE LONGITUD DE PALABRAS \n")

    # Usamos una TUPLA para definir los límites (datos que no cambian)
Limites= (4, 8) 

    # Usamos una LISTA para guardar el historial de intentos (datos que crecen)
intentos = []

while True:
    palabra = input("Ingresa una palabra: ")
    n = len(palabra)
    
    # Agregamos la palabra a nuestra lista de historial
    intentos.append(palabra)

    if Limites[0] <= n <= Limites[1]:
        print("✅ La palabra es correcta.")
        break 
    elif n < Limites[0]:
        print(f"❌ Hacen falta letras. Solo tiene {n}.")
    else:
        print(f"❌ Sobran letras. Tiene {n}.")

   # Al finalizar, mostramos el resumen
print(f"\nResumen de la sesión:")
print(f"Total de intentos: {len(intentos)}")
print(f"Lista de palabras probadas: {intentos}")


input()




      #PROYECTO 2

      #Titulo
print ("\n                   CORDENADAS DEL PLANO CARTESIANO  ")
print ("\n  Para encontrar los 4 puntos cardinales : (+,+),(-,+),(-,-),(+,-) ")

while True:
    print ("     \n Recuerda que las coordenadas pueden ser numeros               \n               positivo(+) o negativo(-) \n")
    
    
    
      # Pedir datos
    x = int(input("Ingrese Coordenada X: "))
    y = int(input("Ingrese Cordenada Y: "))

    # Validar que no sean 0
    if x == 0 or y == 0:
        print("Error: Ninguna coordenada puede ser 0. Intenta de nuevo.\n")
        continue  # vuelve a pedir datos

    # Evaluar cuadrante
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III")
    else:   # x > 0 and y < 0
        print("El punto se encuentra en el cuadrante IV")

        break    # Se termina el programa




