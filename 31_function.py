"""Function -> F(x)"""


# Reguler | Plan function
def sayHello():
    """
    saying hello to user
    """
    print("Hello words!")


sayHello()


# Argumented function
def greeting(name: str):
    """
    greeting user
    """
    print(f"Hello {name}")


greeting("Bagus")


# default argument
def greeting_with_default(name: str = "kamu"):
    """
    greeting user
    """
    print(f"Hello {name}")


greeting_with_default()

# named parameter
greeting_with_default(name="Named Argument")


# function dengar return
def tambah(a: int, b: int):
    """
    Menambahkan 2 buah variable
    """
    return a + b


hasil = tambah(6, 4)
print(f"hasil -> {hasil}")


# multiple return
def operasi_dasar(a: int, b: int):
    return a + b, a - b, a / b, a * b


tambah, kurang, bagi, kali = operasi_dasar(6, 10)

print(f"hasil tambah -> {tambah}")
print(f"hasil kurang -> {kurang}")
print(f"hasil bagi -> {bagi}")
print(f"hasil kali -> {kali}")
