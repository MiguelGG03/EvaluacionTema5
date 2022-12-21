import os
import time
import pynput as p



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
    

if __name__=='__main__':
    main_reloj()