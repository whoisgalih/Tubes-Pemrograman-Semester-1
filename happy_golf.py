import random
import time
import sys
from string import ascii_letters

pemain_golf = []

kode = {'QD': 4, 'TP': 3, 'DB': 2, 'BG': 1,
        'PAR': 0, 'BR': -1, 'EG': -2, 'AL': -3, 'CN': -4}

try:
    while True:
        text = input().split()
        data_pemain = {
            'nama': text[0]
        }
        for nomor, skor in enumerate(text[1:], 1):
            if skor == 'ACE':
                data_pemain[f'hole{nomor}'] = 1
            else:
                data_pemain[f'hole{nomor}'] = 5 + kode[skor]
        pemain_golf.append(data_pemain)
except EOFError:
    pass


def total_skor(pemain_golf):
    tmp = []
    for pemain in pemain_golf:
        skor = 0
        for hole in list(pemain)[1:]:
            skor += pemain[hole]
        tmp.append({
            pemain['nama']: skor
        })
    return tmp


def pemenang(pemain_golf):
    tmp_skor = list()
    for x in pemain_golf:
        tmp_skor.append(list(x.values())[0])
    skor_pemenang = max(tmp_skor)
    index_pemenang = tmp_skor.index(skor_pemenang)
    pemenang = list(pemain_golf[index_pemenang].keys())[0]
    return pemenang


def rerata(pemain_golf):
    '''
    Fungsi unutk mencari rata-rata skor pemain golf
    Parameter:

    '''
    tmp_total_skor = 0
    for x in pemain_golf:
        tmp_total_skor += list(x.values())[0]
    return tmp_total_skor/len(pemain_golf)


def printerr(*args, sep=' ', end='\n'):
    print(sep.join(args), end=end, file=sys.stderr)


def table_sep(len_column_1, len_column_2):
    print('+', '-'*(len_column_1+2), '+', '-'*(len_column_2+2), '+', sep='')


def table_body(body1, body2, len_column_1, len_column_2):
    print('|', body1.ljust(len_column_1), '|', body2.rjust(len_column_2), '|')


def table_header(header1, header2, len_column_1, len_column_2):
    print('|', header1.center(len_column_1),
          '|', header2.center(len_column_2), '|')


def table(pemain_golf, header1, header2):
    len_column_1 = max([len(list(pemain.keys())[0])
                       for pemain in pemain_golf]+[len(header1)]) + 1
    len_column_2 = max([len(str(list(pemain.values())[0]))
                       for pemain in pemain_golf]+[len(header2)]) + 1
    table_sep(len_column_1, len_column_2)
    table_header(header1, header2, len_column_1, len_column_2)
    table_sep(len_column_1, len_column_2)
    for pemain in pemain_golf:
        table_body(list(pemain.keys())[0], str(
            list(pemain.values())[0]), len_column_1, len_column_2)
    table_sep(len_column_1, len_column_2)


def print_pemenang(pemain_golf):
    printerr('\n\nPemenangnya adalah:')
    winner = pemenang(pemain_golf)
    len_w = len(winner)
    for i in range(15):
        printerr(''.join(random.choice(ascii_letters)
                         for _ in range(random.randint(1, len_w))).ljust(len_w), end='\r')
        time.sleep(0.1)
    print(winner)


def print_judul():
    printerr('''
    ██╗░░██╗░█████╗░██████╗░██████╗░██╗░░░██╗  ░██████╗░░█████╗░██╗░░░░░███████╗
    ██║░░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝  ██╔════╝░██╔══██╗██║░░░░░██╔════╝
    ███████║███████║██████╔╝██████╔╝░╚████╔╝░  ██║░░██╗░██║░░██║██║░░░░░█████╗░░
    ██╔══██║██╔══██║██╔═══╝░██╔═══╝░░░╚██╔╝░░  ██║░░╚██╗██║░░██║██║░░░░░██╔══╝░░
    ██║░░██║██║░░██║██║░░░░░██║░░░░░░░░██║░░░  ╚██████╔╝╚█████╔╝███████╗██║░░░░░
    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░░  ░╚═════╝░░╚════╝░╚══════╝╚═╝░░░░░''')


# Interactive
def main():
    global pemain_golf
    print_judul()
    print(pemain_golf)
    pemain_golf = total_skor(pemain_golf)
    printerr('\n\nDaftar Pemain')
    table(pemain_golf, 'Player Name', 'Score')
    print_pemenang(pemain_golf)
    printerr('\n\nRata - rata seluruh pemain golf:')
    print(rerata(pemain_golf))


main()
