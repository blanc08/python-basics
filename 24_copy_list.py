a = ["Bagus", "Oktaviadi"]
print(f"a = {a}")

b = a
print(f"b = {b}")

a[0] = "Uncle"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# kedua variable tersebut akan sama" terubah jika dimanipulasi lansung seperti datas..
# dikarenakan, kedua variable tersebut mengarah ke referensi atau adress sama

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")


# method copy
c = a.copy()
c.insert(2, "Ok")
print(f"address c = {hex(id(c))}")
print(f"c = {c}")
print(f"a = {a}")
