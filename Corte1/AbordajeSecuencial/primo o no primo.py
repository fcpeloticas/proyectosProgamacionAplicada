# este ejercicio vale 1 decima del 1 corte 
while True:
    try:
        numero = int(input("Ingrese un número para saber si es primo o no.. "))
        if numero % 2 == 0:
                print(f'{numero} no es primo')
        else:
                print(f'{numero} es primo ')
                
    except ValueError:
        print("Error: Por favor ingresa un numero")
    
    # preguntar si quiere ver otro numero
    continuar = input("\n¿Quieres verificar otro numero (v/f): ")
    if continuar.lower() != 'v':
        print(" gracias por participar ")
        break