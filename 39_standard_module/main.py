from collections import Counter
import datetime

waktu = datetime.datetime.now()
print(f"data waktu -> {waktu}")
print(f"data tahun -> {waktu.year}")

data = ["a", "b", "c", "a", "d", "e", "c", "a"]

counts = Counter(data)

print(counts.get("a"))

hasil_file = open("./text.txt", "r")
print(hasil_file.read())
