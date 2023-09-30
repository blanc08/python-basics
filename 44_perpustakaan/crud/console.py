import time

from . import operasi, database
from .utils import random_string


def delete_console():
    read_console()

    while True:
        print('silahkan pilih nomor buku yang akan di update')
        nomor_buku = int(input('pilih nomor buku yang akan di update : '))
        data_buku = operasi.read(index=nomor_buku)

        if data_buku is not None:
            break

        print('=' * 100)
        print('nomor tidak valid, silahkan pilih nomor yang lain')
    # end while

    operasi.delete(nomor_buku, data_buku)


def update_console():
    read_console()

    while True:
        print('silahkan pilih nomor buku yang akan di update')
        nomor_buku = int(input('pilih nomor buku yang akan di update : '))
        data_buku = operasi.read(index=nomor_buku)

        if data_buku is not None:
            break

        print('=' * 100)
        print('nomor tidak valid, silahkan pilih nomor yang lain')
    # end while

    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    # user updating process
    while True:
        print("silahkan pilih data apa yang ingin dirubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        user_options = input("pilih [1,2,3]: ")

        match user_options:
            case "1":
                judul = input('judul\t:')
            case "2":
                penulis = input('penulis\t:')
            case "3":
                while True:
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")
                    except:
                        print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")
            case _:
                print('pilihan tidak tersedia')

        is_done = input("Apakah selesai? Y/N = ")
        if is_done.lower() == "y":
            break
        # end user updating process

    # update database
    operasi.update(nomor_buku, pk, data_add, penulis, judul, tahun)


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
