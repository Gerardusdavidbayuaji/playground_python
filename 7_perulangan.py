# looping = akan mengulang sampai kondisinya terpenuhi
# percabangan = mengambil 1 kondisi

# for kondisi:
# aksi

# __FOR IN__
# 1. menggunakan list 

# angka_list = [0, 3, 6, 9, 12]

# for i in angka_list:
#     print(f'ini adalah angka :', i)
# print('program selesai \n')

# 2. menggunakan range

# for j in range(10):
#     print('ini adalah angka :', j)
# print('program selesai \n')

# __WHILE LOOP__
# angka = 0

# while angka < 5:
#     angka += 1
#     print('ini adalah angka :', angka)

# __CONTINUE, PASS, BREAK__

# 1. pass > tidak akan dieksekusi

# angka = 0 

# while angka < 5:
#     angka += 1
    
#     if angka == 3:
#         pass

#     print(angka)

# 2. continue > akan meloncat ke step selanjutnya

angka = 0 
while angka < 10:
    angka += 1
    print('heyyy', angka) #aksi 1

    if angka == 5:
        ('hello world')
        continue #akan membuat loop meloncat ke stap selanjutnya

    print('learning python') #aksi 1

print('program stop')