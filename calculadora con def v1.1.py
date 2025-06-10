import time
# MENU DE CALCULADORA 
    #METODOS DEF
    #VALIDACIONES CON TRY EXCEPT
    #CICLOS DE REPETICION
    #MENU ITERATIVO


#CREACION DE FUNCIONES DEF

#metodo def que recibe dos argumentos, num1 y num2
def sumar(num1,num2):
    resultado_suma = num1 + num2
    return(resultado_suma)

#metodo def para restar numeros
def restar(num1, num2):
    resultado_resta = num1 - num2
    return(resultado_resta)
#metodo def para dividir numeros
def division(num1,num2):
    try:
        resultado_division = num1 / num2
        return(resultado_division)
    except ZeroDivisionError:
        print('Error: no se puede dividir por cero.')
        time.sleep(3)

def multiplicar(num1,num2):
    resultado_multiplicacion = num1 * num2
    return(resultado_multiplicacion)

def mostrar_menu():
    print('=========================================================')
    print('Menu de calculadora en python')
    print('=========================================================')
    print('1.- Sumar.')
    print('2.- Restar.')
    print('3.- Multiplicar.')
    print('4.- Dividir.')
    print('5.- Salir.')

def obtener_numeros():
    while True:
        try:
            num1 = int(input('Ingrese el primer numero a operar: '))
            num2 = int(input('Ingrese el segundo numero a operar: '))
            return num1,num2
        except ValueError:
            print('Error, por favor ingrese numeros validos.')

def main():

    #ciclo para repetir menu
    while True:
        #llamar a funcion mostrar menu
        mostrar_menu()

        #menu de opciones segun el numero ingresado

        #ingresar una opcion
        try:
            op = int(input('\nPor favor, ingrese una opcion de 1 a 5: '))
        except ValueError:
            print('Error, ha ingresado un valor no numerico.')
            time.sleep(3)
        
        #validar que el numero ingresado sea una opcion de 1 a 5
        if op < 1 or op > 5:
            print('Ha ingresado una opcion no valida.')
            time.sleep(3)
        
        #si la opcion ingresada es una de esas 4 opciones, pasa adentro del if
        if op in [1,2,3,4]:
            #en la variable num1 y num2 guardan los datos ingresados
            #en la funcion obtener numeros
            num1,num2 = obtener_numeros()

            if op == 1:
                resultado = sumar(num1, num2)
                print(f'Resultado de la suma : {resultado}\n')
                time.sleep(2)
            if op == 2:
                resultado = restar(num1,num2)
                print(f'Resultado de la resta: {resultado}\n')
                time.sleep(2)
            if op == 3:
                resultado = multiplicar(num1,num2)
                print(f'Resultado de la multiplicacion: {resultado}\n')
                time.sleep(2)
            if op == 4:
                resultado = division(num1,num2)
                print(f'Resultado de la division: {resultado}\n')
                time.sleep(2)

        if op == 5:
            print('Muchas gracias por utilizar el programa.')
            exit()

main()




