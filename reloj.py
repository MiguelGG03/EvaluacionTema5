import os
import time
import keyboard as k



def main_reloj():
    print('Presione Enter para parar el reloj')
    print('En cinco segundos se iniciara el reloj')
    time.sleep(5)
    
    while True:
        try:
            if k.is_pressed('Enter'):
                break
            else:
                os.system('cls')
                print(time.strftime('%H:%M:%S'))
                time.sleep(1)
        except:
            break

if __name__=='__main__':
    main_reloj()