import random
import sys
import string


def create_random_input():
    kode_skor = ['QD', 'TP', 'DB', 'BG', 'PAR', 'BR', 'EG', 'AL', 'CN']

    try:
        print('Berapa banyak pemain yang akan dibuat?\n(Masukan selain bilangan bulat untuk random)',
              file=sys.stderr)
        jumlah_buat = int(input())
    except ValueError:
        print('Yaudah, aku pilihin. Jurinya cuma mau maksimal 50 pemain aja',
              file=sys.stderr)
        jumlah_buat = random.randrange(1, 50)
        print(f'Jadi ada {jumlah_buat} pemain ya\n',
              file=sys.stderr)

    try:
        print('Berapa jumlah pukulan?\n(Masukan selain bilangan bulat untuk random)',
              file=sys.stderr)
        pukulan = int(input())
    except ValueError:
        print('Jumlah pukulan random tiap pemain\n(tapi maksimal 50, nanti kalo lebih, yang main capek)\n',
              file=sys.stderr)

    nama = ''
    baris2 = []
    for i in range(jumlah_buat):
        baris = list()
        nama = ''.join(random.choice(string.ascii_uppercase) for i in range(5))
        baris.append(nama)

        try:
            for i in range(pukulan):
                baris.append(random.choice(kode_skor))
        except NameError:
            for i in range(random.randrange(1, 50)):
                baris.append(random.choice(kode_skor))

        baris2.append(' '.join(baris))

    file = open('./text/happy_golf.random.input2', 'w')
    file.write('\n'.join(baris2))
    file.close()
