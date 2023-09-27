# list methods

# get with index
# index  0(-3)    1(-2)    2(-3)
data = ["bagus", "okta", "viadi"]

print(data[0])
print(data[-1])
print("==============================")

# len
print(len(data))
print("==============================")


# manipulasi
# manipulasi data yang sudah ada
print("data sebelum dimanipulas = ", data)
data[0] = "bagus manipulated"
print("data setelah dimanipulas = ", data)
print("==============================")

# insert
print("data sebelum dimanipulas = ", data)
data.insert(1, "agus")
print("data setelah dimanipulas = ", data)
print("==============================")

# append | menambahkan data di akhir list
print("data sebelum dimanipulas = ", data)
data.append("agus appended")
print("data setelah dimanipulas = ", data)
print("==============================")

# union | merge | extends
data_baru = ["data baru 1", "data baru 2"]
print("data sebelum dimanipulas = ", data)
data.extend(data_baru)
print("data setelah dimanipulas = ", data)
print("==============================")

# remove
print("data sebelum dimanipulas = ", data)
data.remove("agus appended")
# data.remove("tidak ada") # akan error jika data tidak ada di list
print("data setelah dimanipulas = ", data)
print("==============================")

# remove data paling belakang
print("data sebelum dimanipulas = ", data)
data_akhir = data.pop()
print("data setelah dimanipulas = ", data)
print("data yang di pop = ", data_akhir)
print("==============================")
