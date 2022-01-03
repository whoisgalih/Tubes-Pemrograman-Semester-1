from program.print import print_pemenang, print_judul, file_input
from program.table import table
from program.happy_golf import total_skor, rerata, baca_data_input
from time import sleep


# d. Buatlah main program yang digunakan untuk menampilkan list dan memanggil fungsi yang dibuat.
def main():
    # Print judul
    print_judul()

    # Memsukan input
    pemain_golf = baca_data_input(file_input())

    # Print data pemain
    jumlah_data = [len(data_pemain) for data_pemain in pemain_golf]
    terpanjang = max(jumlah_data)
    index_data_pemain_terpanjang = jumlah_data.index(terpanjang)
    data_table = {
        'Holes': [hole for hole in list(pemain_golf[index_data_pemain_terpanjang])[1:]]
    }
    for data_pemain in pemain_golf:
        data_table[data_pemain['nama']] = list(data_pemain.values())[1:]

    print('\n\nData Pemain')
    table(data_table)

    # Print Pemenang
    pemain_golf = total_skor(pemain_golf)
    print_pemenang(pemain_golf)
    sleep(1)

    # Print Daftar Pemain
    print('\n\nDaftar Pemain')
    table({
        'Player Name': [list(pemain.keys())[0] for pemain in pemain_golf],
        'Score': [list(pemain.values())[0] for pemain in pemain_golf]
    })

    # Print Rata-Rata Skor
    print('\n\nRata - rata seluruh pemain golf:')
    print(rerata(pemain_golf))


main()
