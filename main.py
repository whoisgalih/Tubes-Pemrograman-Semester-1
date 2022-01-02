from print import *
from table import table
from happy_golf import total_skor, rerata, baca_data_input


# Interactive
def main(pemain_golf):
    print_judul()
    print_nama(pemain_golf)
    print(pemain_golf)
    pemain_golf = total_skor(pemain_golf)
    print('\n\nDaftar Pemain')
    table(pemain_golf, 'Player Name', 'Score')
    print_pemenang(pemain_golf)
    print('\n\nRata - rata seluruh pemain golf:')
    print(rerata(pemain_golf))


main(baca_data_input())
