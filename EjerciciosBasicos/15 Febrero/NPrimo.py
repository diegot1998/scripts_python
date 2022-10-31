x = 2
z=4
while x <= 100:
    if x%2 == 0 or x%3 == 0 or x%5 == 0 or x%7 == 0:
        if x == 2 or x == 3 or x == 5 or x == 7:
            print(x, 'Es un numero primo')
    else:
        print(x, 'Es un numero primo')  
        z= z+1
    x = x+1


