h, z, o, y = 0, 0, 0, 1
h = h+y
o = o + h
print(z)
print(h, o)
while h <=10000000 and o <= 10000000:
    h = h+y
    o = o + h
    y= y+h
    z = z+o
    print(h, o)