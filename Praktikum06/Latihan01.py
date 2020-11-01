#Latihan membuat function pythagoras

def isPythagoras(a, b, c) :
    if((a*a) == (c*c) - (b*b) or (b*b) == (c*c) - (a*a) or (c*c) == (b*b) + (a*a)) :
        print(True)
    else :
        print(False)

a = 3
b = 4
c = 5

isPythagoras(a,b,c)

#-----------------

x = 5
y = 9
z = 12

isPythagoras(x,y,z)

#-----------------

k = 8
l = 6
m = 10

isPythagoras(k,l,m)

#-----------------

d = 7
e = 8
f = 11

isPythagoras(d,e,f)
