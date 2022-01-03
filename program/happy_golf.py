# a. Buatlah sebuah sebuah list pemain_golf dengan elemen berupa dictionary.
# Setiap dictionary digunakan untuk menyimpan nama
# peserta dan skor peserta di semua holes.
# Gunakan tipe data terstruktur ini untuk proses pada fungsi yang diminta di bawah ini.
def baca_data_input(file_input):
    pemain_golf = []
    kode = {'QD': 4, 'TP': 3, 'DB': 2, 'BG': 1,
            'PAR': 0, 'BR': -1, 'EG': -2, 'AL': -3, 'CN': -4}

    file = open(file_input, 'r')
    texts = file.readlines()
    file.close()

    for text in texts:
        text = text.split()
        data_pemain = {
            'nama': text[0]
        }
        for nomor, skor in enumerate(text[1:], 1):
            if skor == 'ACE':
                data_pemain[f'Hole {nomor}'] = 1
            else:
                data_pemain[f'Hole {nomor}'] = 5 + kode[skor]
        pemain_golf.append(data_pemain)
    return pemain_golf


# Fungsi Pembantu
def total_skor(pemain_golf):
    '''
    Fungsi total_skor mengembalikan list yang berisi 
    dictionary dengan key nama pemain dan value skor pemain
    '''
    tmp = []
    for pemain in pemain_golf:
        skor = 0
        for hole in list(pemain)[1:]:
            skor += pemain[hole]
        tmp.append({
            pemain['nama']: skor
        })
    return tmp


# b. Buatlah fungsi pemenang untuk mengembalikan (return) peserta ke berapa yang menjadi pemenang.
def pemenang(pemain_golf):
    '''
    Mengembalikan nama pemenang
    '''
    tmp_skor = list()
    for x in pemain_golf:
        tmp_skor.append(list(x.values())[0])
    skor_pemenang = max(tmp_skor)
    index_pemenang = tmp_skor.index(skor_pemenang)
    pemenang = list(pemain_golf[index_pemenang].keys())[0]
    return pemenang


# c. Buatlah fungsi rerata yang digunakan untuk mengembalikan (return) rata-rata skor semua pemain.
def rerata(pemain_golf):
    '''
    Fungsi unutk mencari rata-rata skor pemain golf

    Dengan pameter berupa list yang berisi dictionary dengan 
    key nama pemain dan value skor pemain
    '''
    tmp_total_skor = 0
    for x in pemain_golf:
        tmp_total_skor += list(x.values())[0]
    return tmp_total_skor/len(pemain_golf)
