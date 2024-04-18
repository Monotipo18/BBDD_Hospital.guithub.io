from Login import *
print("-"*50)
print(" " * ((50 - len("Menú Login")) // 2) + "Menú Login")
print("-"*50)
print("\n")
print("1. Iniciar Sesión")
print("2. Salir")
Centinela=True
Crear_csv()
while Centinela:
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        print("-"*50)
        print(" " * ((50 - len("Inici de Sessio")) // 2) + "Inici de Sessio")
        print("-"*50)
        print("\n")
    
        USUARIO=input("Introduce tu Usuario: ")
        CONTRASEÑA=pwinput.pwinput("Introduce tu Contraseña: ")
        Login(USUARIO,CONTRASEÑA)
        print("Credenciales válidas. Conectando a la base de datos...")            

        print("-"*50)
        print(" " * ((50 - len("Menu Gestio de Hospital")) // 2) + "Menu Gestio de Hospital")
        print("-"*50)
        print("\n")

        print("1. Manteniments")
        print("2. Consultes i informes")
        print("3. Exportacio de Dades")
        print("4. Sortir")
        opcionv2 = input("Seleccione una opcion: ")
        if opcionv2 == "1":
            print("-"*50)
            print(" " * ((50 - len("Menu Gestio de Hospital")) // 2) + "Menu Gestio de Hospital")
            print("-"*50)
            print("1. Donar d'alta nou personal del centre")
            print("2. Donar d'alta un pacient nou")
            print("3. Informacio de les infermeres")
            print("4. Operacions previstes")
            print("5. Visites Planificades")
            print("6. Sortir")
            opcionv3 = input("Seleccione una opcion: ")  
            if opcionv3 == "1":
                 print("-"*50)
                 print(" " * ((50 - len("Tipus Treballador")) // 2) + "Tipus Treballador")
                 print("-"*50)
                 print("\n")
                 print("1. Metge")
                 print("2. Infermer")
                 print("3. Administratiu")
                 print("4. Neteja")
                 tipov2 = input("Seleccione una opcion: ")
                 if tipov2 == "1":
                    USUARIO=input("Introduce tu Usuario: ")
                    CONTRASEÑA=pwinput.pwinput("Introduce tu Contraseña: ")
                    metge(USUARIO,CONTRASEÑA)
                 elif tipov2 == "2":
                    USUARIO=input("Introduce tu Usuario: ")
                    CONTRASEÑA=pwinput.pwinput("Introduce tu Contraseña: ")
                    infermer(USUARIO,CONTRASEÑA)
                 elif tipov2 == "3":
                    USUARIO=input("Introduce tu Usuario: ")
                    CONTRASEÑA=pwinput.pwinput("Introduce tu Contraseña: ")
                    administratiu(USUARIO,CONTRASEÑA)
                 elif tipov2 == "4":
                    USUARIO=input("Introduce tu Usuario: ")
                    CONTRASEÑA=pwinput.pwinput("Introduce tu Contraseña: ")
                    neteja(USUARIO,CONTRASEÑA)
        elif opcionv2 == "2":
            print("-"*50)
            print(" " * ((50 - len("Menu de Consultes e Informes")) // 2) + "Menu de Consultes e Informes")
            print("-"*50)
            print("1. Consulta de les plantes")
            print("2. Informe de personal")
            print("3. Informe de nombre de visites per dia")
            print("4. Sortir")
        elif opcionv2 == "3":
            print("-"*50)
            print(" " * ((50 - len("Exportacio de Dades")) // 2) + "Exportacio de Dades")
            print("-"*50)
    elif opcion == "2":
        print("Saliendo del programa...")
        Centinela=False
    else:
        print("Opcion invalida")
