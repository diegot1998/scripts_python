Sueldo = int(input("Ingrese el valor del sueldo: "))
if Sueldo > 3000:
    print("Debe de abonar impuestos")
    impuesto = int((Sueldo * 10)/100)
    Saldopagar = Sueldo - impuesto
    print("El saldo a pagar es de: ")
    print(Saldopagar)
    print("El impuesto para el estado es de: ")
    print(impuesto)
else:
    print("No se hace descuento, su salario es: ")
    print(Sueldo)