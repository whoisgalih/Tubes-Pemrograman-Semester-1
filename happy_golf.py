pemain_golf = []
text = ''
nilai = 0

kode = {'QD': 4, 'TP': 3, 'DB': 2, 'BG': 1,
        'PAR': 0, 'BR': -1, 'EG': -2, 'AL': -3, 'CN': -4}

try:
    while True:
        text = input().split()
        nilai = 0
        for skor in text[1:]:
            if skor == 'ACE':
                nilai += 1
            else:
                nilai += 5 + kode[skor]
        pemain_golf.append({text[0]: nilai})
except EOFError:
    pass


def pemenang(pemain_golf):
    tmp_skor = list()
    for x in pemain_golf:
        tmp_skor.append(list(x.values())[0])
    skor_pemenang = max(tmp_skor)
    index_pemenang = tmp_skor.index(skor_pemenang)
    pemenang = list(pemain_golf[index_pemenang].keys())[0]
    return pemenang


def rerata(pemain_golf):
    tmp_total_skor = 0
    for x in pemain_golf:
        tmp_total_skor += list(x.values())[0]
    return tmp_total_skor/len(pemain_golf)


print(pemain_golf)
print(pemenang(pemain_golf))
print(rerata(pemain_golf))
