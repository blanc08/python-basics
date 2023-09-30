from . import operasi

DB_NAME = "data.csv"
TEMPLATE = {
    "pk": "XXXXXX",
    "date_add": "YYYY-MM-DD",
    "judul": 255 * " ",
    "penulis": 255 * " ",
    "tahun": "YYYY",
}


def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("database tersedia, init done!")
    except Exception:
        print("database tidak ditemukan, membuat database baru...")

        operasi.create_first_data()
