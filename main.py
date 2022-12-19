from operaciones import *

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

 

    