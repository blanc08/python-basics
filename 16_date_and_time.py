import datetime as dt

# tanggal_lahir = dt.date(2001, 10, 8)
# print(tanggal_lahir)

# print(f"hari ini adalah hari {dt.date.today():%A}")

tanggal = int(input("Tanggal \t:"))
bulan = int(input("bulan \t:"))
tahun = int(input("tahun \t:"))

tanggal_lahir = dt.date(tahun, bulan, tanggal)

print(tanggal_lahir)

umur = dt.date.today() - tanggal_lahir

print(f"umur anda = {umur.days // 356} tahun")
