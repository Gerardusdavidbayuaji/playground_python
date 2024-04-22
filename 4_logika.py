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

