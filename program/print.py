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

    # Mengambil nama pemenang menggunakan fungsi pemenenang(...)
    winner = pemenang(pemain_golf)

    # Animasi
    # Mencari panjang nama pememnang
    len_w = len(winner)

    # Lopping untuk print huruf acak dalam baris yang sama yang akan me-reveal nama pemenang
    for i in range(30):
        printerr(''.join(choice(ascii_letters)
                         for _ in range(randint(1, len_w))).ljust(len_w), end='\r')
        # sleep selama 0.1s untuk memperindah animasi
        sleep(0.1)

    # Print nama pemenang
    print(winner)


def print_judul():
    '''
    Mencetak judul HAPPY GOLF di CLI saja agar menghindari error ASCII string
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
    # Print pilihan inpput
    printerr('''Ingin input file dari mana? 
[1] Input dari tugas
[2] Buat input random melalui create_random_input.py
[3] File teks costom
[4] Input CLI

Ketik angka: ''', end='')

    # input kode file sesuai angka
    kode_file = input()

    # Mengembailikan directory file
    if kode_file == '1':
        return 'text/happy_golf.input'
    elif kode_file == '2':
        create_random_input()
        return 'text/happy_golf.random.input'
    elif kode_file == '3':
        printerr('Masukan alamat file: ', end='\n')
        return input()
    else:
        # Mengambil inputan terus-menerus hingga string kosong
        line = input()
        lines = ''
        while line != '':
            lines += line + '\n'
            line = input()

        # Menyimpan input dalam file
        file = open('text/custom.input', 'w')
        file.write(lines)
        file.close()

        return 'text/custom.input'
