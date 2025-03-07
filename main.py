import pickle
from estudiante import Estudiante


estudiantes = []


cursos = {
    "Matemáticas": [],
    "Ciencias": [],
    "Historia": [],
    "Programación": []
}

def guardar_datos():
    with open("estudiantes.pkl", "wb") as file:
        pickle.dump((estudiantes, cursos), file)

def cargar_datos():
    global estudiantes, cursos
    try:
        with open("estudiantes.pkl", "rb") as file:
            estudiantes, cursos = pickle.load(file)
    except FileNotFoundError:
        pass

def mostrar_menu():
    print("\n----- MENÚ -----")
    print("1. Registrar nuevo estudiante")
    print("2. Ver estudiantes registrados")
    print("3. Matricular estudiante en un curso")
    print("4. Ver cursos y sus estudiantes")
    print("5. Guardar y salir")

def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            break
        except ValueError:
            print("Por favor, ingrese una edad válida.")
    direccion = input("Ingrese la dirección del estudiante: ")
    estudiante = Estudiante(nombre, edad, direccion, "No matriculado")
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} registrado con éxito.")

def ver_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("\n----- Estudiantes Registrados -----")
        for estudiante in estudiantes:
            print(estudiante)

def matricular_estudiante():
    if not estudiantes:
        print("No hay estudiantes para matricular.")
        return
    print("\nEstudiantes disponibles:")
    for i, estudiante in enumerate(estudiantes, 1):
        print(f"{i}. {estudiante.get_nombre()}")
    try:
        opcion = int(input("Seleccione un estudiante por número: ")) - 1
        if 0 <= opcion < len(estudiantes):
            print("Cursos disponibles:")
            for i, curso in enumerate(cursos.keys(), 1):
                print(f"{i}. {curso}")
            curso_opcion = int(input("Seleccione un curso por número: ")) - 1
            if 0 <= curso_opcion < len(cursos):
                curso_seleccionado = list(cursos.keys())[curso_opcion]
                estudiantes[opcion].set_curso(curso_seleccionado)
                cursos[curso_seleccionado].append(estudiantes[opcion])
                print(f"Estudiante {estudiantes[opcion].get_nombre()} matriculado en {curso_seleccionado}.")
            else:
                print("Opción de curso inválida.")
        else:
            print("Opción de estudiante inválida.")
    except ValueError:
        print("Entrada no válida. Debe ser un número.")

def ver_cursos():
    print("\n----- Cursos y sus estudiantes -----")
    for curso, lista in cursos.items():
        print(f"\nCurso: {curso}")
        if lista:
            for estudiante in lista:
                print(f" - {estudiante.get_nombre()}")
        else:
            print(" No hay estudiantes matriculados.")

def main():
    cargar_datos()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            registrar_estudiante()
        elif opcion == '2':
            ver_estudiantes()
        elif opcion == '3':
            matricular_estudiante()
        elif opcion == '4':
            ver_cursos()
        elif opcion == '5':
            guardar_datos()
            print("Datos guardados. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
