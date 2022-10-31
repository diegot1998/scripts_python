CantidadPreguntas = int(input("Ingrese la cantidad de preguntas realizadas: "))
CantidadPreguntasCorrectas = int(input("Ingrese la cantidad de preguntas que contesto correctamente: "))
PorcentajePreguntas = (CantidadPreguntasCorrectas/CantidadPreguntas)*100
if PorcentajePreguntas >= 90:
    print("Usted esta en el nivel maximo y su porcentaje es igual a: ")
    print(PorcentajePreguntas)
else:
    if PorcentajePreguntas >= 75 and PorcentajePreguntas < 90:
        print("Usted esta en el nivel medio y su porcentaje es igual a: ")
        print(PorcentajePreguntas)
    else:
        if PorcentajePreguntas >= 50 and PorcentajePreguntas < 75:
            print("Usted esta en el nivel regular y su porcentaje es igual a: ")
            print(PorcentajePreguntas)
        else:
            if PorcentajePreguntas < 50:
                print("Usted esta fuera de nivel y su porcentaje es igual a: ")
                print(PorcentajePreguntas)