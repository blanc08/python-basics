# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean
# >, >, <=, >=, ==, !=, is, is not

x = 4
y = 4

# >
print(x > y)
print(x < y)
print(x <= y)
print(x >= y)
print(x == y)
print(x != y)
print(x is y)
print(x is not y)

# advance topic
# variable di python akan dsimpan dalam memory dengan alamat yang dapat dilihat dari
print(hex(id(x)))

# python dapat secara pintar dengan menyimpan primitive variable yang mempunyai value
# yang sama
# misal, a = 4 dan b = 4
# maka, a dan b akan dsimpan di memory yang sama
a = 4
b = 4
print(hex(id(a)), hex(id(b)))

# sebaliknya, jika c = 6 dan d = 7
# makan kedua variable tersebut akan disimpan dimemory yang berbeda oleh python
c = 6
d = 7
print(hex(id(c)), hex(id(d)))

# nah dalam python, comparator "is" dan "is not" membandingkan alamat dimemory komputer,
# atau "komparasi object identity"
# maka dari itu is tidak direkomandasikan untuk membandingkan variable x literal seperti
# x is 4
# print(x is 4)
