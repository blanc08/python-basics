def tambah(*args):
    """
    docstring
    """
    hasil = 0
    for data in args:
        hasil += data

    return hasil


def kali(*args):
    """
    docstring
    """
    hasil = 0
    for data in args:
        hasil *= data

    return hasil


def bagi(*args):
    """
    docstring
    """
    hasil = 0
    for data in args:
        hasil /= data

    return hasil
