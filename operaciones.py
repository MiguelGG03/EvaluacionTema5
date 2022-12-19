def suma(a, b):
    if(type(a)==str and type(b)==str):
        print("No se puede sumar una cadena de string")
    else:
        return a + b

def resta(a, b):
    if(type(a)==str and type(b)==str):
        print("No se puede restar una cadena de string")
    else:
        return a - b

def producto(a, b):
    if(type(a)==str and type(b)==str):
        print("No se puede multiplicar una cadena de string")
    else:
        return a*b

def division(a,b):
    if(type(a)==str and type(b)==str):
        print("No se puede dividir una cadena de string")
    else:
        try:
            return a/b
        except ZeroDivisionError:
            print("No se puede dividir por cero")
            return None
    