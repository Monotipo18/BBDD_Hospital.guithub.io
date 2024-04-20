from pruebas_Login import *
print("-"*50)
print(" " * ((50 - len("Menú Login")) // 2) + "Menú Login")
print("-"*50)
print("\n")
print("1. Iniciar Sesión")
print("2. Registrar-se")
print("3. Salir")
Centinela=True
Crear_csv()
while Centinela:
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        USUARIO=input("Introduce tu Usuario: ")
        CONTRASEÑA=pwinput.pwinput("Introduce tu Contraseña: ")
        Login(USUARIO,CONTRASEÑA)
        Centinela=False
    elif opcion == "2":
        USUARIO=input("Introduce tu Usuario: ")
        CONTRASEÑA=pwinput.pwinput("Introduce tu Contraseña: ")
        Registro(USUARIO,CONTRASEÑA)
    elif opcion == "3":
        print("Saliendo del programa...")
        Centinela=False
    else:
        print("Opcion invalida")
