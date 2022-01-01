def table_sep(len_column_1, len_column_2):
    print('+', '-'*(len_column_1+2), '+', '-'*(len_column_2+2), '+', sep='')


def table_body(body1, body2, len_column_1, len_column_2):
    print('|', body1.ljust(len_column_1), '|', body2.rjust(len_column_2), '|')


def table_header(header1, header2, len_column_1, len_column_2):
    print('|', header1.center(len_column_1),
          '|', header2.center(len_column_2), '|')


def table(pemain_golf, header1, header2):
    len_column_1 = max([len(list(pemain.keys())[0])
                       for pemain in pemain_golf]+[len(header1)]) + 1
    len_column_2 = max([len(str(list(pemain.values())[0]))
                       for pemain in pemain_golf]+[len(header2)]) + 1
    table_sep(len_column_1, len_column_2)
    table_header(header1, header2, len_column_1, len_column_2)
    table_sep(len_column_1, len_column_2)
    for pemain in pemain_golf:
        table_body(list(pemain.keys())[0], str(
            list(pemain.values())[0]), len_column_1, len_column_2)
    table_sep(len_column_1, len_column_2)
