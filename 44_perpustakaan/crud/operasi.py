import time
from .utils import random_string
from . import database


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


def read():
    try:
        with open(database.DB_NAME, 'r', encoding='utf-8') as file:
            content = file.readlines()
            return content

    except Exception:
        return None
