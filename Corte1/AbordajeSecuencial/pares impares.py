# este ejercicio vale 1 decima del 1 corte 
while True:
    try:
        numero = int(input("Ingrese un número"))
        if numero % 2 == 0:
                print(f'{numero} es par')
        else:
                print(f'{numero} es impar')
                
    except ValueError:
        print("Error: Por favor ingresa un numero")
    
    # preguntar si quiere ver otro numero
    continuar = input("\n¿Quieres verificar otro numero (si/no): ")
    if continuar.lower() != 'si':
        print("game over")
        break