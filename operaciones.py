def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def producto(a, b):
    return a*b

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return None