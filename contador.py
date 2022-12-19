def main_contador():
    try:
        f=open('contador.txt', 'r')
    except FileNotFoundError:
        with open('contador.txt', 'w') as f:
            f.write('0')

if __name__ == '__main__':
    main_contador()