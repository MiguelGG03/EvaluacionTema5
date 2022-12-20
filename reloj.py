import os
import time



def main_reloj():
    print('Presione Enter para parar el reloj')
    print('En cinco segundos se iniciara el reloj')
    time.sleep(5)
    
    while True:
        os.system('cls')
        print(time.strftime('%H:%M:%S'))
        time.sleep(1)
        if input()=='':
            break
        else:
            continue


if __name__=='__main__':
    main_reloj()