# Tubes Pemrograman Semester 1

| Identitas                    |                     |
| ---------------------------- | ------------------- |
| Nama                         | Galih Akbar Nugraha |
| NIM                          | 1301213060          |
| Kelas                        | IF-45-07            |
| Dosen Pengenalan Pemrograman | Jimmy Tirtawangsa   |
| Nomor Soal                   | 35                  |

## Inputan dari Soal:

```
PRAS PAR BR BR EG TR BG PAR CN ACE QD TR TR DB PAR TR BR EG AL
SAID BR BR BG BG BG PAR DB TR TR QD TR DB PAR BR EG AL CN ACE
VANIE ACE PAR PAR BR BG PAR BR BR BG BG BG BR PAR PAR PAR BR BR BG
FARAH DB AL TP BR EG AL BG CN AL AL BG CN EG AL AL BR ACE QD
BUNYAMIN DB DB QD BR BR BG DB EG BR BG TP QD DB CN AL TP BR PAR
SELLY CN EG TP QD EG DB EG DB PAR QD ACE PAR BR QD CN BG PAR ACE
```

## main.py

File **main.py** digunakan untuk menjalankan seluruh program yang diminta yaitu:

<ol type="a">
  <li>Buatlah sebuah sebuah list <code>pemain_golf</code> dengan elemen berupa dictionary. Setiap dictionary digunakan untuk menyimpan nama peserta dan skor peserta di semua holes. Gunakan tipe data terstruktur ini untuk proses pada fungsi yang diminta di bawah ini. (terletak di main.py, menggunkan fungsi dari happy_golf.py)</li>
  <li>Buatlah fungsi <code>pemenang</code> untuk mengembalikan (return) peserta ke berapa yang menjadi pemenang. (terletak di happy_golf.py)</li>
  <li>Buatlah fungsi <code>rerata</code> yang digunakan untuk mengembalikan (return) rata-rata skor semua pemain. (terletak di happy_golf.py)</li>
  <li>Buatlah <code>main</code> program yang digunakan untuk menampilkan list dan memanggil fungsi yang dibuat. (terletak di main.py)</li>
</ol>

## happy_golf.py

File **happy_golf.py** memiliki semua fungsi yang diminta didalam soal. Fungsinya adalah:

1. `baca_data_input(<path to file>)` mengembailkan list yang elemennya berupa dictionary:
   `{'nama': 'PRAS', 'hole1': 5, 'hole2': 4, ...}`
2. `total_skor(pemain_golf)` mengembalikan list yang elemennya berupa dictionary dengan key nama pemain dan value total kor pemain. Selain itu, funsi ini untuk membantu:
   1. mencari siapa pemenang permainan,
   2. membantu mencetak total or masing masing pemain, dan
   3. membantu mecari rata-rata.
3. `pemenang(<pemain_golf yang didapat dari total_skor(pemain_golf)>)` megembailkan nama pemenang
4. `rerata(<pemain_golf yang didapat dari total_skor(pemain_golf)>)` mnegembailkan rata-rata

## table.py

File **table.py** membantu untuk mencetak tabel yang scalable. Table memiliki parameter beupa dictionary dengan key judul kolom dan value list isi kolom.

## print.py

File **print.py** berisi fungsi pembantu untuk mencetak:

1. `printerr(...)` mempersingkat mencetak suatu kalimat/kata dalam file stderr
2. `print_pemenang(...)` mencetak nama pemenang dengan animasi random karakter
3. `print_judul()` mencetak ascii art dari judul
4. `file_input()` memberi pilihan dari mana program akan membaca file yang diinputkan yang terdiri dari 4 pilihan:
   1. Input dari tugas yang diberi oleh dosen
   2. Buat input random melalui create_random_input.py
   3. File teks costom
   4. Input CLI

## create_random_input.py

File **create_random_input.py** berisi fungsi tambahan untuk membuat inputan yang random. Fungsi akan mebuat file teks berupa string dengan pola yang sama dengan yang diberi oleh dosen. Jumlah baris maksimumnya adalah 50 dan jumlah holes maksimumnya adalah 50. Pengguna dapat menentukan berapa abanyak pemain dan berapa banyak holes.
