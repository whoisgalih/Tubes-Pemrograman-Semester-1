from random import choice, randint
from time import sleep
import sys
from string import ascii_letters
from happy_golf import pemenang


def printerr(*args, sep=' ', end='\n'):
    print(sep.join(args), end=end, file=sys.stderr)


def print_pemenang(pemain_golf):
    print('\n\nPemenangnya adalah:')
    winner = pemenang(pemain_golf)
    len_w = len(winner)
    for i in range(15):
        print(''.join(choice(ascii_letters)
                      for _ in range(randint(1, len_w))).ljust(len_w), end='\r')
        sleep(0.1)
    print(winner)


def print_judul():
    print('''
██╗░░██╗░█████╗░██████╗░██████╗░██╗░░░██╗  ░██████╗░░█████╗░██╗░░░░░███████╗
██║░░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝  ██╔════╝░██╔══██╗██║░░░░░██╔════╝
███████║███████║██████╔╝██████╔╝░╚████╔╝░  ██║░░██╗░██║░░██║██║░░░░░█████╗░░
██╔══██║██╔══██║██╔═══╝░██╔═══╝░░░╚██╔╝░░  ██║░░╚██╗██║░░██║██║░░░░░██╔══╝░░
██║░░██║██║░░██║██║░░░░░██║░░░░░░░░██║░░░  ╚██████╔╝╚█████╔╝███████╗██║░░░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░░  ░╚═════╝░░╚════╝░╚══════╝╚═╝░░░░░''')
