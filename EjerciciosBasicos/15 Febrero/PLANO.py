for i in range(10):
    x = int(input("Ingrese el valor en x: "))
    y = int(input("Ingrese el valor en y: "))
    if x != 0 and y !=0:
        if x > 0 and y > 0:
            print("El punto se encuentra en el primer cuadrante")
        else:
            if x < 0 and y > 0:
                print("El punto se encuentra en el segundo cuadrante")
            else:
                if x < 0 and y < 0:
                    print("El punto se encuentra en el tercer cuadrante")
                else:
                    print("El punto se encuentra en el cuarto cuadrante")
    else:
        print("Estas en el centro o alguno de los punto corta algun eje")