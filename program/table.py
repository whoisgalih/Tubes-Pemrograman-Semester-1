def table_sep(len_columns):
    '''
    Membuat pemisah tabel dengan argumen berupa panjang kolom-kolom
    '''
    for len_column in len_columns:
        print('+', '-'*(len_column+2), sep='', end='')
    print('+')


def table_body(bodies, len_columns):
    '''
    Membuat baris tabel
    '''
    # Looping mencetak setiap elemen bodies
    for len_column, body in zip(len_columns, bodies):
        body = str(body)

        # Jika body numerik, maka dicetak rata kanan
        if body.isnumeric():
            print('|', body.rjust(len_column), end=' ')
        else:
            print('|', body.ljust(len_column), end=' ')
    print('|')


def table_header(headers, len_columns):
    '''
    Membuat baris judul tabel
    '''
    # Looping mencetak setiap elemen headrs dengan rata tengah
    for idx, header in enumerate(headers):
        print('|', str(header).center(len_columns[idx]), end=' ')
    print('|')


def table(kwargs):
    '''
    Membuat tabel scalable dengan argumen berupa dictionary dengan key judul kolom dan value isi (body) kolom
    '''
    # Mengabil key dari dictionary
    headers = list(kwargs)

    # Mebuat list kosong unutk menyimpan seuluh lebar satu kolom
    len_columns = list()

    # Looping menambahkan setiap kolom
    for k, v in kwargs.items():
        # Mencari string terpanjang dalam kolom unutk dijadikan lebar kolom
        len_columns.append(max([len(str(item)) for item in v]+[len(str(k))]))

    # Membuat pembatas horizontal
    table_sep(len_columns)

    # Membuat judul kolom dengan
    table_header(headers, len_columns)

    # Membuat pembatas horizontal
    table_sep(len_columns)

    # Looping untuk membuat tebel body
    for idx in range(max([len(x) for x in kwargs.values()])):
        tmp = list()
        # Menambahkan elemen untuk body tabel
        for header in headers:
            try:
                tmp.append(kwargs[header][idx])
            except IndexError:
                tmp.append('')
        # Membuat body tabel
        table_body(tmp, len_columns)

    # Membuat pembatas horizontal
    table_sep(len_columns)
