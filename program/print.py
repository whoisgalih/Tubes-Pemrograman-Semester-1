from random import choice, randint
from time import sleep
from sys import stderr
from string import ascii_letters
from program.happy_golf import pemenang
from program.create_random_input import create_random_input


def printerr(*args, sep=' ', end='\n'):
    '''
    Membantu print dalam file stderr
    '''
    print(sep.join(args), end=end, file=stderr)


def print_pemenang(pemain_golf):
    '''
    Mencetak nama pemenenang dengan animasi random letters
    '''
    print('\n\nPemenangnya adalah:')
    winner = pemenang(pemain_golf)
    len_w = len(winner)
    for i in range(30):
        printerr(''.join(choice(ascii_letters)
                         for _ in range(randint(1, len_w))).ljust(len_w), end='\r')
        sleep(0.1)
    print(winner)


def print_judul():
    '''
    Mencetak judul HAPPY GOLF
    '''
    printerr('''
    ██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗   ██╗   ██████╗  █████╗ ██╗     ███████╗
    ██║  ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝  ██╔════╝ ██╔══██╗██║     ██╔════╝
    ███████║███████║██████╔╝██████╔╝ ╚████╔╝   ██║  ██╗ ██║  ██║██║     █████╗
    ██╔══██║██╔══██║██╔═══╝ ██╔═══╝   ╚██╔╝    ██║  ╚██╗██║  ██║██║     ██╔══╝
    ██║  ██║██║  ██║██║     ██║        ██║     ╚██████╔╝╚█████╔╝███████╗██║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝      ╚═════╝  ╚════╝ ╚══════╝╚═╝


''')


def file_input():
    '''
    Memberi pilihan dari mana program akan membaca file yang diinputkan yang terdiri dari 4 pilihan:
    1. Input dari tugas yang diberi oleh dosen
    2. Buat input random melalui create_random_input.py
    3. File teks costom
    4. Input CLI
    '''
    printerr('''Ingin input file dari mana? 
[1] Input dari tugas
[2] Buat input random melalui create_random_input.py
[3] File teks costom
[4] Input CLI

Ketik angka: ''', end='')
    kode_file = input()
    if kode_file == '1':
        return 'text/happy_golf.input'
    elif kode_file == '2':
        create_random_input()
        return 'text/happy_golf.random.input'
    elif kode_file == '3':
        printerr('Masukan alamat file: ', end='\n')
        return input()
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
