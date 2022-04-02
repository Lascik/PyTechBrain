import random
import time


if __name__ == '__main__':
    board = ptb.PyTechBrain()
    
    # - Zmiana jasnosci RGB
    while True:
        x = board.potencjometr_raw()

        board.RGB_kolor(
            x if x <= 255 else 255, 
            x if x <= 255 else 255, 
            x if x <= 255 else 255
        )

        if board.przycisk_lewy(): board.buzzer_sygnal('demo')
        if board.przycisk_prawy(): board.buzzer_sygnal('off')



