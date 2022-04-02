
import random
import time


if __name__ == '__main__':
    board = ptb.PyTechBrain()
  
 #Sprawdza czy masz gorączke
    while True:
        print(board.temperatura_C())
        if board.przycisk_lewy():
            print('Pobieranie temperatury')
            time.sleep(3)

            temp = board.temperatura_C()
            print(f'Twoja temperatura: {temp}')

            if temp >= 38: print('Masz goraczke! ')
            else:
                print('Nie masz goraczki!')
                board.buzzer_sygnal('demo')