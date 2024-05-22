
import time
from Funciones_Login import *
from Funciones_Menu import *
from Funciones_sql import *
from insercion_de_datos import *
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
            
        contraseña_administrador = pwinput.pwinput("Introdueix una contrasenya: ")        
        while not check_password_hash(hash_adm, contraseña_administrador):
            if contador_pass == 2:
                print("Has superat el nombre d'intents")
                exit()
            else:
                print("Contrasenya incorrecta (Torni a introduir la contrasenya)")
                contraseña_administrador = pwinput.pwinput("Introduce una contraseña: ")
                contador_pass = contador_pass+1
        menu_login_adm()  



    Centinela = True
    Centinela2 = True


    while Centinela:
        opcion = input("Seleccioni una opció: ")
        if opcion == "1":
            USUARIO = input("Introdueix el teu Usuari: ")
            CONTRASEÑA = pwinput.pwinput("Introdueix la teva Contrasenya: ")
            Comprobacion = login(USUARIO, CONTRASEÑA)         
            if Comprobacion:
                    if administrador:
                        menu_gestio_hospital_adm()
                        opcion_adm = input("Seleccioni una opció: ")   
                        while Centinela2:
                            if opcion_adm == "1":
                                menu_manteniments_adm()
                                opcion = input("Seleccioni una opció: ")
                                if opcion == "1":
                                    USUARIO = input("Introdueix el teu Usuari: ")
                                    CONTRASEÑA = pwinput.pwinput("Introduce la Contraseña: ")
                                    TIPUS = input("Introduce el tipo de trabajador (Medico infermer/a celador conductor d'ambulancies Administratius): ")
                                    Registro(USUARIO, CONTRASEÑA, TIPUS)
                                elif opcion == "2":
                                    USUARIO = input("Introdueix el teu Usuari: ")
                                    CONTRASEÑA = pwinput.pwinput("Introdueix la Contrasenya: ")
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
                        while opcion!="5":
                            menu_gestio_hospital()
                            opcion = input("Seleccioni una opció: ")
                            if opcion == "1":
                                menu_manteniments()
                                opcion_mnt = input("Seleccioni una opció: ")
                                if opcion_mnt == '1':
                                    DNI_Infermera=input("Introdueix el DNI de la Infermera: ")
                                    select_personal_infermeria(USUARIO,CONTRASEÑA, DNI_Infermera)
                                    time.sleep(3)
                                elif opcion_mnt == '2':
                                    Fecha_Operacion=input("Introdueix la data de la Operacion (YYYY-MM-DD): ")
                                    obtener_operaciones_por_quirofano(USUARIO,CONTRASEÑA,Fecha_Operacion)
                                    time.sleep(3)
                                elif opcion_mnt == '3':
                                    Fecha_VisitaProgramada=input("Introdueix la data de la Visita Programada (YYYY-MM-*DD): ")
                                    obtener_visitas_programadas_por_dia(USUARIO,CONTRASEÑA,Fecha_VisitaProgramada)
                                    time.sleep(3)
                                elif opcion_mnt=="4":
                                    num_habitacion=input("Introdueix el numero d'habitació: ")
                                    obtener_reservas_por_habitacion(USUARIO,CONTRASEÑA,num_habitacion)
                                    time.sleep(3)
                                elif opcion_mnt=="5":
                                    dni_paciente=input("Introdueix el DNI del pacient: ")
                                    obtener_informacion_paciente(USUARIO,CONTRASEÑA,dni_paciente)
                                    time.sleep(3)
                                elif opcion_mnt=="6":
                                    Todos_Los_Quirofanos=input("Per a tots els quirofanos (S/N): ")
                                    if Todos_Los_Quirofanos.upper()=="S":
                                        obtener_equipos_por_quirofano(USUARIO,CONTRASEÑA)
                                    if Todos_Los_Quirofanos.upper()=="N":
                                        Numero_Quirofano=input("Introdueix el numero de quiròfan: ")
                                        obtener_equipos_por_quirofano(USUARIO,CONTRASEÑA,Numero_Quirofano)
                                    time.sleep(3)
                                elif opcion_mnt=="7":
                                    dni_medico=input("Introdueix el DNI del medico: ")
                                    obtener_informacion_medico(USUARIO,CONTRASEÑA,dni_medico)
                                    time.sleep(3)
                                elif opcion_mnt=="8":
                                    print("Sortint del progrma")
                            elif opcion == "2":
                                menu_consultes_informes()
                                opcion = input("Seleccioni una opció: ")
                                if opcion=="1":
                                    Planta=input("Introdueix el numero de planta: ")
                                    informacion_de_la_planta(USUARIO,CONTRASEÑA,Planta)
                                    time.sleep(3)
                                elif opcion=="2":
                                    informe_personal(USUARIO,CONTRASEÑA)
                                    time.sleep(3)
                                elif opcion=="3":
                                    visites=input("Vols totes els visitis(S/N): ")
                                    if visites.upper()=="S":
                                        Informe_nombre_visites_ateses(USUARIO,CONTRASEÑA)
                                        time.sleep(3)
                                    elif visites.upper()=="N":
                                        Data=input("Introdueix la data (YYYY-MM-DD):")
                                        Informe_nombre_visites_ateses_per_data(USUARIO,CONTRASEÑA,Data)
                                        time.sleep(3)
                                    else:
                                        print("hola")
                                    time.sleep(3)
                                elif opcion=="4":
                                    opcion="3"
                                    Ranking_metges_mes_pacients(USUARIO,CONTRASEÑA)
                                    time.sleep(3)
                                elif opcion=="5":
                                    Malalties_mes_comunes(USUARIO,CONTRASEÑA)
                                    time.sleep(3)
                                elif opcion=="6":
                                    print("Sortint del progrma")  
                                    Centinela = False
                                    opcion="4"
                                    Centinela2=False
                                else:
                                    print("Opcion Invalida")
                            elif opcion == "4":
                                menu_dummy_data()
                                opcion_dummy = input("Seleccioni una opció: ")
                                if opcion_dummy == "1":
                                    dummy_data(USUARIO,CONTRASEÑA)
                                elif opcion_dummy == "2":
                                    vaciar_tablas(USUARIO,CONTRASEÑA)
                                elif opcion_dummy == "3":
                                    Centinela = False
                            elif opcion  == "5":
                                print("Sortint del progrma")  
                                Centinela =  False 
                                                 
            elif opcion == "2":
                print("Saliendo del programa...")
                Centinela = False
            else:
                print("Opción inválida")
        elif opcion == "2":
            Centinela = False


if __name__ == "__main__":
    tipo_usuario = input("Ets administrador? (S/N) ")
    if tipo_usuario.lower() == "s":
        main(administrador=True)
    elif tipo_usuario.lower() == "n":
        main()
    else:
        print("Tipus d'usuari no vàlid.")
