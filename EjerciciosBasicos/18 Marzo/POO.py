class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Libre")


# bloque principal

for x in range (0,1):
    AlumnN = input("Ingrese el nombre: ")
    AlumnoE = int(input("Ingrese la nota: "))
    alumno1=Alumno()
    alumno1=Alumno()
    alumno1.inicializar(AlumnN,AlumnoE)
    alumno1.imprimir()
    alumno1.mostrar_estado()

