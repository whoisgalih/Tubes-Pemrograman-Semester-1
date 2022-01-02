def table_sep(len_columns):
    for len_column in len_columns:
        print('+', '-'*(len_column+2), sep='', end='')
    print('+')


def table_body(bodies, len_columns):
    for len_column, body in zip(len_columns, bodies):
        if isinstance(body, int):
            print('|', str(body).rjust(len_column), end=' ')
        else:
            print('|', str(body).ljust(len_column), end=' ')
    print('|')


def table_header(headers, len_columns):
    for idx, header in enumerate(headers):
        print('|', str(header).center(len_columns[idx]), end=' ')
    print('|')


def table(kwargs):
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
