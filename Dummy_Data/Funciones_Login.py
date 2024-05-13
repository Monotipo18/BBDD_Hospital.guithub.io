import csv
import psycopg2
from psycopg2 import sql
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv
import pwinput
load_dotenv()

usuario_BBDD = os.getenv("usuario_BBDD")
contraseña_BBDD = os.getenv("contraseña_BBDD")
hostname_BBDD = os.getenv("hostname_BBDD")
archivo_csv = 'Datos.csv'

def conectar_bd(dbname, usuario, contraseña, host="snakeeater.equemmfoundation.top", port="5432"):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=usuario,
            password=contraseña,
            host=host,
            port=port
        )
        return conn
    except psycopg2.Error as e:
        print("Error de conexión:", e)
        return None

def cerrar_bd(conn, cur):
    if cur:
        cur.close()
    if conn:
        conn.close()


def crear_rol_usuario(cur, usuario, contraseña):
    '''crea un rol de usuario en la BDD'''
    cur.execute(sql.SQL("CREATE ROLE {} LOGIN PASSWORD %s").format(sql.Identifier(usuario)), (contraseña,))

def rol_administrativo(cur, usuario, contraseña):
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
        return conn, cur

def Registro(USUARIO, CONTRASEÑA,TIPO):
    '''Registra un usuario en la BDD con el rol que se le especifique'''
    conn, cur = rol_administrativo()

    if TIPO.upper() == "MEDICO":
        crear_rol_usuario(cur, USUARIO, CONTRASEÑA)
        role_name = sql.Identifier(USUARIO)
        sql_query = sql.SQL("GRANT medicos TO {};").format(role_name)
        cur.execute(sql_query)
        print (f"Se ha dado de alta correctamente al usuario {USUARIO} en el rol {TIPO} ")
    elif TIPO.upper() == "INFERMER/A":
        crear_rol_usuario(cur, USUARIO, CONTRASEÑA)
        role_name = sql.Identifier(USUARIO)
        sql_query = sql.SQL("GRANT enfermeros TO {};").format(role_name)
        cur.execute(sql_query)
    elif TIPO.upper() == "PACIENT":
        crear_rol_usuario(cur, USUARIO, CONTRASEÑA)
        role_name = sql.Identifier(USUARIO)
        sql_query = sql.SQL("GRANT pacient TO {};").format(role_name)
        cur.execute(sql_query)
    elif TIPO.upper() == "ADMINISTRATIUS":
        crear_rol_usuario(cur, USUARIO, CONTRASEÑA)
        role_name = sql.Identifier(USUARIO)
        sql_query = sql.SQL("GRANT Administratius TO {};").format(role_name)
        cur.execute(sql_query)

    cerrar_bd(conn, cur)

def login(usuario, contraseña, host="snakeeater.equemmfoundation.top", port="5432"):
    try:
        conn = conectar_bd("asixhospitalbd", usuario, contraseña, host)
        if conn:
            cur = conn.cursor()
            return conn, cur
    except psycopg2.Error as e:
        print("Error de conexión:", e)
        return None, None

    try:
        conn = conectar_bd("asixhospitalbd", usuario, contraseña, "revolverocelot.equemmfoundation.top", "5433")
        if conn:
            cur = conn.cursor()
            return conn, cur
    except psycopg2.Error as e:
        print("Error de conexión:", e)
        return None, None


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