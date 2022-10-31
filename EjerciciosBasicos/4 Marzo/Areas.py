def ACuadrado(Valor):
    Area = Valor * Valor
    print("El area del cuadrado es: ", Area)
def ATriangulo(valor, valor1):
    Area = (valor * valor1)/2
    print("El area del triangulo es: ", Area)
def ATrapecio(valor, valor1, valor2):
    Area = ((valor1+valor2)/2)*valor
    print("El area del trapecio es: ", Area)
def ARectangulo(valor, valor1):
    Area = valor * valor1
    print("El area del rectangulo es: ", Area)
def AParalelograma(valor, valor1):
    Area = valor * valor1
    print("El area del paralelograma es: ", Area)
def Areas(Decision):
    if Decision == "cuadrado":
        Valor1 = int(input("Ingrse el valor del lado: "))
        ACuadrado(Valor1)
    elif Decision == "triangulo":
        Valor1 = int(input("Ingrse el valor de la altura: "))
        Valor2 = int(input("Ingrse el valor de la base: "))
        ATriangulo(Valor1, Valor2)
    elif Decision == "trapecio":
        Valor1 = int(input("Ingrse el valor de la altura: "))
        Valor2 = int(input("Ingrse el valor de la base 1: "))
        Valor3 = int(input("Ingrse el valor de la base 2: "))
        ATrapecio(Valor1, Valor2, Valor3)
    elif Decision == "rectangulo":
        Valor1 = int(input("Ingrse el valor de la lado 1: "))
        Valor2 = int(input("Ingrse el valor de la lado 2: "))
        ARectangulo(Valor1, Valor2)
    elif Decision == "paralelograma":
        Valor1 = int(input("Ingrse el valor de la altura: "))
        Valor2 = int(input("Ingrse el valor de la base: "))
        AParalelograma(Valor1, Valor2)
    else:
        print("La respuesta no es valida")
        Areas(Decision)
Dec = input("Ingrese la figura geometrica: ")
Areas(Dec)