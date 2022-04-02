import random
import time


if __name__ == '__main__':
    board = ptb.PyTechBrain()

#   - Nuta wlazł kotek na płotek
    notes = [
        ptb.G3, ptb.E1, ptb.E1, ptb.F5, ptb.D1, ptb.D1, 
        ptb.C1, ptb.E1, ptb.G5, 
        ptb.G3, ptb.E1, ptb.E1, ptb.F5, ptb.D1, ptb.D1, 
        ptb.C3, ptb.E1, ptb.C3, 
        ptb.C3, ptb.E1, ptb.E1, ptb.D5, ptb.F1, ptb.F1, 
        ptb.C1, ptb.E1, ptb.G3, 
        ptb.G3, ptb.E1, ptb.E1, ptb.F5, ptb.D1, ptb.D1
    ]

    stops = [6, 9, 15, 18, 24, 27, 33]s

    i = 0
    while True:
        if board.przycisk_lewy():
            if i <= len(notes):
                board.nuta(notes[i], 1 / 4)
                i += 1
                if i in stops: time.sleep(.3)
            time.sleep(.2)