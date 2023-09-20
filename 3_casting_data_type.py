# casting adalah proses mengkonversi dari satu tipe data ke tipe data lainnya


## Integer
variable_integer = 5
print("data = ", variable_integer, ", type = ", type(variable_integer))
# int to float
variable_float = float(variable_integer)
print("data = ", variable_float, ", type = ", type(variable_float))
# int to boolean => 0 adalah false, selain itu akan menjadi true
variable_boolean = bool(variable_integer)
print("data = ", variable_boolean, ", type = ", type(variable_boolean))
# int to string
variable_string = str(variable_integer)
print("data = ", variable_string, ", type = ", type(variable_string))
print("==================================================================")

## Float
variable_float = 5.4
print("data = ", variable_float, ", type = ", type(variable_float))
# float to int
variable_int = int(variable_float)
print("data = ", variable_int, ", type = ", type(variable_int))
# float to boolean => 0 adalah false, selain itu akan menjadi true
variable_boolean = bool(variable_float)
print("data = ", variable_boolean, ", type = ", type(variable_boolean))
# float to string
variable_string = str(variable_float)
print("data = ", variable_string, ", type = ", type(variable_string))
print("==================================================================")


## Boolean
variable_boolean = True
print("data = ", variable_boolean, ", type = ", type(variable_boolean))
# boolean to int
variable_int = int(variable_boolean)
print("data = ", variable_int, ", type = ", type(variable_int))
# boolean to float
variable_float = float(variable_boolean)
print("data = ", variable_float, ", type = ", type(variable_float))
# boolean to string
variable_string = str(variable_boolean)
print("data = ", variable_string, ", type = ", type(variable_string))
print("==================================================================")

## string
variable_string = "string"
print("data = ", variable_string, ", type = ", type(variable_string))
# string to int || hanya bisa ter convert jika string adalah angka || ex => '10'
variable_int = int(variable_string)
print("data = ", variable_int, ", type = ", type(variable_int))
# string to float || hanya bisa ter convert jika string adalah angka || ex => '10'
variable_float = float(variable_string)
print("data = ", variable_float, ", type = ", type(variable_float))
# string to boolean || string apapun dibaca true, sedangkan string kosong akan menjadi false  # noqa: E501
variable_boolean = bool(variable_string)
print("data = ", variable_boolean, ", type = ", type(variable_boolean))
print("==================================================================")
