Nota1 = float(input("Nota #1: "))
Nota2 = float(input("Nota #2: "))
Nota3 = float(input("Nota #3: "))
NotaFinal = float(input("Examen Final: "))
TrabajoFinal = float(input("Trabajo Final: "))
NotaFinalPromedio = (((Nota1 + Nota2  + Nota3)/3) * 0.55) 
ExamenFinal = NotaFinal * 0.30
TrabFinal = TrabajoFinal * 0.15
ValorFinal = ExamenFinal + TrabFinal + NotaFinalPromedio
print("La nota final es igual a: ")
print("{:.2f}".format(ValorFinal))

