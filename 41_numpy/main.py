import numpy as np

list_a = [1, 2, 3, 4]
vector_a = np.array([1, 2, 3, 4])

print(f"list a -> {list_a}")
print(f"vector a -> {vector_a**2}")

vector_b = np.array([(1, 2), (3, 4)])
print(f"vector b -> \n{vector_b}")
print(f"vector b -> \n{vector_b**2}")

zeros_c = np.zeros((2, 2))
print(f"zeros c -> \n{zeros_c}")

ones_d = np.ones((2, 2))
print(f"ones d -> \n{ones_d}")

jumlah = vector_b + zeros_c + ones_d
print(f"jumlah -> \n {jumlah}")
