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

inputUser = float(input("masukan data >0, <5, >8, <11 :"))

isLebihDariNol = (inputUser >0)
print("nilai lebih dari 0 adalah:", isLebihDariNol)

isKurangDariLima = (inputUser <5)
print("nilai kurang dari 5 adalah:", isKurangDariLima)

isLebihDariLapan = (inputUser >8)
print("nilai kurang dari 5 adalah:", isLebihDariLapan)

isKurangDariSebelas = (inputUser <11)
print("nilai kurang dari 5 adalah:", isKurangDariSebelas)

isCorrect = isLebihDariNol and isKurangDariLima and isLebihDariLapan and isKurangDariSebelas
print('nilai anda saat ini adalah', isCorrect)
