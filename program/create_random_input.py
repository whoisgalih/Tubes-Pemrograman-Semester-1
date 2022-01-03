from random import randrange, choice
from sys import stderr
from string import ascii_uppercase


def create_random_input():
    kode_skor = ['QD', 'TP', 'DB', 'BG', 'PAR', 'BR', 'EG', 'AL', 'CN']

    try:
        print('Berapa banyak pemain yang akan dibuat?\n(Masukan selain bilangan bulat untuk random)',
              file=stderr)
        jumlah_buat = int(input())
    except ValueError:
        print('Yaudah, aku pilihin. Jurinya cuma mau maksimal 50 pemain aja',
              file=stderr)
        jumlah_buat = randrange(1, 50)
        print(f'Jadi ada {jumlah_buat} pemain ya\n',
              file=stderr)

    try:
        print('Berapa jumlah pukulan?\n(Masukan selain bilangan bulat untuk random)',
              file=stderr)
        pukulan = int(input())
    except ValueError:
        print('Jumlah pukulan random tiap pemain\n(tapi maksimal 50, nanti kalo lebih, yang main capek)\n',
              file=stderr)

    nama = ''
    baris2 = []
    for i in range(jumlah_buat):
        baris = list()
        nama = ''.join(choice(ascii_uppercase) for i in range(5))
        baris.append(nama)

        try:
            for i in range(pukulan):
                baris.append(choice(kode_skor))
        except NameError:
            for i in range(randrange(1, 50)):
                baris.append(choice(kode_skor))

        baris2.append(' '.join(baris))

    file = open('./text/happy_golf.random.input', 'w')
    file.write('\n'.join(baris2))
    file.close()
