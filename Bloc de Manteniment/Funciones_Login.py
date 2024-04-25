import csv
import psycopg2
from psycopg2 import sql
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

usuario_BBDD = os.getenv("usuario_BBDD")
contraseña_BBDD = os.getenv("contraseña_BBDD")
hostname_BBDD = os.getenv("hostname_BBDD")
archivo_csv = 'Datos.csv'

def conectar_bd():
    ''' Funció per connectar a postgres'''
    conn = psycopg2.connect(
        dbname="asixhospitalbd",
        user="grupomaviunal",
        password="uN@i3st4fu3rtE",
        host="snakeeater.equemmfoundation.top",
    )
    cur = conn.cursor()
    return conn, cur




def cerrar_bd(conn, cur):
    '''funció per desconectar de la base de dades'''
    conn.commit()
    cur.close()
    conn.close()

def Crear_csv():
    '''Funcion para crear automaticamente un archivo csv'''
    try:
        if not os.path.exists(archivo_csv):
            with open(archivo_csv, 'w', newline='', encoding= "utf-8") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(["Usuario", "Contraseña"])
    except Exception as e:
        print("Error:", e)

def usuario_existente(usuario):
    '''comprueba si existe el usuario en el ficher CSV'''
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
        return False

def crear_rol_usuario(cur, usuario, contraseña):
    '''crea un rol de usuario en la BDD'''
    cur.execute(sql.SQL("CREATE ROLE {} LOGIN PASSWORD %s").format(sql.Identifier(usuario)), (contraseña,))
    
def Registro(USUARIO, CONTRASEÑA,TIPO):
    '''Registra un usuario en la BDD con el rol que se le especifique'''
    conn, cur = conectar_bd()
    if usuario_existente(USUARIO):
        print("El usuario ya existe.")
        cerrar_bd(conn, cur)
        return
    USUARIO_ENC = generate_password_hash(USUARIO, method='pbkdf2:sha256')
    PASWORD_ENC = generate_password_hash(CONTRASEÑA, method='pbkdf2:sha256')
    Cargar_csv(USUARIO_ENC, PASWORD_ENC)

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


def Cargar_csv(dato1, dato2):
    '''Carga los datos que se le especifiquen dentro del archivo CSV '''
    with open(archivo_csv, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([dato1, dato2])

def Login(USUARIO, CONTRASEÑA):
    '''Conecta a la BDD contrastando los datos con el CSV'''
    try:
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector_csv = csv.reader(csvfile, delimiter=';')
            next(lector_csv)
            for fila in lector_csv:
                hash_usuario = fila[0]
                hash_contraseña = fila[1]
                if check_password_hash(hash_usuario, USUARIO) and check_password_hash(hash_contraseña, CONTRASEÑA):
                    conn = psycopg2.connect(
                         dbname="asixhospitalbd",
                         user=USUARIO,
                         password=CONTRASEÑA,
                         host="snakeeater.equemmfoundation.top"
                    )
                    return True
                break   
        print("Credenciales no válidas")
        return False
    except FileNotFoundError:
        print("El archivo CSV no existe.")
        return False
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
