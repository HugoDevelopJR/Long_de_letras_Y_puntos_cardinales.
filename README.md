El objetivo fue crear un programa interactivo que valide si una palabra ingresada tiene una longitud específica, utilizando las herramientas fundamentales de Python.

   1. Estructuras de Datos utilizadas:
-Tuplas (LIMITES): Se utilizó una tupla para definir los valores mínimo (4) y máximo (8). Al ser inmutable, nos asegura que los límites del programa no cambien accidentalmente durante la ejecución.

-Listas (intentos): Se empleó una lista vacía para almacenar cada palabra que el usuario escribió. Esto nos permitió llevar un registro histórico de la sesión.

   2. Control de Flujo (Lógica)
Ciclo while True: Implementamos un bucle infinito para que el programa no se cierre si el usuario comete un error. Esto garantiza una mejor experiencia de usuario.
Condicionales (if, elif, else):
-if: Verifica si la longitud está dentro del rango correcto.
-elif: Identifica si la palabra es demasiado corta.
-else: Captura el caso restante (palabra demasiado larga).
-Sentencia break: Es el "interruptor" que detiene el ciclo while únicamente cuando la validación es exitosa.

   3. Funciones y Métodos clave
-input(): Para interactuar con el usuario.
-len(): Para contar los caracteres de la cadena de texto.
-.append(): Método de listas para agregar la palabra ingresada al historial.
-f-strings: Usadas para insertar variables dentro de los mensajes de texto de forma dinámica.

   4. Resultado final
El programa no solo valida la entrada, sino que al final entrega un reporte con el total de intentos y el listado completo de las palabras probadas, demostrando cómo Python puede procesar y organizar información de manera eficiente.





Este programa fue desarrollado para identificar en qué cuadrante del plano cartesiano se encuentra un punto, a partir de dos coordenadas ingresadas por el usuario (X, Y).

🔹 1. Entrada de datos

Se utilizó la función input() para solicitar al usuario los valores de X y Y.
Estos valores se convirtieron a enteros usando int() para poder compararlos.

🔹 2. Uso de ciclo while

Se implementó un ciclo while True para repetir el proceso hasta que el usuario ingrese valores válidos.
Esto permite que el programa no termine hasta cumplir con la condición requerida.

🔹 3. Validación de datos

Se verificó que ninguna coordenada sea igual a 0 utilizando una condición:

if x == 0 or y == 0

Esto es importante porque:

Si X o Y es 0, el punto estaría sobre un eje
Y el ejercicio pide únicamente puntos dentro de cuadrantes

Si ocurre esto, el programa muestra un mensaje de error y vuelve a pedir los datos.

🔹 4. Estructuras condicionales (if)

Se utilizaron condiciones if, elif y else para determinar el cuadrante según el signo de X y Y:

(+, +) → Cuadrante I
(-, +) → Cuadrante II
(-, -) → Cuadrante III
(+, -) → Cuadrante IV

🔹 5. Salida de resultados

El programa imprime en pantalla el cuadrante correspondiente usando print().

🔹 6. Finalización del programa

Una vez que se ingresan datos válidos y se muestra el resultado, se utiliza break para salir del ciclo while y terminar la ejecución.

✅ Conclusión

El programa logra su objetivo utilizando:

Entrada de datos (input)
Validación (if)
Repetición (while)
Control de flujo (break)

Esto permite identificar correctamente el cuadrante de un punto en el plano cartesiano, asegurando que los datos ingresados sean válidos.
