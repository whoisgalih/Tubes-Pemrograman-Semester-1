def table_sep(len_columns):
    for len_column in len_columns:
        print('+', '-'*(len_column+2), sep='', end='')
    print('+')


def table_body(bodies, len_columns, justify):
    for len_column, body, just in zip(len_columns, bodies, justify):
        if just == 'right':
            print('|', str(body).rjust(len_column), end=' ')
        elif just == 'center':
            print('|', str(body).center(len_column), end=' ')
        else:
            print('|', str(body).ljust(len_column), end=' ')
    print('|')


def table_header(headers, len_columns):
    for idx, header in enumerate(headers):
        print('|', str(header).center(len_columns[idx]), end=' ')
    print('|')


# def table(pemain_golf, header1, header2):
#     len_column_1 = max([len(list(pemain.keys())[0])
#                        for pemain in pemain_golf]+[len(header1)])
#     len_column_2 = max([len(str(list(pemain.values())[0]))
#                        for pemain in pemain_golf]+[len(header2)])
#     len_columns = [len_column_1, len_column_2]
#     table_sep(len_columns)
#     table_header(
#         headers=[header1, header2],
#         len_columns=len_columns
#     )
#     table_sep(len_columns)
#     for pemain in pemain_golf:
#         table_body(
#             bodies=[list(pemain.keys())[0], str(list(pemain.values())[0])],
#             len_columns=len_columns,
#             justify=['left', 'right']
#         )
#     table_sep(len_columns)


def table(kwargs):
    headers = list(kwargs)
    len_kwargs = len(headers)
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
            tmp.append(kwargs[header][idx])
        bodies.append(tmp)
    for item in bodies:
        table_body(item, len_columns, ['left']*len_kwargs)
    table_sep(len_columns)
