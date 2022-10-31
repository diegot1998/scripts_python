Nota1 = float(input("Nota #1: "))
Nota2 = float(input("Nota #2: "))
Nota3 = float(input("Nota #3: "))
NotaFinal = float(input("Examen Final: "))
NotaFinalPromedio = (((Nota1 + Nota2  + Nota3)/3) * 0.55) 
ExamenFinal = NotaFinal * 0.30
NotaNecesaria = (3.0 - ExamenFinal -NotaFinalPromedio) / 0.15
print("La nota necesaria para ganar la meteria es igual a: ")
print("{:.2f}".format(NotaNecesaria))
