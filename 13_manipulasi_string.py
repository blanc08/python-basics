first_name = "Bagus"
last_name = "Oktaviadi"
full_name = first_name + " " + last_name
print(full_name)

# method length | len
print(len(full_name))

# includes | check karakter | case-sensitive
ada_ga = "B" in full_name
print(ada_ga)


# not | exclude
ada_ga = "B" not in full_name
print(ada_ga)

# mengulang string
print("wk" * 20)


# indexing => bahas lagi di slice | array | list
print(full_name[0])

# indexing dengan range
# misal 0 sampai 4
print(full_name[0:3])

# max and min
(print(min(full_name)))
(print(max(full_name)))

ascii_code = ord("a")
print(str(ascii_code))

# string method
uppercased = full_name.upper()
print(uppercased)
