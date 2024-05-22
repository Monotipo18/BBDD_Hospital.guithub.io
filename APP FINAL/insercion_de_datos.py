import psycopg2
from faker import Faker
import lorem
import random
import string
import datetime
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from Generacion_De_Datos import *
import pdfkit
from Generacion_De_Datos import *
from Funciones_Login import *
# Conéctate a la base de datos PostgreSQL
    # Crea una instancia de Faker
fake = Faker()
def dummy_data(usuario, contraseña):
    conn, cur = login(usuario, contraseña)

# Crea un cursor
    cur = conn.cursor()

# 100k de vistas
    Insercion_Visitas = 100 
# FIN 100k de vistas

# 50K de paciente
    Inserciones_Paciente = 100 #Canviar a 50K
# FIN 50K de paciente

# 100 Medicos
    Inserciones_Medicos = 100
# FIN 100 Medicos

# 200 enfermeros
    Inserciones_enfermeros = 100 #Canviar a 100
    Inserciones_enfermeros_planta = 500
# FIN 200 enfermeros

# 50 personal_Limpieza
    Inserciones_personal_nateja = 50
# FIN 50 personal_Limpieza

# 50 Administradores
    Inserciones_Administradores = 50
# FIN 50 Administradores

# Esto es el extra que hemos querido añadir nosotros. ^.- 
    Insercion_Especilidad = 100
    Insercion_Cita_Medica =  100
    Insercion_Planta = 5
    Insercion_Operacion = 100
    Insercion_Personal_Vari = 70
    Insercion_Quirofano = 25
    Insercion_Habitacion = 100
    Insercion_Reserva_Habitacion = 500
    Insercion_Aparell_Medic = 100
    Insercion_Agenda_Medico = 100
    Insercion_Caracteres_Cirilicos = 100
    Insercion_Reserva_Quirofano = 100


#Tabla paciente
    Lista_ID_Pac = []
    Lista_Nombre_Pac = []
    Lista_Cognom_Pac = []
    Lista_Cognom2_Pac = []
    Lista_DNI_Pac = []
    Lista_Tlf_Pac = []
    Lista_Fecha_Pac = []
    Lista_Sexe_Pac = []
    Lista_num_seg_soc = []
    Generar_Numeros(Inserciones_Paciente, Lista_ID_Pac, inicio=101) #Canviar a 1
    Generar_Nombre(Inserciones_Paciente, Lista_Nombre_Pac)
    Generar_Cognom(Inserciones_Paciente, Lista_Cognom_Pac)
    Generar_Cognom(Inserciones_Paciente, Lista_Cognom2_Pac)
    generar_dni(Inserciones_Paciente, Lista_DNI_Pac)
    Generar_Tlf(Inserciones_Paciente, Lista_Tlf_Pac)
    Generar_Fecha(Inserciones_Paciente, Lista_Fecha_Pac)
    Generar_Caracteres(Inserciones_Paciente, Lista_Sexe_Pac, ["H", "M"])
    generar_tarjeta_sanitaria_catalana(Inserciones_Paciente, Lista_num_seg_soc, Lista_Cognom_Pac, Lista_Cognom2_Pac, Lista_Sexe_Pac ,Lista_Fecha_Pac)

#Tabla paciente Rusos
    Lista_ID_Pac_Rus=[]
    Lista_Nombre_Pac_rus = []
    Lista_Cognom_Pac_rus = []
    Lista_Cognom2_Pac_rus = []
    Lista_DNI_Pac_rus = []
    Lista_Tlf_Pac_rus = []
    Lista_Fecha_Pac_rus = []
    Lista_Sexe_Pac_rus = []
    Lista_TSE_rus = []
    Generar_Numeros(Inserciones_Paciente, Lista_ID_Pac_Rus, inicio = 500000)
    Generar_Nombre_cirilico(Insercion_Caracteres_Cirilicos, Lista_Nombre_Pac_rus)
    Generar_Cognom_cirilico(Insercion_Caracteres_Cirilicos, Lista_Cognom_Pac_rus)
    Generar_Cognom_cirilico(Insercion_Caracteres_Cirilicos, Lista_Cognom2_Pac_rus)
    generar_dni(Insercion_Caracteres_Cirilicos, Lista_DNI_Pac_rus)
    Generar_Tlf(Insercion_Caracteres_Cirilicos, Lista_Tlf_Pac_rus)
    Generar_Fecha(Insercion_Caracteres_Cirilicos, Lista_Fecha_Pac_rus)
    Generar_Caracteres(Insercion_Caracteres_Cirilicos, Lista_Sexe_Pac_rus, ["H", "M"])
    generar_numero_tse_rusa(Insercion_Caracteres_Cirilicos,Lista_TSE_rus)

#Medicos
    Lista_ID_Med = []
    Lista_Nombre_Med = []
    Lista_Cognom_Med = []
    Lista_Cognom2_Med = []
    Lista_DNI_Med = []
    Lista_Tlf_Med = []
    Lista_Fecha_Med = []
    Lista_Email_Med = []
    Generar_Numeros(Inserciones_Medicos, Lista_ID_Med, inicio=1)
    Generar_Nombre(Inserciones_Medicos, Lista_Nombre_Med)
    Generar_Cognom(Inserciones_Medicos, Lista_Cognom_Med)
    Generar_Cognom(Inserciones_Medicos, Lista_Cognom2_Med)
    generar_dni(Inserciones_Medicos, Lista_DNI_Med)
    Generar_Tlf(Inserciones_Medicos, Lista_Tlf_Med)
    Generar_Fecha(Inserciones_Medicos, Lista_Fecha_Med)
    Generar_correo_electronico(Inserciones_Medicos,Lista_Email_Med)

#Personal Infermeria
    Lista_ID_Personal_Inf = []
    Lista_Nombre_Personal_Inf = []
    Lista_Cognom_Personal_Inf = []
    Lista_Cognom2_Personal_Inf = []
    Lista_DNI_Personal_Inf = []
    Lista_Tlf_Personal_Inf = []
    Lista_Fecha_Personal_Inf = []
    Lista_Email_Personal_Inf = []
    Generar_Numeros(Inserciones_enfermeros, Lista_ID_Personal_Inf, inicio=101)
    Generar_Nombre(Inserciones_enfermeros, Lista_Nombre_Personal_Inf)
    Generar_Cognom(Inserciones_enfermeros, Lista_Cognom_Personal_Inf)
    Generar_Cognom(Inserciones_enfermeros, Lista_Cognom2_Personal_Inf)
    generar_dni(Inserciones_enfermeros, Lista_DNI_Personal_Inf)
    Generar_Tlf(Inserciones_enfermeros, Lista_Tlf_Personal_Inf)
    Generar_Fecha(Inserciones_enfermeros, Lista_Fecha_Personal_Inf)
    Generar_correo_electronico(Inserciones_enfermeros,Lista_Email_Personal_Inf)

#Personal Infermeria de planta
    Lista_ID_Personal_Inf_planta = []
    Lista_Nombre_Personal_Inf_planta = []
    Lista_Cognom_Personal_Inf_planta = []
    Lista_Cognom2_Personal_Inf_planta = []
    Lista_DNI_Personal_Inf_planta = []
    Lista_Tlf_Personal_Inf_planta = []
    Lista_Fecha_Personal_Inf_planta = []
    Lista_Email_Personal_Inf_planta = []
    Generar_Numeros(Inserciones_enfermeros_planta, Lista_ID_Personal_Inf_planta, inicio=202)
    Generar_Nombre(Inserciones_enfermeros_planta, Lista_Nombre_Personal_Inf_planta)
    Generar_Cognom(Inserciones_enfermeros_planta, Lista_Cognom_Personal_Inf_planta)
    Generar_Cognom(Inserciones_enfermeros_planta, Lista_Cognom2_Personal_Inf_planta)
    generar_dni(Inserciones_enfermeros_planta, Lista_DNI_Personal_Inf_planta)
    Generar_Tlf(Inserciones_enfermeros_planta, Lista_Tlf_Personal_Inf_planta)
    Generar_Fecha(Inserciones_enfermeros_planta, Lista_Fecha_Personal_Inf_planta)
    Generar_correo_electronico(Inserciones_enfermeros_planta,Lista_Email_Personal_Inf_planta)

#Personal de neteja
    Lista_ID_Personal_Net = []
    Lista_Nombre_Personal_Net = []
    Lista_Cognom_Personal_Net = []
    Lista_Cognom2_Personal_Net = []
    Lista_DNI_Personal_Net = []
    Lista_Tlf_Personal_Net = []
    Lista_Fecha_Personal_Net = []
    Lista_Email_Personal_Net = []
    Generar_Numeros(Inserciones_personal_nateja, Lista_ID_Personal_Net, inicio=303)
    Generar_Nombre(Inserciones_personal_nateja, Lista_Nombre_Personal_Net)
    Generar_Cognom(Inserciones_personal_nateja, Lista_Cognom_Personal_Net)
    Generar_Cognom(Inserciones_personal_nateja, Lista_Cognom2_Personal_Net)
    generar_dni(Inserciones_personal_nateja, Lista_DNI_Personal_Net)
    Generar_Tlf(Inserciones_personal_nateja, Lista_Tlf_Personal_Net)
    Generar_Fecha(Inserciones_personal_nateja, Lista_Fecha_Personal_Net)
    Generar_correo_electronico(Inserciones_personal_nateja,Lista_Email_Personal_Net)

#Persones d'amnistració
    Lista_ID_Personal_Adm = []
    Lista_Nombre_Personal_Adm = []
    Lista_Cognom_Personal_Adm = []
    Lista_Cognom2_Personal_Adm = []
    Lista_DNI_Personal_Adm = []
    Lista_Tlf_Personal_Adm = []
    Lista_Fecha_Personal_Adm = []
    Lista_Email_Personal_Adm = []
    Generar_Numeros(Inserciones_Administradores, Lista_ID_Personal_Adm, inicio=403)
    Generar_Nombre(Inserciones_Administradores, Lista_Nombre_Personal_Adm)
    Generar_Cognom(Inserciones_Administradores, Lista_Cognom_Personal_Adm)
    Generar_Cognom(Inserciones_Administradores, Lista_Cognom2_Personal_Adm)
    generar_dni(Inserciones_Administradores, Lista_DNI_Personal_Adm)
    Generar_Tlf(Inserciones_Administradores, Lista_Tlf_Personal_Adm)
    Generar_Fecha(Inserciones_Administradores, Lista_Fecha_Personal_Adm)
    Generar_correo_electronico(Inserciones_Administradores,Lista_Email_Personal_Adm)

#Tabla visitas_programadas
    Lista_ID_visitas_prog=[]
    Lista_Diagnosticos=[]
    Lista_Medicaments=[]
    Lista_Fecha_Visitas_Prog=[]
    Lista_Hora_Visitas_Prog=[]
    Lista_Ya_Visitat=[]
    Generar_Numeros(Insercion_Visitas, Lista_ID_visitas_prog, inicio=1)
    Generar_Diagnosticos(Insercion_Visitas,Lista_Diagnosticos)
    Generar_Medicamientos(Insercion_Visitas,Lista_Medicaments)
    Generar_Fecha(Insercion_Visitas, Lista_Fecha_Visitas_Prog)
    Generar_Hora(Insercion_Visitas, Lista_Hora_Visitas_Prog)
    Generar_Caracteres(Insercion_Visitas, Lista_Ya_Visitat, ["S", "N"])

#Tabla Especilidad
    Lista_ID_Espc=[]
    Lista_Nom_Especilidad=[]
    Generar_Numeros(Insercion_Especilidad,Lista_ID_Espc,inicio=1)
    Generar_Especialidad(Insercion_Especilidad,Lista_Nom_Especilidad)

#Tabla Planta
    Lista_Planta_ = []
    Generar_Numeros(Insercion_Planta, Lista_Planta_, inicio=1)

#Tabla Cita Medica
    Lista_Numero_Visita = []
    Lista_Hora_Cita_Medica = []
    Lista_Fecha_Cita_Medica = []
    Generar_Numeros(Insercion_Cita_Medica, Lista_Numero_Visita, inicio=1)
    Generar_Hora(Insercion_Cita_Medica,Lista_Hora_Cita_Medica)
    Generar_Fecha(Insercion_Cita_Medica,Lista_Fecha_Cita_Medica)

#Tabla Quirofano
    Lista_Numero_Quirofano=[]
    Generar_Numeros(Insercion_Quirofano,Lista_Numero_Quirofano, inicio=1)

#Tabla Operaciones
    Lista_ID_Operacion=[]
    Lista_Fecha_Operacion=[]
    Lista_Hora_Operacion=[]
    Lista_Nombre_Operacion=[]
    Generar_Numeros(Insercion_Operacion,Lista_ID_Operacion,inicio=1)
    Generar_Fecha(Insercion_Operacion,Lista_Fecha_Operacion)
    Generar_Hora(Insercion_Operacion,Lista_Hora_Operacion)
    Generar_Tipo_Operacion(Insercion_Operacion,Lista_Nombre_Operacion)

#Tabla Personal Vari (Zelador)
    Lista_DNI_Zelador=[]
    generar_dni(Insercion_Personal_Vari,Lista_DNI_Zelador)

#Tabla Reserva Quirofan
    Lista_Numero_Reserva_Quirofano=[]
    Generar_Numeros(Insercion_Reserva_Quirofano,Lista_Numero_Reserva_Quirofano,inicio=1)

#Tabla Habitacion
    Lista_Numero_Habitacion=[]
    Generar_Numeros(Insercion_Habitacion,Lista_Numero_Habitacion,inicio=1)

#Tabla reserva_habitacion
    Lista_ID_Res_Habitcion=[]
    Lista_Fecha_Entrada_Res_Habitcion=[]
    Lista_Fecha_Salida_Res_Habitcion=[]
    Generar_Numeros(Insercion_Reserva_Habitacion,Lista_ID_Res_Habitcion,inicio=1)
    generar_dos_fechas_en_rango(Insercion_Reserva_Habitacion, Lista_Fecha_Salida_Res_Habitcion,Lista_Fecha_Entrada_Res_Habitcion)
    Generar_Fecha(Insercion_Reserva_Habitacion,Lista_Fecha_Entrada_Res_Habitcion)

#Tabla hospital.aparells_medics
    Lista_ID_aparells_medics=[]
    Lista_Nom_Aparell_medics=[]
    Generar_Numeros(Insercion_Aparell_Medic,Lista_ID_aparells_medics,inicio=1)
    Generar_Aparell_Medico(Insercion_Aparell_Medic,Lista_Nom_Aparell_medics)

#Tabla Agenda_Medico
    Lista_ID_Agenda_Medico=[]
    Lista_Fecha_Agenda_Medico=[]
    Lisa_Hora_Agenda_Medico=[]
    Generar_Numeros(Insercion_Agenda_Medico,Lista_ID_Agenda_Medico)
    Generar_Fecha_Mismo_Mes(Insercion_Agenda_Medico,Lista_Fecha_Agenda_Medico)
    Generar_Hora(Insercion_Agenda_Medico,Lisa_Hora_Agenda_Medico)
#Curriculum
    print("Incio Generar Curriculum")
    Cantidad_Curriculum=100
    Lista_FechaIncio_Emp=[]
    Lista_Fecha2Fin_Emp=[]
    Lista_Fecha_Incio_Est=[]
    Lista_Fecha_Fin_Est=[]
    Lista_Direccion=[]
    Lista_Empresa=[]
    Lista_Empleo=[]
    Lista_Centro_Educativo=[]
    Lista_habilidad1=[]
    Lista_habilidad2=[]
    Lista_Tlf_Personal=[]
    generar_dos_fechas_en_rango(Cantidad_Curriculum,Lista_FechaIncio_Emp,Lista_Fecha2Fin_Emp)
    generar_dos_fechas_en_rango(Cantidad_Curriculum,Lista_Fecha_Incio_Est,Lista_Fecha_Fin_Est)
    generar_dirreccion(Cantidad_Curriculum,Lista_Direccion)
    Generar_Tlf(Cantidad_Curriculum,Lista_Tlf_Personal)
    generar_empleo(Cantidad_Curriculum,Lista_Empleo)
    generar_centro_educativo(Cantidad_Curriculum,Lista_Centro_Educativo)
    habilidad(Cantidad_Curriculum,Lista_habilidad1,Lista_habilidad2)
    Generar_empresa(Cantidad_Curriculum,Lista_Empresa)
    print("Fin Generar Curriculum")
    #Esto de aqui es la insercion de datos del curriculum

    '''Curriculum'''

    def llenar_datos_en_html(html_str, nombre, direccion, telefono, correo_electronico, nombre_empresa, fechas_Empleo, Empleo, Estudios, Fecha_Inicio_Fecha_Estudios, Centro_Educativo,Habilidad_1,Habilidad_2):
        soup = BeautifulSoup(html_str, 'html.parser')

        for tag in soup.find_all():
            if tag.string and "{" in tag.string and "}" in tag.string:
                contenido = tag.string.strip('{}')
                if contenido == "Nombre":
                    tag.string.replace_with(nombre)
                elif contenido == "Dirrecion":
                    tag.string.replace_with(direccion)
                elif contenido == "Telefono":
                    tag.string.replace_with(telefono)
                elif contenido == "Correo_Electronico":
                    tag.string.replace_with(correo_electronico)
                elif contenido == "Nombre_Empresa":
                    tag.string.replace_with(nombre_empresa)
                elif contenido == "Fecha_Inicio_Fecha":
                    tag.string.replace_with(fechas_Empleo)
                elif contenido == "Empleo":
                    tag.string.replace_with(Empleo)
                elif contenido == "Titulo":
                    tag.string.replace_with(Estudios)
                elif contenido == "Fecha_Inicio_Fecha_Estudios":
                    tag.string.replace_with(Fecha_Inicio_Fecha_Estudios)
                elif contenido == "Centro_Educativo":
                    if Centro_Educativo:
                        tag.string.replace_with(Centro_Educativo.pop(0))
                    else:
                        tag.string.replace_with("IES SAPAlOMERA")  
                elif contenido == "Habilidad_1":
                    tag.string.replace_with(Habilidad_1)
                elif contenido == "Habilidad_2":
                    tag.string.replace_with(Habilidad_2)
        return str(soup)


    def generar_pdf_con_datos(template_file, nombre, direccion, telefono, correo_electronico, nombre_empresa, fechas_Empleo,empleo,Estudios,Fecha_Inicio_Fecha_Estudios,Centro_Educativo,Habilidad1,Habilidad2,output_pdf):    # Leer el contenido del archivo de plantilla HTML
        with open(template_file, "r") as file:
            html_original = file.read()

        # Llenar los datos en el HTML
        html_con_datos = llenar_datos_en_html(html_original, nombre, direccion, telefono, correo_electronico, nombre_empresa,empleo,fechas_Empleo,Estudios,Fecha_Inicio_Fecha_Estudios,Centro_Educativo,Habilidad1,Habilidad2)

        # Guardar el HTML con los datos en un archivo temporal
        with open("temp.html", "w") as f:
            f.write(html_con_datos)

        # Convertir el HTML a PDF
        pdfkit.from_file("temp.html", output_pdf)

        print(f"PDF '{output_pdf}' generado exitosamente.")


    
    # Nombre del archivo de plantilla HTML
    template_file = "/mnt/DATOS/ASIX/M02/PROYECTO/Fake_Data/Curriculum/template.html"

# Comienza la insercion de datos;

    '''Tabla Pacientes'''
    for i in range(Inserciones_Paciente):
        cur.execute("INSERT INTO hospital.paciente(id_paciente, dni, nom, primer_cognom, segon_cognom, telefon, data_naixement, sexe, num_seguretat_social) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (Lista_ID_Pac[i], Lista_DNI_Pac[i], Lista_Nombre_Pac[i], Lista_Cognom_Pac[i], Lista_Cognom2_Pac[i], Lista_Tlf_Pac[i], Lista_Fecha_Pac[i], Lista_Sexe_Pac[i], Lista_num_seg_soc[i]))
        conn.commit()
    '''Fin Tabla Pacientes'''

    '''Paciente rusos'''
    print("Tablas Rusos")
    for i in range(Insercion_Caracteres_Cirilicos):
        cur.execute("INSERT INTO hospital.paciente(id_paciente, dni, nom, primer_cognom, segon_cognom, telefon, data_naixement, sexe) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (Lista_ID_Pac_Rus[i], Lista_DNI_Pac_rus[i], Lista_Nombre_Pac_rus[i], Lista_Cognom_Pac_rus[i], Lista_Cognom2_Pac_rus[i], Lista_Tlf_Pac_rus[i], Lista_Fecha_Pac_rus[i], Lista_Sexe_Pac_rus[i]))
        conn.commit()

    print("Fin Tablas Rusos")

    '''Tabla Personal'''
    
#Insercion de datos medicos
    print("Medicos")
    for i in range(Inserciones_Medicos):
        Empleo=random.choice(Lista_Empleo)
        Tlf_Personal=random.choice(Lista_Tlf_Personal)
        Empleo=random.choice(Lista_Empleo)
        habilidad1=random.choice(Lista_habilidad1)
        habilidad2=random.choice(Lista_habilidad1)
        Dirrecion=random.choice(Lista_Direccion)
        Empresa=random.choice(Lista_Empresa)
        output_pdf = f"cv_{i+1}.pdf"
        fecha_inicio_empleo = Lista_FechaIncio_Emp[i]
        fecha_fin_empleo = Lista_Fecha2Fin_Emp[i]      
        fechas_str_empleo = f"{fecha_inicio_empleo} - {fecha_fin_empleo}"
        fecha_inicio_estudios = Lista_Fecha_Incio_Est[i]
        fecha_fin_estudios = Lista_Fecha_Fin_Est[i]
        fechas_str_estudios = f"{fecha_fin_estudios} - {fecha_inicio_estudios}"
        generar_pdf_con_datos(template_file, Lista_Nombre_Med[i], Dirrecion, Tlf_Personal, Lista_Email_Med[i], 
                               Empresa, fechas_str_empleo, Empleo,"Medicina",fechas_str_estudios,
                                Lista_Centro_Educativo,habilidad1,habilidad2,output_pdf)
    
        with open(output_pdf, "rb") as f:
           pdf_data = f.read()

          # Insertar el archivo PDF en la base de datos
        cur.execute("INSERT INTO hospital.personal(id_personal, curriculum, estudis, dni, nom, primer_cognom, segon_cognom, telefon, fecha, email, tipus_personal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
               (Lista_ID_Med[i], psycopg2.Binary(pdf_data), "Medicina", Lista_DNI_Med[i], Lista_Nombre_Med[i], Lista_Cognom_Med[i], Lista_Cognom2_Med[i], Lista_Tlf_Med[i], Lista_Fecha_Med[i], Lista_Email_Med[i], "Medico"))
 
     
        conn.commit()
    print("Fin Medicos")
#Insercion de datos enfermeros
    print("Enfermeros")
    for i in range(100):
        Empleo=random.choice(Lista_Empleo)
        Tlf_Personal=random.choice(Lista_Tlf_Personal)
        Empleo=random.choice(Lista_Empleo)
        habilidad1=random.choice(Lista_habilidad1)
        habilidad2=random.choice(Lista_habilidad1)
        Dirrecion=random.choice(Lista_Direccion)
        Empresa=random.choice(Lista_Empresa)
        output_pdf = f"cv_{i+1}.pdf"
        fecha_inicio_empleo = Lista_FechaIncio_Emp[i]
        fecha_fin_empleo = Lista_Fecha2Fin_Emp[i]      
        fechas_str_empleo = f"{fecha_inicio_empleo} - {fecha_fin_empleo}"
        fecha_inicio_estudios = Lista_Fecha_Incio_Est[i]
        fecha_fin_estudios = Lista_Fecha_Fin_Est[i]
        fechas_str_estudios = f"{fecha_fin_estudios} - {fecha_inicio_estudios}"
        generar_pdf_con_datos(template_file, Lista_Nombre_Med[i], Dirrecion, Tlf_Personal, Lista_Email_Personal_Inf[i], 
                              Empresa, fechas_str_empleo, Empleo,"Enfermería",fechas_str_estudios,
                                Lista_Centro_Educativo,habilidad1,habilidad2
        ,output_pdf)
        with open(output_pdf, "rb") as f:
            pdf_data = f.read()
        cur.execute("INSERT INTO hospital.personal(id_personal, curriculum, estudis, dni, nom, primer_cognom, segon_cognom, telefon, fecha, email, tipus_personal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                (Lista_ID_Personal_Inf[i], psycopg2.Binary(pdf_data), "Enfermeria", Lista_DNI_Personal_Inf[i], Lista_Nombre_Personal_Inf[i], Lista_Cognom_Personal_Inf[i], Lista_Cognom2_Personal_Inf[i], Tlf_Personal, Lista_Fecha_Personal_Inf[i], Lista_Email_Personal_Inf[i], "Enfermero"))
        conn.commit()
    conn.commit()
    print("Fin enfermeros")
#Insercion de datos enfermeros planta
    print("enfermeros Planta")
    for i in range(100):
        Empleo=random.choice(Lista_Empleo)
        Tlf_Personal=random.choice(Lista_Tlf_Personal)
        Empleo=random.choice(Lista_Empleo)
        habilidad1=random.choice(Lista_habilidad1)
        habilidad2=random.choice(Lista_habilidad1)
        Dirrecion=random.choice(Lista_Direccion)
        Empresa=random.choice(Lista_Empresa)
        output_pdf = f"cv_{i+1}.pdf"
        fecha_inicio_empleo = Lista_FechaIncio_Emp[i]
        fecha_fin_empleo = Lista_Fecha2Fin_Emp[i]      
        fechas_str_empleo = f"{fecha_inicio_empleo} - {fecha_fin_empleo}"
        fecha_inicio_estudios = Lista_Fecha_Incio_Est[i]
        fecha_fin_estudios = Lista_Fecha_Fin_Est[i]
        fechas_str_estudios = f"{fecha_fin_estudios} - {fecha_inicio_estudios}"
        generar_pdf_con_datos(template_file, Lista_Nombre_Med[i], Dirrecion, Tlf_Personal, Lista_Email_Personal_Inf[i], 
                               Empresa, fechas_str_empleo, Empleo,"Enfermería",fechas_str_estudios,
                                Lista_Centro_Educativo,habilidad1,habilidad2
        ,output_pdf)
        with open(output_pdf, "rb") as f:
            pdf_data = f.read()
        cur.execute("INSERT INTO hospital.personal(id_personal, curriculum, estudis, dni, nom, primer_cognom, segon_cognom, telefon, fecha, email, tipus_personal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                (Lista_ID_Personal_Inf_planta[i], psycopg2.Binary(pdf_data), "Enfermeria", Lista_DNI_Personal_Inf_planta[i], Lista_Nombre_Personal_Inf_planta[i], Lista_Cognom_Personal_Inf_planta[i], Lista_Cognom2_Personal_Inf_planta[i], Tlf_Personal, Lista_Fecha_Personal_Inf_planta[i], Lista_Email_Personal_Inf_planta[i], "Enfermero"))
        conn.commit()
    conn.commit()
    print("Fin enfermeros Planta")
#Insercion de datos personal nateja
    print("Limpieza")
    for i in range(Inserciones_personal_nateja):
        Empleo=random.choice(Lista_Empleo)
        Tlf_Personal=random.choice(Lista_Tlf_Personal)
        Empleo=random.choice(Lista_Empleo)
        habilidad1=random.choice(Lista_habilidad1)
        habilidad2=random.choice(Lista_habilidad1)
        Dirrecion=random.choice(Lista_Direccion)
        Empresa=random.choice(Lista_Empresa)
        email=random.choice(Lista_Email_Personal_Net)
        output_pdf = f"cv_{i+1}.pdf"
        fecha_inicio_empleo = Lista_FechaIncio_Emp[i]
        fecha_fin_empleo = Lista_Fecha2Fin_Emp[i]      
        fechas_str_empleo = f"{fecha_inicio_empleo} - {fecha_fin_empleo}"
        fecha_inicio_estudios = Lista_Fecha_Incio_Est[i]
        fecha_fin_estudios = Lista_Fecha_Fin_Est[i]
        fechas_str_estudios = f"{fecha_fin_estudios} - {fecha_inicio_estudios}"
        generar_pdf_con_datos(template_file, Lista_Nombre_Med[i], Dirrecion, Tlf_Personal, Lista_Email_Personal_Inf[i], 
                               Empresa, fechas_str_empleo, Empleo,"Enfermería",fechas_str_estudios,
                                Lista_Centro_Educativo,habilidad1,habilidad2
        ,output_pdf)
        with open(output_pdf, "rb") as f:
            pdf_data = f.read()
        cur.execute("INSERT INTO hospital.personal(id_personal, curriculum, estudis, dni, nom, primer_cognom, segon_cognom, telefon, fecha, email, tipus_personal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                (Lista_ID_Personal_Net[i], psycopg2.Binary(pdf_data), "ESO", Lista_DNI_Personal_Net[i], Lista_Nombre_Personal_Inf_planta[i], Lista_Cognom_Personal_Net[i], Lista_Cognom2_Personal_Net[i], Tlf_Personal, Lista_Fecha_Personal_Net[i], email, "Personal de neteja"))
        conn.commit()
    print("Fin Limpieza")
#Insercion de datos Administradores
    print("Administradores")
    for i in range(Inserciones_Administradores):
        Empleo=random.choice(Lista_Empleo)
        Tlf_Personal=random.choice(Lista_Tlf_Personal)
        habilidad1=random.choice(Lista_habilidad1)
        habilidad2=random.choice(Lista_habilidad1)
        Dirrecion=random.choice(Lista_Direccion)
        output_pdf = f"cv_{i+1}.pdf"
        fecha_inicio_empleo = Lista_FechaIncio_Emp[i]
        fecha_fin_empleo = Lista_Fecha2Fin_Emp[i]      
        fechas_str_empleo = f"{fecha_inicio_empleo} - {fecha_fin_empleo}"
        fecha_inicio_estudios = Lista_Fecha_Incio_Est[i]
        fecha_fin_estudios = Lista_Fecha_Fin_Est[i]
        fechas_str_estudios = f"{fecha_fin_estudios} - {fecha_inicio_estudios}"
        generar_pdf_con_datos(template_file, Lista_Nombre_Personal_Adm[i], Lista_Direccion[i], Tlf_Personal, Lista_Email_Personal_Adm[i], 
                               Empresa, fechas_str_empleo, Empleo,"ASIR",fechas_str_estudios,
                                Lista_Centro_Educativo,habilidad1,habilidad2
        ,output_pdf)
        # Leer el contenido del archivo PDF en modo binario
        with open(output_pdf, "rb") as f:
            pdf_data = f.read()
        cur.execute("INSERT INTO hospital.personal(id_personal, curriculum, estudis, dni, nom, primer_cognom, segon_cognom, telefon, fecha, email, tipus_personal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                (Lista_ID_Personal_Adm[i], psycopg2.Binary(pdf_data), "ASIR", Lista_DNI_Personal_Adm[i], Lista_Nombre_Personal_Adm[i], Lista_Cognom_Personal_Adm[i], Lista_Cognom2_Personal_Adm[i], Lista_Tlf_Personal_Adm[i], Lista_Fecha_Personal_Adm[i], Lista_Email_Personal_Adm[i], "Personal de administració"))
        conn.commit()
    print("Fin Administradores")
    ''' Fin Tabla Personal'''

    '''Tabla Personal Metge'''
    for i in range(Inserciones_Medicos):
            cur.execute("INSERT INTO hospital.metge_metgessa(dni,id_paciente) VALUES (%s, %s)",
                (Lista_DNI_Med[i],Lista_ID_Pac[i]))
    '''Fin Tabla Personal Metge'''

    '''Tabla Visitas Programadas'''
    for i in range(Insercion_Visitas):
        dni_medico=random.choice(Lista_DNI_Med)
        cur.execute("INSERT INTO hospital.visitas_programadas(id_visita, diagnostic, medicaments, fecha, hora, ya_visitat, id_paciente, dni) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (Lista_ID_visitas_prog[i], Lista_Diagnosticos[i], Lista_Medicaments[i], Lista_Fecha_Visitas_Prog[i], Lista_Hora_Visitas_Prog[i], Lista_Ya_Visitat[i], Lista_ID_Pac[i], dni_medico))
        conn.commit()
    '''Fin Visitas Programadas'''

    '''Tabla Especilidad'''
    for i in range(Inserciones_Medicos):
        cur.execute("INSERT INTO hospital.especialidad(id_especialidad, nom_especialitat, dni_metge) VALUES (%s, %s, %s)",
        (Lista_ID_Espc[i], Lista_Nom_Especilidad[i],Lista_DNI_Med[i]))
        conn.commit()
    '''Fin Tabla Especilidad'''

    '''Tabla Planta'''
    for item in Lista_Planta_:
        cur.execute("INSERT INTO hospital.planta VALUES (%s)", (item, ))
        conn.commit()
    '''Fin Tabla Planta'''

    '''Tabla cita_medica'''
    for i in range(Insercion_Cita_Medica):
        num_planta = random.randint(1, 5)
        dni_medico = random.choice(Lista_DNI_Med)
        if i < len(Lista_Numero_Visita):
            cur.execute("INSERT INTO hospital.cita_medica(nº_visita,dia,hora,id_paciente,dni,nº_planta) VALUES (%s, %s, %s, %s, %s, %s)", 
                (Lista_Numero_Visita[i],Lista_Fecha_Cita_Medica[i],Lista_Hora_Cita_Medica[i],Lista_ID_Pac[i],dni_medico, num_planta))
        conn.commit()
    '''Fin Tabla cita_medica'''

    '''Tabla Quirofano'''
    for i in range(Insercion_Quirofano):
        num_planta = random.randint(1, Insercion_Planta)
        num_quirofano = Lista_Numero_Quirofano[i]
        cur.execute("INSERT INTO hospital.quirofano(num_quirofano, num_planta) VALUES (%s, %s)", 
        (num_quirofano, num_planta))
        conn.commit()
    '''Fin Tabla Quirofano'''

    '''Tabla Operacion'''
    for i in range(Insercion_Operacion):
        num_quirofano=random.choice(Lista_Numero_Quirofano)
        dni_medico=random.choice(Lista_DNI_Med)
        cur.execute("INSERT INTO hospital.operaciones(id_operaciones, data,hora,tipus_operacio,id_paciente,num_quirofano,dni_metge) VALUES (%s, %s, %s,%s, %s, %s,%s)",
            (Lista_ID_Operacion[i],Lista_Fecha_Operacion[i],Lista_Hora_Operacion[i],Lista_Nombre_Operacion[i],Lista_ID_Pac[i],num_quirofano,dni_medico))
        conn.commit()
    '''Fin Tabla Operacion'''

    '''Tabla Personal Infermeria'''
    for i in range(Inserciones_enfermeros):
        num_planta = random.randint(1, 5)
        id_operaciones = random.choice(Lista_ID_Operacion)
        dni_medico = random.choice(Lista_DNI_Med)
        cur.execute("INSERT INTO hospital.personal_infermeria(dni, dni_medic, num_planta, id_operaciones) VALUES (%s, %s, %s, %s)",
                    (Lista_DNI_Personal_Inf[i], dni_medico, num_planta, id_operaciones))
        conn.commit()
    '''Fin tabla Personal Infermeria'''

    '''Tabla Personal Infermeria de planta'''
    for i in range(Inserciones_enfermeros_planta):
        num_planta = random.randint(1, 5)
        id_operaciones = random.choice(Lista_ID_Operacion)
        cur.execute("INSERT INTO hospital.personal_infermeria(dni, num_planta, id_operaciones) VALUES (%s, %s, %s)",
                    (Lista_DNI_Personal_Inf_planta[i], num_planta, id_operaciones))
        conn.commit()
    '''Fin tabla Personal Infermeria de planta'''

    '''Tabla Personal_Vari'''
#personal de neteja

    for i in range(Inserciones_personal_nateja):
        cur.execute("INSERT INTO hospital.personal_vari(tipus_personal,dni) VALUES (%s, %s)",
        ("Personal de nateja)",Lista_DNI_Personal_Net[i]))
        conn.commit()
        
#personal d'administració

    for i in range(Inserciones_Administradores):
        cur.execute("INSERT INTO hospital.personal_vari(tipus_personal,dni) VALUES (%s, %s)",
        ("Personal D'administració",Lista_DNI_Personal_Adm[i]))
        conn.commit()
    '''Fin Tabla Personal_Vari'''

    '''Tabla Reserva Quirofano'''
    for i in range(Insercion_Quirofano):
        cur.execute("INSERT INTO hospital.reserva_quirofano(num_reserva_quirofano,num_quirofano) VALUES (%s, %s)",
        (Lista_Numero_Reserva_Quirofano[i],Lista_Numero_Quirofano[i]))
        conn.commit()
    '''Fin Tabla Reserva Quirofano'''

    '''Tabla Habitacion'''
    for i in  range(len(Lista_Numero_Habitacion)):
            Planta = random.choice(Lista_Planta_)
            cur.execute("INSERT INTO hospital.habitacion(num_habitacion, num_planta) VALUES (%s, %s)",
                        (Lista_Numero_Habitacion[i], Planta))
            conn.commit()
    '''Fin Tabla Habitacion'''

    '''Tabla Reserva Habitacion'''
    for i in range(Insercion_Reserva_Habitacion):
        num_habitacion=random.choice(Lista_Numero_Habitacion)
        id_paciente=random.choice(Lista_ID_Pac)
        cur.execute("INSERT INTO hospital.reserva_habitacion(id_reserva,dia_sortida,dia_ingresa,num_habitacion,id_paciente) VALUES (%s, %s,%s, %s, %s)",
        (Lista_ID_Res_Habitcion[i],Lista_Fecha_Entrada_Res_Habitcion[i],Lista_Fecha_Salida_Res_Habitcion[i],num_habitacion,id_paciente))
        conn.commit()
    '''Fin Tabla Reserva Habitacion'''

    '''Tabla Aparells Medics'''
    for i in range(Insercion_Aparell_Medic):
        num_quirofano=random.choice(Lista_Numero_Quirofano)
        print(Lista_Nom_Aparell_medics)
        cur.execute("INSERT INTO hospital.aparells_medics(id_aparells_medics,nom,num_quirofano) VALUES (%s, %s,%s)",
        (Lista_ID_aparells_medics[i],Lista_Nom_Aparell_medics[i],num_quirofano))
        conn.commit()
    '''Fin Tabla Aparells Medics'''

    '''Tabla Agenda Medico'''
    for i in range(Insercion_Agenda_Medico):
        dni_metge = random.choice(Lista_DNI_Med)
        cur.execute("INSERT INTO hospital.agenda_metge(id_agenda_metge, fecha, hora, dni_metge) VALUES (%s, %s, %s, %s)",
                    (Lista_ID_Agenda_Medico[i], Lista_Fecha_Agenda_Medico[i], Lisa_Hora_Agenda_Medico[i], dni_metge))
        conn.commit()

    '''Fin Tabla Agenda Medico'''
    # Cierra la conexión
    cur.close()
    conn.close()