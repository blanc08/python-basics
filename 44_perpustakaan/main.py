import os
import crud as crud

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix":
            os.system("clear")
        case "nt":
            os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=========================")

    # check database
    crud.init_console()

    while True:
        match sistem_operasi:
            case "posix":
                os.system("clear")
            case "nt":
                os.system("cls")

        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")

        print("1. Read data")
        print("2. Create data")
        print("3. Update data")
        print("4. Delete data")
        print("=========================")

        user_option = int(input("Masukkan opsi: "))

        match user_option:
            case 1:
                crud.read_console()
            case 2:
                crud.create_console()
            case 3:
                print("3")
            case 4:
                print("4")

        print("=========================")

        is_done = input("Apakah selesai? Y/N = ")
        if is_done.lower() == "y":
            break

        print("program berakhir, Terima kasih!")
