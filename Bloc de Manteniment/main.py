'''
grupomaviunal
uN@i3st4fu3rtE
'''
import time
from Funciones_Login import *
from Funciones_Menu import *
from Funciones_sql import *
from dotenv import load_dotenv
import pwinput
load_dotenv()
contraseña_adm = os.getenv("CONTRASEÑA_ADM")
hash_adm=generate_password_hash(contraseña_adm, method='pbkdf2:sha256')




def main(administrador=False):
    contador_pass = 0
    if not administrador:
        menu_login()
    else:
            
        contraseña_administrador = pwinput.pwinput("Introduce una contraseña: ")        
        while not check_password_hash(hash_adm, contraseña_administrador):
            if contador_pass == 2:
                print("Has superado el número de intentos")
                exit()
            else:
                print("Contraseña incorrecta (Vuelva a introducir la contraseña)")
                contraseña_administrador = pwinput.pwinput("Introduce una contraseña: ")
                contador_pass = contador_pass+1
        menu_login_adm()  



    Centinela = True
    Centinela2 = True
    Crear_csv()

    while Centinela:
        opcion = input("AAASeleccione una opción: ")
        if opcion == "1":
            USUARIO = input("Introduce tu Usuario: ")
            CONTRASEÑA = pwinput.pwinput("Introduce tu Contraseña: ")
            Comprobacion = Login(USUARIO, CONTRASEÑA)         
            if Comprobacion:
                    if administrador:
                        menu_gestio_hospital_adm()
                        opcion_adm = input("Seleccione una opción: ")   
                        while Centinela2:
                            if opcion_adm == "1":
                                menu_manteniments_adm()
                                opcion = input("Seleccione una opción: ")
                                if opcion == "1":
                                    USUARIO = input("Introduce el Usuario: ")
                                    CONTRASEÑA = pwinput.pwinput("Introduce la Contraseña: ")
                                    TIPUS = input("Introduce el tipo de trabajador (Medico infermer/a celador conductor d'ambulancies Administratius): ")
                                    Registro(USUARIO, CONTRASEÑA, TIPUS)
                                elif opcion == "2":
                                    USUARIO = input("Introduce el Usuario: ")
                                    CONTRASEÑA = pwinput.pwinput("Introduce la Contraseña: ")
                                    Registro(USUARIO, CONTRASEÑA, "PACIENTS")
                                elif opcion == "3":
                                    Centinela = False
                                    Centinela2 = False
                                else:
                                    print("Opción inválida")
                            elif opcion_adm == "2":
                                Centinela2 = False
                                Centinela = False
                    else:
                        while opcion!="4":
                            menu_gestio_hospital()
                            opcion = input("Seleccione una opción: ")
                            if opcion == "1":
                                menu_manteniments()
                                opcion_mnt = input("Seleccione una opción: ")
                                if opcion_mnt == '1':
                                    DNI_Infermera=input("Introduce el DNI de la Infermera: ")
                                    select_personal_infermeria(DNI_Infermera)
                                    time.sleep(3)
                                elif opcion_mnt == '2':
                                    Fecha_Operacion=input("Introduce la fecha de la Operacion (YYYY-MM-DD): ")
                                    obtener_operaciones_por_quirofano(Fecha_Operacion)
                                    time.sleep(3)
                                elif opcion_mnt == '3':
                                    Fecha_VisitaProgramada=input("Introduce la fecha de la Visita Programada (YYYY-MM-DD): ")
                                    obtener_visitas_programadas_por_dia(Fecha_VisitaProgramada)
                                    time.sleep(3)
                                elif opcion_mnt=="4":
                                    num_habitacion=input("Introduce el numero de habitación: ")
                                    obtener_reservas_por_habitacion(num_habitacion)
                                    time.sleep(3)
                                elif opcion_mnt=="5":
                                    dni_paciente=input("Introduce el DNI del paciente: ")
                                    obtener_informacion_paciente(dni_paciente)
                                    time.sleep(3)
                                elif opcion_mnt=="6":
                                    Todos_Los_Quirofanos=input("Para todos los quirofanos (S/N): ")
                                    if Todos_Los_Quirofanos.upper()=="S":
                                        obtener_equipos_por_quirofano()
                                    if Todos_Los_Quirofanos.upper()=="N":
                                        Numero_Quirofano=input("Introduce el numero de quirófano: ")
                                        obtener_equipos_por_quirofano(Numero_Quirofano)

                                    time.sleep(3)
                                elif opcion_mnt=="7":
                                    dni_medico=input("Introduce el DNI del medico: ")
                                    obtener_informacion_medico(dni_medico)
                                    time.sleep(3)
                                elif opcion_mnt=="8":
                                    print("Saliendo del progrma")
                            elif opcion  == "4":
                                print("Saliendo del progrma")  
                                Centinela =  False                      
            elif opcion == "2":
                print("Saliendo del programa...")
                Centinela = False
            else:
                print("Opción inválida")
        elif opcion == "2":
            Centinela = False
if __name__ == "__main__":
    tipo_usuario = input("Eres administrador? (S/N) ")
    if tipo_usuario.lower() == "s":
        main(administrador=True)
    elif tipo_usuario.lower() == "n":
        main()
    else:
        print("Tipo de usuario no válido.")