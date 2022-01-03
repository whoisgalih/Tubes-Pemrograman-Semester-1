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
    for len_column, body in zip(len_columns, bodies):
        body = str(body)
        if body.isnumeric():
            print('|', body.rjust(len_column), end=' ')
        else:
            print('|', body.ljust(len_column), end=' ')
    print('|')


def table_header(headers, len_columns):
    '''
    Membuat baris judul tabel
    '''
    for idx, header in enumerate(headers):
        print('|', str(header).center(len_columns[idx]), end=' ')
    print('|')


def table(kwargs):
    '''
    Membuat tabel dengan argumen berupa dictionary dengan key judul kolom dan value isi (body) kolom
    '''
    headers = list(kwargs)
    len_columns = list()
    for k, v in kwargs.items():
        len_columns.append(max([len(str(item)) for item in v]+[len(str(k))]))
    table_sep(len_columns)
    table_header(headers, len_columns)
    table_sep(len_columns)
    bodies = list()
    for idx in range(max([len(x) for x in kwargs.values()])):
        tmp = list()
        for header in headers:
            try:
                tmp.append(kwargs[header][idx])
            except IndexError:
                tmp.append('')
        bodies.append(tmp)
    for item in bodies:
        table_body(item, len_columns)
    table_sep(len_columns)
