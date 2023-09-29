"""args"""


def args_func(*args):
    """
    docstring
    """
    print(f"nama -> {args[0]}, umur -> {args[1]}")


args_func("Bagus", 51)


# use case
def tambah(*numbers):
    output = 0
    for angka in numbers:
        output += angka

    return output


hasil = tambah(5, 6, 1, 2, 7, 8)
print(hasil)

hasil2 = tambah(1, 2)
print(hasil2)
