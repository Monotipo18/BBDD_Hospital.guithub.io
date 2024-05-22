#1
def menu_paciente():
    print("-"*50)
    print(" " * ((50 - len("Menu Pacient")) // 2) + "Menu Pacient")
    print("-"*50)
    print("\n")
    print("1. Informació Personal")
    print("2. Consulta De visites")
    print("3. Reserves d'habitacions")
    print("4. Operacions pendents")
    print("5. Sortir")
#2
def menu_Metge():
    print("-"*50)
    print(" " * ((50 - len("Menu Metge")) // 2) + "Menu Metge")
    print("-"*50)
    print("1. Visitas Programadas")
    #Informe_nombre_visites_ateses_per_data
    print("2. Informació Pacient")
    #obtener_informacion_paciente
    print("3. Informació Infermera asignat")
    #medico_personal_infermeria
    print("4. Informe maltés més comuns")
    #Malalties_mes_comunes
    print("5. Sortir")

    
def menu_Infermeres():
    print("-"*50)
    print(" " * ((50 - len("Menu Infermeres")) // 2) + "Menu Infermeres")
    print("-"*50)
    print("1. Informació Metge/Planta asignat")
    #select_personal_infermeria

def menu_zelador():
    print("-"*50)
    print(" " * ((50 - len("Menu Celador")) // 2) + "Menu Celador")
    print("-"*50)
    print("1. Informació de les habitacions reservades.")
    #obtener_reservas_por_habitacion
    print("2. Informació dels aparells mèdics")
    #obtener_equipos_por_quirofano
    print("3. Sortir")
    


def menu_administrador():
    print("-"*50)
    print(" " * ((50 - len("Menu administrador")) // 2) + "Menu administrador")
    print("-"*50)
    print("1. Manteniments")
    print("2. Consultes i informes")
    print("3. Exportacio de dades")
    print("5. Dummy data")
    print("6. Logs")
    print("4. Sortir")

def menu_administrador_man():
    print("-"*50)
    print(" " * ((50 - len("Menú de manteniments Administradors")) // 2) + "Menú de manteniments Administradors")
    print("-"*50)
    print("\n")
    print("1. Donar d'alta a nou personal del centre")
    #Registro(USUARIO, CONTRASEÑA,TIPO)
    print("2. Donar d'alta a nou pacient")
    #Registro(USUARIO, CONTRASEÑA,"pacient")
    print("3. Sortir")

def menu_administrador_consultas():
    print("-"*50)
    print(" " * ((50 - len("Menú de consultas Administradors")) // 2) + "Menú de consultas Administradors")
    print("-"*50)
    print("\n")
    print("1. Consulta de les plantes")
    #informacion_de_la_planta
    print("2. Informe de personal")
    #informe_personal
    print("3. Informe de nombre de visites per dia")
    #Informe_nombre_visites_ateses_per_data(usuario, contraseña, data)
    #Informe_nombre_visites_ateses(usuario, contraseña)
    '''Esta son todas o una  por fecha''' #hay que hacer un if i elif
    print("4. Informe Rànquing de Metges amb més pacients atesos")
    #Ranking_metges_mes_pacients(usuario, contraseña)
    print("5. Informe amb les malalties més comunes")
    #Malalties_mes_comunes(usuario, contraseña)
    print("6. Sortir")

def menu_administrador_exportacio():
    print("-"*50)
    print(" " * ((50 - len("Exportació de dades")) // 2) + "Exportació de dades")
    print("-"*50)
    '''Poner el input en el main i borrar esto'''
    #input("Introdueix la ruta del xml: ")

def menu_dummy_data():
    print("-"*50)
    print(" " * ((50 - len("Menú inserció/eliminació de dades Inventades")) // 2) + "Menú inserció/eliminació de dades Inventades")
    print("-"*50)
    print("1. Inserció de dades")
    print("2. Eliminació TOTAL de les dades")
    print("3. Sortir")

def menu_logs():
    print("-"*50)
    print(" " * ((50 - len("Registres de informació vulnerable")) // 2) + "Registres de informació vulnerable")
    print("-"*50)
    print("1. Veure els registres")
    print("2. Sortir")

def menu_login():
    print("-"*50)
    print(" " * ((50 - len("Menú Login")) // 2) + "Menú Login")
    print("-"*50)
    print("\n")
    print("1. Iniciar Sesión")
    print("2. Registrarse")
    print("3. Salir")