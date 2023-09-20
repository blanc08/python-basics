# string
variable_string = "contoh string"
print("tipe data dari variable_string adalah : ", type(variable_string))

# integer
variable_integer = 4
print("tipe data dari variable_integer adalah : ", type(variable_integer))

# float
variable_float = 4.1
print("tipe data dari variable_float adalah : ", type(variable_float))

# float
variable_boolean = True
print("tipe data dari variable_boolean adalah : ", type(variable_boolean))

# integer_string
variable_integer_string = "10"
print("tipe data dari variable_integer_string adalah : ", type(variable_integer_string))


## tipe data khusus
#
# bilangan complex, ex => 5x + 6i
variable_data_complex = complex(5, 6)
print("tipe data dari variable_data_complex adalah : ", type(variable_data_complex))

# tipe data dari bahasa C

# c_double
from ctypes import c_double

variable_c_double = c_double(10.5)
print(
    "tipe data dari variable_c_double yang ber value :",
    variable_c_double,
    " adalah : ",
    type(variable_c_double),
)
