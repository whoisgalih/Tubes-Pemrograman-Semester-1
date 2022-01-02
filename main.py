from print import *
from table import table
from happy_golf import total_skor, rerata, baca_data_input
from time import sleep


# Buatlah main program yang digunakan untuk menampilkan list dan memanggil fungsi yang dibuat.
def main(pemain_golf):
    print_judul()

    # Print data
    jumlah_data = [len(data_pemain) for data_pemain in pemain_golf]
    terpanjang = max(jumlah_data)
    index_data_pemain_terpanjang = jumlah_data.index(terpanjang)
    data_table = {
        'Holes': [hole for hole in list(pemain_golf[index_data_pemain_terpanjang])[1:]]
    }
    for data_pemain in pemain_golf:
        data_table[data_pemain['nama']] = list(data_pemain.values())[1:]

    table(data_table)

    # Pemenang
    pemain_golf = total_skor(pemain_golf)
    print_pemenang(pemain_golf)
    sleep(3)

    print('\n\nDaftar Pemain')
    table({
        'Player Name': [list(pemain.keys())[0] for pemain in pemain_golf],
        'Score': [list(pemain.values())[0] for pemain in pemain_golf]
    })

    print('\n\nRata - rata seluruh pemain golf:')
    print(rerata(pemain_golf))


main(baca_data_input())
