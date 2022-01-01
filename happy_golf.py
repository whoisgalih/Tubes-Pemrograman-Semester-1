def baca_data_input():
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
    return pemain_golf


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
