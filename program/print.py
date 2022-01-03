from random import choice, randint
from time import sleep
from sys import stderr
from string import ascii_letters
from happy_golf import pemenang
from create_random_input import create_random_input


def printerr(*args, sep=' ', end='\n'):
    print(sep.join(args), end=end, file=stderr)


def print_pemenang(pemain_golf):
    print('\n\nPemenangnya adalah:')
    winner = pemenang(pemain_golf)
    len_w = len(winner)
    for i in range(30):
        printerr(''.join(choice(ascii_letters)
                         for _ in range(randint(1, len_w))).ljust(len_w), end='\r')
        sleep(0.1)
    print(winner)


def print_judul():
    printerr('''
    ██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗   ██╗   ██████╗  █████╗ ██╗     ███████╗
    ██║  ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝  ██╔════╝ ██╔══██╗██║     ██╔════╝
    ███████║███████║██████╔╝██████╔╝ ╚████╔╝   ██║  ██╗ ██║  ██║██║     █████╗
    ██╔══██║██╔══██║██╔═══╝ ██╔═══╝   ╚██╔╝    ██║  ╚██╗██║  ██║██║     ██╔══╝
    ██║  ██║██║  ██║██║     ██║        ██║     ╚██████╔╝╚█████╔╝███████╗██║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝      ╚═════╝  ╚════╝ ╚══════╝╚═╝
''')


def file_input():
    inputan = input('''Ingin input file dari mana? 
[1] Input dari tugas
[2] Buat input random melalui create_random_input.py
[3] File teks costom
[4] Input CLI

Ketik angka: ''')
    if inputan == '1':
        return 'text/happy_golf.input'
    elif inputan == '2':
        create_random_input()
        return 'text/happy_golf.random.input'
    elif inputan == '3':
        return input('Masukan alamat file: ')
    else:
        line = input()
        lines = ''
        while line != '':
            lines += line + '\n'
            line = input()

        file = open('text/custom.input', 'w')
        file.write(lines)
        file.close()

        return 'text/custom.input'
