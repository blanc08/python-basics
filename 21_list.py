# list
variable_list = [1, 2, 3, 4, 5, "5"]
print(variable_list)


# cara alternatif
variable_list = list(range(1, 10))
print(variable_list)

# for loop
variable_list = [i for i in range(0, 10)]
print(variable_list)

# for loop di kuadrat
variable_list = [i**2 for i in range(0, 10)]
print(variable_list)


# # for if
variable_list = [i for i in range(0, 10) if i != 5]
print(variable_list)

# for if | genap
variable_list = [i for i in range(0, 10) if i % 2 == 0]
print(variable_list)
