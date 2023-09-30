import os
import time
from .utils import random_string
from . import database


def delete(nomor_buku, data_str):
    data_length = len(data_str)
    try:
        with open(database.DB_NAME, 'r+', encoding="utf-8") as file:
            counter = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == nomor_buku - 1:
                    pass
                else:
                    try:
                        with open('data_temporary.csv', 'a', encoding="utf-8") as temp_file:
                            temp_file.write(content)
                    except Exception:
                        print("error saat melakukan update")
                counter += 1
            # end while loop

            os.rename('data_temporary.csv', database.DB_NAME)
            print('successfully deleting database')
    except:
        print("error saat melakukan update")


def update(nomor_buku, pk, data_add, penulis, judul, tahun):
    data = database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    data_length = len(data_str)
    try:
        with open(database.DB_NAME, 'r+', encoding="utf-8") as file:
            file.seek(data_length * (nomor_buku - 1))
            file.write(data_str)
            print('successfully updating database')
    except:
        print("update saat melakukan update")


def create(tahun: int, judul: str, penulis: str):
    data = database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(database.DB_NAME, 'a', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit ditambahkan boooos, gagal maning")


def create_first_data():
    # with open(DB_NAME, "w", encoding="utf-8") as file:
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

    data = database.TEMPLATE.copy()
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data['penulis'] = penulis + database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + database.TEMPLATE["judul"][len(judul):]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"

    try:
        with open(database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str)

    except Exception:
        print('Gagal menyimpan data')


def read(**kwargs):
    try:
        with open(database.DB_NAME, 'r', encoding='utf-8') as file:
            content = file.readlines()

            if "index" in kwargs:
                if 0 <= (kwargs['index'] - 1) < len(content):
                    return content[kwargs['index'] - 1]
                else:
                    return None

            return content

    except Exception:
        return None
