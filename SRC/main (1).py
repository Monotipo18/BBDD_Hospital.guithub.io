from Login import *

print("-"*50)
print(" " * ((50 - len("Menú Login")) // 2) + "Menú Login")
print("-"*50)
print("\n")
print("1. Inici de sesió")
print("2. Registrar-se")
while True:
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        USUARIO=input("Introduce tu Usuario: ")
        PASWORD=pwinput.pwinput("Introduce tu Contraseña: ")
        Login(USUARIO,PASWORD)
    elif opcion == "2":
        USUARIO=input("Introduce tu Usuario: ")
        PASWORD=pwinput.pwinput("Introduce tu Contraseña: ")
        Registro(USUARIO,PASWORD)
    else:
        print("Opción inválida. Por favor, seleccione nuevamente.")