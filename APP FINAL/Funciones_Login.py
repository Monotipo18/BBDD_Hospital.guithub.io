import csv
import psycopg2
from psycopg2 import sql
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv
import pwinput
import xml.etree.ElementTree as ET
import xml.dom.minidom
from random import sample
load_dotenv()

usuario_BBDD = os.getenv("usuario_BBDD")
contraseña_BBDD = os.getenv("contraseña_BBDD")
hostname_BBDD = os.getenv("hostname_BBDD")
archivo_csv = 'Datos.csv'


def conectar_bd(USUARIO,CONTRASEÑA):
    ''' Función para conectar a PostgreSQL'''
    try:
        conn = psycopg2.connect(
            dbname="asixhospitalbd",
            user=USUARIO,
            password=CONTRASEÑA,
            host="snakeeater.equemmfoundation.top",
        )
        cur = conn.cursor()
        return conn, cur
    except psycopg2.Error as e:
        try:
            conn = psycopg2.connect(
                dbname="asixhospitalbd",
                user=USUARIO,
                password=CONTRASEÑA,
                host="revolverocelot.equemmfoundation.top",
                port="5433"
            )
            cur = conn.cursor()
            return conn, cur
        except:
            print("Error en la conexión a la base de datos")
            return None, None


def cerrar_bd(conn, cur):
    if cur:
        cur.close()
    if conn:
        conn.close()


def crear_rol_usuario(cur, usuario, contraseña):
    '''crea un rol de usuario en la BDD'''
    cur.execute(sql.SQL("CREATE ROLE {} LOGIN PASSWORD %s").format(sql.Identifier(usuario)), (contraseña,))

'''def rol_administrativo(cur, usuario, contraseña):
    usuario = input("Introdueix el teu Usuari: ")
    contraseña = pwinput.pwinput("Introdueix la teva Contrasenya: ")
    try:
        conn = psycopg2.connect(
            dbname="asixhospitalbd",
            user = usuario,
            password = contraseña,
            host="snakeeater.equemmfoundation.top",
        )
        cur = conn.cursor()
        return conn, cur
    except psycopg2.Error as e:
        conn = psycopg2.connect(
            dbname="asixhospitalbd",
            user = usuario,
            password = contraseña,
            host="revolverocelot.equemmfoundation.top",
            port="5433"
        )
        cur = conn.cursor()
        return conn, cur'''

def Registro(USUARIO_Log, CONTRASEÑA_log,USUARIO,CONTRASEÑA, TIPO):
    #print(USUARIO)
    '''Registra un usuario en la BDD con el rol que se le especifique'''

    '''
    resultado_login = login(USUARIO, CONTRASEÑA)
    print(resultado_login)
    if resultado_login:
        print("Error en la conexión a la base de datos. No se puede registrar el usuario.")
        return
    '''
    
    #conn, cur = resultado_login

    conn, cur = login(USUARIO_Log, CONTRASEÑA_log)
    if TIPO.upper() == "MEDICO":
        crear_rol_usuario(cur, USUARIO, CONTRASEÑA)
        role_name = sql.Identifier(USUARIO)
        sql_query = sql.SQL("GRANT medicos TO {};").format(role_name)
        cur.execute(sql_query)
        conn.commit()
        print(f"Se ha dado de alta correctamente al usuario {USUARIO} en el rol {TIPO}")
    elif TIPO.upper() == "INFERMER/A":
        crear_rol_usuario(cur, USUARIO, CONTRASEÑA)
        role_name = sql.Identifier(USUARIO)
        sql_query = sql.SQL("GRANT enfermeros TO {};").format(role_name)
        cur.execute(sql_query)
        conn.commit()
        print(f"Se ha dado de alta correctamente al usuario {USUARIO} en el rol {TIPO}")
    elif TIPO.upper() == "PACIENT":
        crear_rol_usuario(cur, USUARIO, CONTRASEÑA)
        role_name = sql.Identifier(USUARIO)
        sql_query = sql.SQL("GRANT pacient TO {};").format(role_name)
        cur.execute(sql_query)
        conn.commit()
        print(f"Se ha dado de alta correctamente al usuario {USUARIO} en el rol {TIPO}")
    elif TIPO.upper() == "ADMINISTRATIUS":
        crear_rol_usuario(cur, USUARIO, CONTRASEÑA)
        role_name = sql.Identifier(USUARIO)
        sql_query = sql.SQL("GRANT Administratius TO {};").format(role_name)
        #sql_query_alt = sql.SQL("ALTER ROLE {} CREATEROLE;").format(role_name)
        #cur.execute(sql_query)
        #cur.execute(sql_query_alt)
        conn.commit()
        print(f"Se ha dado de alta correctamente al usuario {USUARIO} en el rol {TIPO}")
        #cur.execute(sql_query_alt)
    cerrar_bd(conn, cur)


'''
def login(usuario, contraseña):
    try:
        con,_ = conectar_bd(usuario, contraseña)
        if con != None:
            return True
        else:
            return False
    except psycopg2.Error as e:
        print("Error de conexión:", e)
'''
def login(usuario, contraseña):
    try:
        con, cur = conectar_bd(usuario, contraseña)
        if con is not None:
            return con, cur
        else:
            return False
    except psycopg2.Error as e:
        print("Error de conexión:", e)
        return False


def Crear_xml_exportacion(ruta_archivo):
    '''Función para crear automáticamente la exportación de datos en un XML'''
    try:
        # Verificar si el archivo ya existe en la ruta especificada
        if not os.path.exists(ruta_archivo):
            # Abrir el archivo para escritura
            with open(ruta_archivo, 'w', newline='', encoding="utf-8") as file:
                # Crear un objeto writer con delimitador ';'
                writer = csv.writer(file, delimiter=';')
                # Escribir la fila de cabecera en el archivo
                writer.writerow(["ID Visita", "Data", "Nom Metge", "Primer Cognom Metge", "Nom Pacient", "Primer Cognom Pacient"])
    except Exception as e:
        print("Error:", e)

def Cargar_exportacion_xml(resultados):
    '''Carga el select dentro del Csv '''
    with open(f"{nombre_archivo}.xml", 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        # Crear un elemento XML para todas las visitas
        root = ET.Element("visitas")
        # Iterar sobre cada fila de resultados y escribir en el archivo CSV
        for resultado in resultados:
            writer.writerow(resultado)
            # Crear un elemento XML para cada fila y agregarlo al árbol XML
            visita = ET.SubElement(root, "visita")
            ET.SubElement(visita, "ID").text = str(resultado[0])
            ET.SubElement(visita, "Fecha").text = resultado[1].strftime("%Y-%m-%d")
            ET.SubElement(visita, "NomMetge").text = resultado[2]
            ET.SubElement(visita, "PrimerCognomMetge").text = resultado[3]
            ET.SubElement(visita, "NomPacient").text = resultado[4]
            ET.SubElement(visita, "PrimerCognomPacient").text = resultado[5]

    # Guardar el árbol XML en un archivo
    xml_tree = ET.ElementTree(root)
    xml_tree.write(f"{nombre_archivo}.xml", encoding="utf-8", xml_declaration=True)
    # Formatear el XML para que esté bien identado y tabulado
    dom = xml.dom.minidom.parse(f"{nombre_archivo}.xml")
    with open(f"{nombre_archivo}.xml", "w", encoding="utf-8") as file:
        file.write(dom.toprettyxml())

def Generar_Titulo(longitud):
  
    # Definimos los caracteres y simbolos
    abc_minusculas = "abcdefghijklmnopqrstuvwxyz"
    abc_mayusculas = abc_minusculas.upper() 
    numeros = "0123456789"
    # Definimos la secuencia
    secuencia = abc_minusculas + abc_mayusculas + numeros 
    # Llamamos la función sample() utilizando la secuencia, y la longitud
    titulo = sample(secuencia, longitud)
    # Con join insertamos los elementos de una lista en una cadena
    password_result = "".join(titulo)
    # Retornamos la variables "password_result"
    return password_result

nombre_archivo = Generar_Titulo(12)

'''def Registro(USUARIO, CONTRASEÑA):
    if usuario_existente(USUARIO):
        print("El usuario ya existe.")
        return
    USUARIO_ENC = generate_password_hash(USUARIO, method='pbkdf2:sha256')
    PASWORD_ENC = generate_password_hash(CONTRASEÑA, method='pbkdf2:sha256')
    Cargar_csv(USUARIO_ENC, PASWORD_ENC)
    conn = psycopg2.connect(
        dbname="Redis",
        user="postgres",
        password="P@ssw0rd",
        host="snakeeater.equemmfoundation.top",
    )
    cur = conn.cursor()
    cur.execute(sql.SQL("CREATE ROLE {} LOGIN PASSWORD %s").format(sql.Identifier(USUARIO)), (CONTRASEÑA,))
    conn.commit()
    conn.close()'''

'''
def Crear_csv():

    try:
        if not os.path.exists(archivo_csv):
            with open(archivo_csv, 'W', newline='', encoding= "utf-8") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(["Usuario", "Contraseña"])
    except Exception as e:
        print("Error:", e)
        '''

'''comprueba si existe el usuario en el ficher CSV'''
'''def usuario_existente(usuario):
    try:
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector_csv = csv.reader(csvfile, delimiter=';')
            next(lector_csv)  
            for fila in lector_csv:
                hash_usuario = fila[0]
                if check_password_hash(hash_usuario, usuario):
                    return True
    except Exception as e:
        print("Error:", e)
        return False'''

'''def Cargar_csv(dato1, dato2):
    with open(archivo_csv, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([dato1, dato2])'''

'''def conectar_bd():

    try:
        conn = psycopg2.connect(
            dbname="asixhospitalbd",
            user="grupomaviunal",
            password="uN@i3st4fu3rtE",
            host="snakeeater.equemmfoundation.top",
        )
        cur = conn.cursor()
        return conn, cur
    except psycopg2.Error as e:
        conn = psycopg2.connect(
            dbname="asixhospitalbd",
            user="grupomaviunal",
            password="uN@i3st4fu3rtE",
            host="revolverocelot.equemmfoundation.top",
            port="5433"
        )
        cur = conn.cursor()
        return conn, cur'''

