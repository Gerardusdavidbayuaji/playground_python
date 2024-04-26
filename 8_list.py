# __LIST__
# list digunakan untuk menyimpan data atau item dalam satu variabel
# list dapat diubah dan diduplikat
# tidak ada array pada python, tapi ada 4 tipe data untuk menyimppan data, yaitu: list, tuple, set, dan dictionary
# contoh: buah = [pisang, anggur, jeruk], indeks [0, 1, 2]

# # kumpulam data integer/number
# data_angka = [0, 1, 2, 3, 5]
# print('ini angka', data_angka)

# # kumpulan data string
# data_string = ['budi', 'udin', 'yanto']
# print('ini string', data_string)

# # kumpulan data boolean
# data_boolean = [False, True, False, False]
# print('ini boolean', data_boolean)

# # kumpulan data campuran
# all_data = [0, 'budi', True]
# print('ini kumpulan data', all_data)

# # cara alternatif membuat list
# data_range = range(0,10) # bisa mengambil data dari fungsi range
# print('ini data range', data_range)

# data_list = list(data_range) #kemudian kondisi range dimapping dalam list
# print('ini data list', data_list)

# # cara menggunakan list menggunakan for loop
# list_for = [i**2 for i in range(0, 10)] # i bisa di pangkatkan (**)
# print('ini nilai list', list_for)

# # cara menggunakan list pake for if
# list_nilai = [i for i in range(0, 10) if i != 6]
# print('ini nilai list kedua', list_nilai)

# __MANIPULASI LIST__
# manipulasi list bisa menggunakan indeks pada item tersebut
# manipulasi list bisa menentukan dari mulai sampai akhir

# menampilkan data yang dipilih dan menghitung banyak data
this_list = ['apple', 'banana', 'cherry']
print(this_list[1])
print(len(this_list))

# menampilkan data tertentu
number_list = ['udin', 'ucup', 'otong', 'budi', 'arman']
print(number_list[2:4])

# mengubah data tertentu
number_list[1] = 'jimmy'
print('number list terkini :', number_list)

# menambahkan data pada akhir list
number_list.append('john')
print('menambahkan nama pada list :', number_list)

# menambahkan list dengan list
number_list.extend(number_list)
print('ini adalah data gabungan :', number_list)

# menghapus data pada list
number_list.remove('otong')
print('ini data yang dihapus :', number_list)
