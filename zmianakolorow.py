import random
import time


if __name__ == '__main__':
    board = ptb.PyTechBrain()

 #Zmiana kolorów w zależności od światła
    MAX = 1023
    while True: 

        brightness = board.fotorezystor_raw()
        if brightness > 0 and brightness < MAX / 5: 
            board.sygnalizator_czerwony('on')
            board.sygnalizator_zolty('off')
            board.sygnalizator_zielony('off')

        if brightness > MAX / 5 and brightness < MAX / 1.5:
            board.sygnalizator_czerwony('off')
            board.sygnalizator_zolty('on')
            board.sygnalizator_zielony('off')

        if brightness > MAX / 1.5 and brightness <= MAX:
            board.sygnalizator_czerwony('off')
            board.sygnalizator_zolty('off')
            board.sygnalizator_zielony('on')
