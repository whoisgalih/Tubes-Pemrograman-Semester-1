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
    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░░  ░╚═════╝░░╚════╝░╚══════╝╚═╝░░░░░
''')


def print_nama(pemain_golf):
    for data_pemain in pemain_golf:
        print(data_pemain['nama'])
        for item in list(data_pemain)[1:]:
            print(item.ljust(8), ':', data_pemain[item])
        print()
