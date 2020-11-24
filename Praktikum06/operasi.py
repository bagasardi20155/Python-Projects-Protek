from operation import *


a = 10
b = 7
print(a, '+', b, '=', jumlah(a,b))
print(a, '-', b, '=', kurang(a,b))
print(a, '*', b, '=', kali(a,b))
print(a, '/', b, '=', bagi(a,b))


#----------------------------------- nomer a -----------------------------------

x = kali(4,6)
y = jumlah(2,x)
z = kurang(y,4)

print(z)


#----------------------------------- nomer b -----------------------------------

k = jumlah(4,7)
l = kurang(6,9)
m = kali(k,l)

print(m)


#----------------------------------- nomer c -----------------------------------

a = jumlah(10,2)
b = jumlah(7,5)
c = kurang(12,34)
d = bagi(a,b)
e = bagi(d,c)

print(e)
