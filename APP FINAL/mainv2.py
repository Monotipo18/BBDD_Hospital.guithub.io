import os
import time
from Funciones_Login import *
from Funciones_sql import *
from insercion_de_datos import *
from dotenv import load_dotenv
import pwinput
from Funciones_MenuV2 import *
'''
grupomaviunal
uN@i3st4fu3rtE
'''
load_dotenv()
#contraseña_adm = os.getenv("CONTRASEÑA_ADM")
#hash_adm = generate_password_hash(contraseña_adm, method='pbkdf2:sha256')

def main():
    centinela = True
    while centinela:
        menu_login()
        opcion = input("Selecciona una opció: ")
        
        if opcion == "1":
            USUARIO = input("Introdueix el teu Usuari: ")
            CONTRASEÑA = pwinput.pwinput("Introdueix la teva Contrasenya: ")
            Comprobacion = login(USUARIO, CONTRASEÑA) 
            
            if Comprobacion:
                rol_usuario = saber_rol(USUARIO)
                if rol_usuario == 'pacient':
                    menu_paciente()
                    opcion_pac = input("Selecciona una opción: ")
                    
                    if opcion_pac == "1":
                        dni_paciente = input("Introdueix el teu DNI: ")
                        obtener_informacion_paciente(USUARIO, CONTRASEÑA, dni_paciente)
                    
                    elif opcion_pac == "2":
                        fecha = input("Introdueix la data de la visita (YYYY-MM-DD): ")
                        obtener_visitas_programadas_por_dia(USUARIO, CONTRASEÑA, fecha)
                    
                    elif opcion_pac == "3":
                        num_habitacion = input("Introdueix el número d'habitació: ")
                        obtener_reservas_por_habitacion(USUARIO, CONTRASEÑA, num_habitacion)                    
                    elif opcion_pac == "4":
                        dni_paciente = input("Introdueix el teu DNI: ")
                        obtener_informacion_paciente(USUARIO, CONTRASEÑA, dni_paciente)
                    elif opcion_pac == "5":
                        print("Saliendo del sistema...")
                        exit()
                elif rol_usuario == 'medicos':
                    menu_Metge()
                    opcion_met = input("Selecciona una opción: ")
                    if opcion_met == "1":
                        data = input("Introdueix la data desitjada (YYYY-MM-DD): ")
                        Informe_nombre_visites_ateses_per_data(USUARIO, CONTRASEÑA, data)
                    elif opcion_met == "2":
                        nom_pacient = input("Introdueix en nom del pacient: ")
                        obtener_informacion_paciente(USUARIO, CONTRASEÑA, nom_pacient)
                    elif opcion_met == "3":
                        dni_metge = input("Introdueix el teu DNI: ")
                        medico_personal_infermeria(USUARIO, CONTRASEÑA,dni_metge )
                    elif opcion_met == "4":
                        Ranking_metges_mes_pacients(USUARIO, CONTRASEÑA)
                    elif opcion_met == "5":
                        print("Saliendo del sistema...")
                        exit()
                elif rol_usuario == 'enfermeros':
                    menu_Infermeres()
                    opcion_inf = input("Selecciona una opción: ")
                    if opcion_inf == "1":
                        dni_inf = input("Introdueix el teu DNI: ")
                        select_personal_infermeria(USUARIO, CONTRASEÑA, dni_inf)
                elif rol_usuario == 'celador':
                    menu_zelador()
                    opcion_zel = input("Selecciona una opción: ")
                    if opcion_zel == "1":
                        habitacion = input("Introdueix numero d'habitacio: ")
                        obtener_reservas_por_habitacion(USUARIO, CONTRASEÑA, habitacion)
                    elif opcion_zel == "2":
                        aparells_medics = input("Ubicació dels aparells medics: ")  
                        obtener_equipos_por_quirofano(USUARIO, CONTRASEÑA, aparells_medics)
                    elif opcion_zel == "3":
                        print("Saliendo del sistema...")
                        exit()      
                elif rol_usuario == 'administratius':
                    menu_administrador()
                    opcion_adm = input("Selecciona una opción: ")
                    if opcion_adm == "1":
                        menu_administrador_man()
                        opcion_adm_m = input("Selecciona una opción: ")
                        if opcion_adm_m == "1":
                            usuario_nuevo = input("Introdueix el nom del nou usuari: ")
                            contraseña_nueva = input("Introdueix la contrasenya: ")
                            TIPO = input("Quin rol te la persona? 'Medico, Infermer/a, Administratius': ")
                            Registro(USUARIO,CONTRASEÑA,usuario_nuevo, contraseña_nueva,TIPO)
                        if opcion_adm_m == "2":
                            usuario_nuevo = input("Introdueix el nom del pacient: ")
                            contraseña_nueva = input("Introdueix la contrasenya: ")
                            Registro(usuario_nuevo, contraseña_nueva,"pacient")
                        if opcion_adm_m == "3":
                            print("Sortint del programa.")
                            centinela = False
                    if opcion_adm == "2":
                        menu_administrador_consultas()
                        opcion_adm_con = input("Selecciona una opción: ")
                        if opcion_adm_con == "1":
                            planta = input("De quina planta vols l'informació? Introdueix un numero: ")
                            informacion_de_la_planta(USUARIO, CONTRASEÑA, planta)
                        elif opcion_adm_con == "2":
                            print("Informe complet del personal: ")
                            informe_personal(USUARIO, CONTRASEÑA)
                        elif opcion_adm_con == "3":
                            visites=input("Vols saber totes les persones visitades? (S/N): ")
                            if visites.upper()=="S":
                                Informe_nombre_visites_ateses(USUARIO,CONTRASEÑA)
                            elif visites.upper()=="N":
                                Data=input("Introdueix la data (YYYY-MM-DD):")
                                Informe_nombre_visites_ateses_per_data(USUARIO,CONTRASEÑA,Data)
                        elif opcion_adm_con == "4":
                            print("Els metges mes eficients per ordre: ")   
                            Ranking_metges_mes_pacients(USUARIO,CONTRASEÑA)
                        elif opcion =="5":
                            print("Malalties mes comuns: ")
                            Malalties_mes_comunes(USUARIO,CONTRASEÑA)
                        elif opcion == "6":
                            print ("Sortint del programa")
                            centinela = False
                    elif opcion_adm == "3" :
                        menu_administrador_exportacio()
                        ruta_archivo = input("Introdueix la ruta del xml: ")
                        Crear_xml_exportacion(ruta_archivo)
                        fecha_visita1 = input("Introdueix la primera data per l'informe: ")
                        fecha_visita2 = input("Introdueix la segona data per l'informe: ")
                        visitas_entre_fechas(USUARIO,CONTRASEÑA,fecha_visita1, fecha_visita2)
                    elif opcion_adm == "4" :
                        menu_dummy_data()
                        opcion_adm_dumy = input("Selecciona una opción: ")
                        if opcion_adm_dumy == "1":
                            print("Insertan dades")
                            dummy_data(USUARIO, CONTRASEÑA)
                            print("Inserció finalitzada")
                        if opcion_adm_dumy == "2":
                            eliminacio = input("Segur que vols eliminar totes les dades? (S/N)")
                            if eliminacio.lower() == "s":
                                eliminacio2 = input("Segur del tot? (S/N)")
                                if eliminacio2.lower() == "s":
                                    print("Tu mateix.... espero que no et despatxin")
                                    print("Eliminant TOTES les dades")
                                    print("jajajajja,Era broma")
                                    eliminacio3 = input("Estas segur?(S/N)")
                                    if eliminacio3.lower() == "s":
                                        vaciar_tablas(USUARIO, CONTRASEÑA)
                                    elif eliminacio3.lower() == "n":
                                        print("Fa pudor fins aqui")
                                elif eliminacio2.lower() == "n":
                                    print("Sortint del programa")
                                    centinela = False
                            elif eliminacio.lower() =="n":
                                print("Sortin del programa")
                                centinela = False 
                    elif opcion_adm == "5" :
                        menu_logs()
                else:
                    print("Rol no reconegut.")
            else:
                print("Usuari o contrasenya incorrectes.")
        elif opcion == "3":
            print("Saliendo del sistema...")
            centinela = False

if __name__ == "__main__":
    main()