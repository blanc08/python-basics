data = [5, 19, 20, 250, 10, 40, 2, 3, 4, 5]

# count | menghitung jumlah value
jumlah = data.count(5)
print(jumlah)
print("===============")

# get index
index = data.index(5)  # kalau datanya ga ada akan error
print(index)
print("===============")

# sort | mengurutkan | jika string, akan diurutkan berdasarkan alphabet
print("sebelum = ", data)
sorted = data.sort()
print("setelah = ", data)
print("variable = ", sorted)  # ga ngebalikin apa", lansung ngerubah list aslinya
print("===============")

# reverse | sort kebalik
print("sebelum = ", data)
data.sort()
data.reverse()
print("setelah = ", data)
print("===============")
