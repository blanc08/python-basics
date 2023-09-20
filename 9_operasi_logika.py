# not, or, and, xor
a = True

print("data boolean a =", a)

# NOT | kebalikan dari a
c = not a
print("data boolean c =", c)

# OR | Jika salah satu true, maka hasilnya akan true
d = c or a
print("data boolean d =", d)

# and || kedua duanya harus true, kalo tidak maka akan selalu jadi false
e = a and c
print("data boolean e =", e)

# xor || akan true jika hanya salah satu true, selain itu false
# misal, jika a = true dan c = true maka akan false
xor = a ^ c
print("data boolean XOR =", xor)
