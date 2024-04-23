# __BOOLEAN__
# NOT
# operator 'not' digunakan untuk membalikan nilai kebenran dari suatu ekspresi bolen
# a = True
# c = not a

# print(a)
# print(c)

# OR
# operator 'or', jika salah satu true, maka hasilnya adalah true 
# a = False
# b = False
# c = a or b 
# print(a, 'OR', b, '=', c)

# a = False
# b = True
# c = a or b 
# print(a, 'OR', b, '=', c)

# a = True
# b = False
# c = a or b 
# print(a, 'OR', b, '=', c)

# a = True
# b = True
# c = a or b 
# print(a, 'OR', b, '=', c)

# AND
# operator 'and', jika nilainya true, maka hasilnya adalah true 
# a = False
# b = False
# c = a and b 
# print(a, 'and', b, '=', c)

# a = False
# b = True
# c = a and b 
# print(a, 'and', b, '=', c)

# a = True
# b = False
# c = a and b 
# print(a, 'and', b, '=', c)

# a = True
# b = True
# c = a and b 
# print(a, 'and', b, '=', c)

# XOR
# operator 'xor', akan true jika salah satunya true 
# a = False
# b = False
# c = a ^ b 
# print(a, 'xor', b, '=', c)

# a = False
# b = True
# c = a ^ b 
# print(a, 'xor', b, '=', c)

# a = True
# b = False
# c = a ^ b 
# print(a, 'xor', b, '=', c)

# a = True
# b = True
# c = a ^ b 
# print(a, 'xor', b, '=', c)

# __KOMPARASI DAN LOGIKA__

# inputData = float(input("masukan data kurang dari tiga dan lebih dari 10:"))

# # +++3---10+++
# isKurangDari = (inputData <=3)
# print("kurang dari 3:", isKurangDari)

# isLebihDari = (inputData >=10)
# print("lebih dari 10:", isLebihDari)

# isCorrect = isKurangDari or isLebihDari
# print("angka yang anda masukan:", isCorrect)

# inputData = float(input("masukan nilai diantara 3 dan 10:"))

# isKurangDari = (inputData >=3)
# print('nilai kurang dari 3:', isKurangDari)

# isLebihDari = (inputData <=10)
# print('nilai kurang dari 10:', isLebihDari)

# isCorrect = isKurangDari and isLebihDari
# print('masukan nilai:', isCorrect)

# Latihan soal, buat kode menjadi:
# 1. ---0+++5---8+++11---

# inputUser = float(input("masukan data >0, <5, >8, <11 :"))

# isLebihDariNol = (inputUser >0)
# print("nilai lebih dari 0 adalah:", isLebihDariNol)

# isKurangDariLima = (inputUser <5)
# print("nilai kurang dari 5 adalah:", isKurangDariLima)

# isLebihDariLapan = (inputUser >8)
# print("nilai kurang dari 5 adalah:", isLebihDariLapan)

# isKurangDariSebelas = (inputUser <11)
# print("nilai kurang dari 5 adalah:", isKurangDariSebelas)

# isCorrect = isLebihDariNol and isKurangDariLima and isLebihDariLapan and isKurangDariSebelas
# print('nilai anda saat ini adalah', isCorrect)

# __OPERATOR BITWISE__
# bitwise > masing masing bit
# int -> 2 = 00000010/ indeks dari binary (76543210) -> 2^1 =2
# a = 9
# print('nilai:', a , 'binary:', format(a, '08b'))

# __OPERATOR ASSIGNMENT__
# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 #adalah assigment
print('nilai a =', a)

a += 1 #artinya adalah a = a + 1
print('nilai a hasil penjumlahan =', a)

a -= 2 #artinya adalah a = a - 2
print('nilai a hasil pengurangan =', a)

a *= 5 #artinya adalah a = a * 5
print('nilai a hasil perkalian =', a)

a /= 2 #artinya adalah a = a / 2
print('nilai a hasil pembagian =', a)