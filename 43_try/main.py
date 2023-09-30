input_user = int(input("Masukkan input"))
hasil = 0 

try:
    hasil = 10 / input_user
except:
    print("something went wrong")

print(f"hasil -> {hasil}")
