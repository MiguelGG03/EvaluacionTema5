def main_contador():
    try:
        f=open('contador.txt', 'r')
    except FileNotFoundError:
        with open('contador.txt', 'w') as f:
            f.write('0')

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

            elif pr2=='dec':
                f=open('contador.txt', 'r')
                cont=int(f.read())
                f.close()
                f=open('contador.txt', 'w')
                f.write(str(cont-1))
        elif(pr1=='n'):
            sigue=False
            f.close()
        else:
            print('Opcion no valida')
            f.close()
    f=open('contador.txt', 'r')
    print('El contador final es: {}'.format(f.read()))
    f.close()    

if __name__ == '__main__':
    main_contador()