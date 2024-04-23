# manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = 'hape'
nama_kedua = 'botol'
nama_akhir = 'kabel'

nama = nama_pertama +" "+ nama_kedua +" "+ nama_akhir
print(nama)

# 2. menghitung panjang karakter
panjang = len(nama)
print('panjang dari ' + nama + " = " + str(panjang))

# 3. mengecek apakah ada karakter atau string di string (in | not in)
d = "b"
is_status = d in nama
print(d + " ada di " + nama + " = " + str(is_status))

a = "z"
is_status = a not in nama
print(a + " tidak ada di " + nama + " = " + str(is_status))

# 4. mengulang string
print("wk"*10)

# 5. indexing
print("index ke 2", nama[2])

# 6. item paling kecil dan besar
print("paling kecil :" + min(nama))
print("paling besar :" + max(nama))

ascii_code = ord("a")
print("ascii code untuk spasi adalah" + str(ascii_code))

data = 197
print("char untuk ascii 197 adalah" + chr(data))

# 7. operator dalam bentuk method

data = 'hallo world'
jumlah = data.count("o")
print('jumlah o dalam ' + data + " = " + str(jumlah))

# 8. pengecekan dengan isX method

# contoh pengecekan lower case
salam = 'hallo world'
jawab = salam.islower()
print(str(jawab))

# contoh pengecekan upper case
salam = 'hallo world'
jawab = salam.isupper()
print(str(jawab))

# isalpha() > untuk mengecek semuanya huruf
# isalnum() > untuk mengecek huruf dan angka
# isdecimal() > untuk mengecek angka saja
# isspace() > untuk mengecek spasi, tab, newline \n
# istitle() > untuk mengecek semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orang Kaya"
cek_judul = judul.istitle() #hasil boolean
print(str(cek_judul))

# 9. ngecek komponen startwith() endwith() 
cek_start = "hallo world".startswith("hallo")
print(str(cek_start))

cek_end = "hallo world".startswith("world")
print(str(cek_end))

nama_siswa = ['udin', 'yanto', 'asep']
print(nama_siswa)

gabungan = ', '.join(nama_siswa)
print(gabungan)

# 10. format string
user = 1902
format_str = f'{user}'
print(format_str)

harga = 10000
jumlah_barang = 5

format_string = f'harga total = {harga*jumlah_barang}'
print(format_string)