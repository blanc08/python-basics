# method cpopy biasa hanya akan meng-copy bagian luar dari list.. child list akan tetap
# menempelkan address lamanya
# untuk menghindari ini, kita dapat menggunakan fungsi deepcopy dari copy package
from copy import deepcopy


data_satu = [1, 2]
data_dua = [3, 4]

list_2D = [data_satu, data_dua]

print(f" list 2D = {list_2D}")

deep_copy_list = deepcopy(list_2D)
print(f" list 2D = {deep_copy_list}")
