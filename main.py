from operaciones import *
from contador import main_contador
from gestor import *
from reloj import *

def main():
    pr1=input('Ingrese el ejercicio que desea ver:\n'
                '1 - Ejercicio 1\n'
                '2 - Ejercicio 2\n'
                '3 - Ejercicio 3\n'
                '4 - Ejercicio 4\n'
                '>>> ')
    if pr1=='1':
        a , b, c, d = (10, 5, 0, "Hola")
        print( "{} + {} = {}".format(a, b, suma(a, b) ) )
        print( "{} - {} = {}".format(b, d, resta(b, d) ) )
        print( "{} * {} = {}".format(b, b, producto(b, b) ) )
        print( "{} / {} = {}".format(a, c, division(a, c) ) )
    elif pr1=='2':
        main_contador()
    elif pr1=='3':
        main_gestor()
    elif pr1=='4':
        main_reloj()
    else:
        print('Opción no válida')
        main()

if __name__=='__main__':
    main()

    