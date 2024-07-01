# __VARIABEL__ 
# nama_a = "udin"
# print(nama_a)

# __TIPE DATA__
# tipe data standar: integer, float, string, boolean

# tipe data integer: ga ada koma
# data_int = 10
# print("data:", data_int)
# print("bertipe:", type(data_int))

# tipe data float: ada koma
# data_flt = 10.5
# print("data:", data_flt)
# print("bertipe:", type(data_flt))

# tipe data string: kumpulan karakter
# data_str = 'gelas'
# print("data:", data_str)
# print("bertipe:", type(data_str))

# tipe data boolean: biner 0/1 (true/false)
# data_bool = True
# print("data:", data_bool)
# print("bertipe:", type(data_bool))

# __CASTING__
# cara ambil data user, kemudian mengubah menjadi int, float, boolean
# data yang dimasukan pasti string
# data = input("masukan disini:")
# print("data =", data, "type =", type(data))

# jika ingin mengubah menjadi integer atau float:
# angka = int(input("masukan disini:"))
# print("data =", angka, "type =", type(angka))

# angka = float(input("masukan disini:"))
# print("data =", angka, "type =", type(angka))

# jika ingin menggunakan boolean:
# biner = bool(int(input("masukan disini:")))
# print("data =", biner, "type =", type(biner))

# __BOOLEAN__
# NOT
# operator 'not' digunakan untuk membalikan nilai kebenran dari suatu ekspresi bolen
# a = True
# c = not a

# print(a)
# print(c)

# OR
# operator 'or', jika salah satu true, maka hasilnya adalah true 
a = False
b = False
c = a or b 
print(a, 'OR', b, '=', c)

a = False
b = True
c = a or b 
print(a, 'OR', b, '=', c)

a = True
b = False
c = a or b 
print(a, 'OR', b, '=', c)

a = True
b = True
c = a or b 
print(a, 'OR', b, '=', c)

# AND
# operator 'and', jika nilainya true, maka hasilnya adalah true 
a = False
b = False
c = a and b 
print(a, 'and', b, '=', c)

a = False
b = True
c = a and b 
print(a, 'and', b, '=', c)

a = True
b = False
c = a and b 
print(a, 'and', b, '=', c)

a = True
b = True
c = a and b 
print(a, 'and', b, '=', c)

# XOR
# operator 'xor', akan true jika salah satunya true 
a = False
b = False
c = a ^ b 
print(a, 'xor', b, '=', c)

a = False
b = True
c = a ^ b 
print(a, 'xor', b, '=', c)

a = True
b = False
c = a ^ b 
print(a, 'xor', b, '=', c)

a = True
b = True
c = a ^ b 
print(a, 'xor', b, '=', c)





