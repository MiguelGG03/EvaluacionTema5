def main_contador():
    try:
        f=open('contador.txt', 'r')
    except FileNotFoundError:
        with open('contador.txt', 'w') as f:
            f.write('0')
    except:
        print('Fichero corrupto')
    try:
        f=open('contador.txt', 'r')
        cont=int(f.read())
        f.close()
    except ValueError:
        print('No se pudo pasar el valor del archivo a entero')

    pr2=input('Desea incrementar o decrementar el contador? (inc/dec): ')
    if pr2=='inc':
        f=open('contador.txt', 'r')
        cont=int(f.read())
        f.close()
        f=open('contador.txt', 'w')
        f.write(str(cont+1))
        f.close()

    elif pr2=='dec':
        f=open('contador.txt', 'r')
        cont=int(f.read())
        f.close()
        f=open('contador.txt', 'w')
        f.write(str(cont-1))
        f.close()
    else:
        cont=str(f.read())
        print('Opcion no valida, el contador final es {}'.format(cont))
        f.close()
    sigue=True
    while(sigue):
        pr1=input('Desea seguir incrementando el contador? (s/n): ')
        if pr1=='s':
            pr2=input('Desea incrementar o decrementar el contador? (inc/dec): ')
            if pr2=='inc':
                f=open('contador.txt', 'r')
                cont=int(f.read())
                f.close()
                f=open('contador.txt', 'w')
                f.write(str(cont+1))
                f.close()

            elif pr2=='dec':
                f=open('contador.txt', 'r')
                cont=int(f.read())
                f.close()
                f=open('contador.txt', 'w')
                f.write(str(cont-1))
                f.close()
            else:
                sigue=False
        elif(pr1=='n'):
            cont=str(f.read())
            print('El contador final es {}'.format(cont))
            f.close()
            sigue=False
            
        else:
            cont=str(f.read())
            print('Opcion no valida, el contador final es {}'.format(cont))
            f.close()
            sigue=False   

if __name__ == '__main__':
    main_contador()