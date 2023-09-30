import time

from . import operasi, database
from .utils import random_string


def create_console():
    penulis = input("Penulis = ")
    judul = input("Judul = ")
    while (True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")
        except:
            print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")

    operasi.create(tahun, judul, penulis)
    read_console()


def read_console():
    data_file = operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n" + "=" * 100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print('-' * 100)

    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(',')

        pk = data_break[0]
        data_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index + 1:4} | {judul:.40} | {penulis:.40} | {tahun:5}", end='')

    # Footer
    print("\n" + "=" * 100 + "\n")
