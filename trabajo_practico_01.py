"""
🧠 Trabajo Práctico: Introducción a Python
📌 Objetivo: Aprender los conceptos básicos de Python.
"""

def ejercicio_1():
    print("\n--- Ejercicio 1: Variables y datos ---")
    nombre = "Juan"
    edad = 18
    print(f"Hola, mi nombre es {nombre} y tengo {edad} años")

def ejercicio_2():
    print("\n--- Ejercicio 2: Entrada de datos ---")
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    print(f"Hola {nombre}, el año que viene tendrás {edad + 1}")

def ejercicio_3():
    print("\n--- Ejercicio 3: Operaciones matemáticas ---")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    if num2 != 0:
        print(f"División: {num1 / num2}")
    else:
        print("División: Error (división por cero)")

def ejercicio_4():
    print("\n--- Ejercicio 4: Condicionales ---")
    num = float(input("Ingrese un número: "))
    if num > 0:
        print("Es Positivo")
    elif num < 0:
        print("Es Negativo")
    else:
        print("Es Cero")

def ejercicio_5():
    print("\n--- Ejercicio 5: Edad y decisiones ---")
    edad = int(input("Ingrese su edad: "))
    if edad < 18:
        print("Sos menor de edad")
    else:
        print("Sos mayor de edad")

def ejercicio_6():
    print("\n--- Ejercicio 6: Bucles (nivel básico) ---")
    print("Números del 1 al 10:")
    for i in range(1, 11):
        print(i, end=" ")
    print() # Nueva línea al final

def ejercicio_7_bonus():
    print("\n--- Ejercicio 7: BONUS (Tabla de multiplicar) ---")
    num = int(input("Ingrese un número para ver su tabla: "))
    print(f"Tabla del {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def mostrar_menu():
    while True:
        print("\n" + "="*40)
        print("   MENÚ TRABAJO PRÁCTICO 01   ")
        print("="*40)
        print("1. Ejercicio 1: Variables y datos")
        print("2. Ejercicio 2: Entrada de datos")
        print("3. Ejercicio 3: Operaciones matemáticas")
        print("4. Ejercicio 4: Condicionales")
        print("5. Ejercicio 5: Edad y decisiones")
        print("6. Ejercicio 6: Bucles")
        print("7. Ejercicio 7: Bonus (Tabla de multiplicar)")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "6":
            ejercicio_6()
        elif opcion == "7":
            ejercicio_7_bonus()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()
