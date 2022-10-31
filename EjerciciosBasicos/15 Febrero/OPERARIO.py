Sueldo = float(input("Ingrese el valor del sueldo: "))
AA = int(input("Ingrese los años de antiguedad: "))
if Sueldo < 500 and AA >= 10:
    TSueldo = (Sueldo * 0.20) + Sueldo 
    print(TSueldo)
else:
    if Sueldo < 500 and AA < 10:
        TSueldo = (Sueldo * 0.05) + Sueldo 
        print(TSueldo)   
    else:
        print("No hay ningun cambio en el sueldo: ", Sueldo)

