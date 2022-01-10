# a. Buatlah sebuah sebuah list pemain_golf dengan elemen berupa dictionary.
# Setiap dictionary digunakan untuk menyimpan nama
# peserta dan skor peserta di semua holes.
# Gunakan tipe data terstruktur ini untuk proses pada fungsi yang diminta di bawah ini.
def baca_data_input(file_input):
    # Membaca file
    file = open(file_input, 'r')
    texts = file.readlines()
    file.close()

    # Membuat dictionary dengan key kode skor dan value skor
    kode = {'QD': 4, 'TP': 3, 'DB': 2, 'BG': 1,
            'PAR': 0, 'BR': -1, 'EG': -2, 'AL': -3, 'CN': -4}

    # Membuat list kosong
    pemain_golf = []

    # Membuat dictionary yang akan ditambahkan ke list pemain_golf
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

    # Mengembailikan list pemain_golf
    return pemain_golf


# Fungsi Pembantu
def total_skor(pemain_golf):
    '''
    Fungsi total_skor mengembalikan list yang berisi 
    dictionary dengan key nama pemain dan value skor pemain
    '''
    # Mambuat list kosong
    tmp = []

    # Looping untuk menambahkan dictionary dengan key nama pemain dan value total skor pemain
    for pemain in pemain_golf:
        # Membuat vaibel skor dengan nolai 0
        skor = 0

        # Looping untuk menambahkan skor pemain kedalam variable skor
        for hole in list(pemain)[1:]:
            skor += pemain[hole]

        # Membuat dictionary dengan key nama pemain dan value total skor pemain
        # lalu menambahkannya ke list tmp
        tmp.append({
            pemain['nama']: skor
        })

    return tmp


# b. Buatlah fungsi pemenang untuk mengembalikan (return) peserta ke berapa yang menjadi pemenang.
def pemenang(skor_pemain):
    '''
    Mengembalikan nama pemenang
    '''
    sorted_winner = sorted(skor_pemain, key=lambda pemain: list(
        pemain.values())[0], reverse=True)

    return (sorted_winner[0], sorted_winner[1], sorted_winner[2])

    # Membuat list kosong yang akan berisi daftar skor setiap pemain
    tmp_skor = list()

    # Looping untuk menambahkan skor tiap pemain ke list tmp_skor
    for pemain in skor_pemain:
        tmp_skor.append(list(pemain.values())[0])

    # Mengambil nilai maksimum pemenang
    skor_pemenang = max(tmp_skor)

    # Mengambil index nilai maksimum pemenang
    index_pemenang = tmp_skor.index(skor_pemenang)

    # Mengambil nama pemenang
    pemenang = list(skor_pemain[index_pemenang].keys())[0]

    return pemenang


# c. Buatlah fungsi rerata yang digunakan untuk mengembalikan (return) rata-rata skor semua pemain.
def rerata(skor_pemain):
    '''
    Fungsi unutk mencari rata-rata skor pemain golf

    Dengan pameter berupa list yang berisi dictionary dengan 
    key nama pemain dan value skor pemain
    '''
    # Membuat variabel tmp_total_skor dengan nilai 0
    tmp_total_skor = 0

    # Looping untuk menambahkan skor setiap pemain ke tmp_total_skor
    for pemain in skor_pemain:
        tmp_total_skor += list(pemain.values())[0]

    # Return rata rata
    return tmp_total_skor/len(skor_pemain)
