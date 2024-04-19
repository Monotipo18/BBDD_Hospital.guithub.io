import csv
from werkzeug.security import generate_password_hash, check_password_hash
import pwinput
import psycopg2
import os
from psycopg2 import sql
archivo_csv = 'A.csv'


#CREACIÓ DEL FITXER
def Crear_csv():
    with open(archivo_csv, 'a', newline='') as file:
        Titols=["Usuario","Contraseña"]
        writer = csv.writer(file, delimiter=';')
        writer.writerow(Titols)

def conecioo_BDD():
        conn = psycopg2.connect(
        dbname="hr",
        user="postgres",
        password="unai",
        host="192.168.56.108",
    )
        return conn
#Comprovació Usuario Existent
def usuario_existente(usuario):
    try:
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector_csv = csv.reader(csvfile, delimiter=';')
            next(lector_csv)  
            for fila in lector_csv:
                hash_usuario = fila[0]
                if check_password_hash(hash_usuario, usuario):
                    return True
    except Exception as e:
        print("Usuario Existente")
        return False
#Registre del usuari
def paciente(USUARIO, CONTRASEÑA):
    if usuario_existente(USUARIO):
        print("El usuario ya existe.")
        return
    USUARIO_ENC = generate_password_hash(USUARIO, method='pbkdf2:sha256')
    PASWORD_ENC = generate_password_hash(CONTRASEÑA, method='pbkdf2:sha256')
    Cargar_csv(USUARIO_ENC, PASWORD_ENC)
    conn = psycopg2.connect(
        dbname="hr",
        user="postgres",
        password="unai",
        host="192.168.56.108",
    )
    cur = conn.cursor()
    cur.execute(sql.SQL("CREATE ROLE {} LOGIN PASSWORD %s").format(sql.Identifier(USUARIO)), (CONTRASEÑA,))
    cur.execute(sql.SQL("GRANT CONNECT ON DATABASE hr TO {}").format(sql.Identifier(USUARIO)))
    cur.execute(sql.SQL("GRANT pacientes TO {}").format(sql.Identifier(USUARIO))) #Cambiar el nombre del rol al que se asigne el usuario
    conn.commit()
    conn.close()


def infermer(USUARIO, CONTRASEÑA):
    if usuario_existente(USUARIO):
        print("El usuario ya existe.")
        return
    USUARIO_ENC = generate_password_hash(USUARIO, method='pbkdf2:sha256')
    PASWORD_ENC = generate_password_hash(CONTRASEÑA, method='pbkdf2:sha256')
    Cargar_csv(USUARIO_ENC, PASWORD_ENC)
    conn1 = psycopg2.connect(
        dbname="hr",
        user="postgres",
        password="unai",  
        host="192.168.56.108",
    )
    cur1 = conn1.cursor()
    cur1.execute(sql.SQL("CREATE ROLE {} LOGIN PASSWORD %s").format(sql.Identifier(USUARIO)), (CONTRASEÑA,))
    cur1.execute(sql.SQL("GRANT CONNECT ON DATABASE hr TO {}").format(sql.Identifier(USUARIO)))
    cur1.execute(sql.SQL("GRANT infermers TO {}").format(sql.Identifier(USUARIO))) #Cambiar el nombre del rol al que se asigne el usuario
    conn1.commit()
    conn1.close()

def metge(USUARIO, CONTRASEÑA):
    if usuario_existente(USUARIO):
        print("El usuario ya existe.")
        return
    USUARIO_ENC = generate_password_hash(USUARIO, method='pbkdf2:sha256')
    PASWORD_ENC = generate_password_hash(CONTRASEÑA, method='pbkdf2:sha256')
    Cargar_csv(USUARIO_ENC, PASWORD_ENC)
    conn1 = psycopg2.connect(
        dbname="hr",
        user="postgres",
        password="unai",  
        host="192.168.56.108",
    )
    cur1 = conn1.cursor()
    cur1.execute(sql.SQL("CREATE ROLE {} LOGIN PASSWORD %s").format(sql.Identifier(USUARIO)), (CONTRASEÑA,))
    cur1.execute(sql.SQL("GRANT CONNECT ON DATABASE hr TO {}").format(sql.Identifier(USUARIO)))
    cur1.execute(sql.SQL("GRANT medico TO {}").format(sql.Identifier(USUARIO))) #Cambiar el nombre del rol al que se asigne el usuario
    conn1.commit()
    conn1.close()

def administratiu(USUARIO, CONTRASEÑA):
    if usuario_existente(USUARIO):
        print("El usuario ya existe.")
        return
    USUARIO_ENC = generate_password_hash(USUARIO, method='pbkdf2:sha256')
    PASWORD_ENC = generate_password_hash(CONTRASEÑA, method='pbkdf2:sha256')
    Cargar_csv(USUARIO_ENC, PASWORD_ENC)
    conn1 = psycopg2.connect(
        dbname="hr",
        user="postgres",
        password="unai",  
        host="192.168.56.108",
    )
    cur1 = conn1.cursor()
    cur1.execute(sql.SQL("CREATE ROLE {} LOGIN PASSWORD %s").format(sql.Identifier(USUARIO)), (CONTRASEÑA,))
    cur1.execute(sql.SQL("GRANT CONNECT ON DATABASE hr TO {}").format(sql.Identifier(USUARIO)))
    cur1.execute(sql.SQL("GRANT administrativos TO {}").format(sql.Identifier(USUARIO))) #Cambiar el nombre del rol al que se asigne el usuario
    conn1.commit()
    conn1.close()

def neteja(USUARIO, CONTRASEÑA):
    if usuario_existente(USUARIO):
        print("El usuario ya existe.")
        return
    USUARIO_ENC = generate_password_hash(USUARIO, method='pbkdf2:sha256')
    PASWORD_ENC = generate_password_hash(CONTRASEÑA, method='pbkdf2:sha256')
    Cargar_csv(USUARIO_ENC, PASWORD_ENC)
    conn1 = psycopg2.connect(
        dbname="hr",
        user="postgres",
        password="unai",  
        host="192.168.56.108",
    )
    cur1 = conn1.cursor()
    cur1.execute(sql.SQL("CREATE ROLE {} LOGIN PASSWORD %s").format(sql.Identifier(USUARIO)), (CONTRASEÑA,))
    cur1.execute(sql.SQL("GRANT CONNECT ON DATABASE hr TO {}").format(sql.Identifier(USUARIO)))
    cur1.execute(sql.SQL("GRANT neteja TO {}").format(sql.Identifier(USUARIO))) #Cambiar el nombre del rol al que se asigne el usuario
    conn1.commit()
    conn1.close()

#Carrega de informació al CSV
def Cargar_csv(dato1,dato2):
        with open(archivo_csv, 'a', newline='',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([dato1,dato2])

#Inici de sesió 
def Login(USUARIO, CONTRASEÑA):
    try:
        credenciales_validas = False  
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector_csv = csv.reader(csvfile, delimiter=';')
            next(lector_csv)  
            for fila in lector_csv:
                hash_usuario = fila[0]
                hash_contraseña = fila[1]
                if check_password_hash(hash_usuario, USUARIO) and check_password_hash(hash_contraseña, CONTRASEÑA):
                    print("Credenciales válidas. Conectando a la base de datos...")            
                    credenciales_validas = True 
   #                 conn = psycopg2.connect(
    #                    dbname="hr",
     #                   user=USUARIO,
      #                  password=CONTRASEÑA,
       #                 host="192.168.56.108"
       #             )
                    credenciales_validas = True  
    
        if credenciales_validas==False:
            print("Credenciales no válidas")
    except Exception as e:
        return False