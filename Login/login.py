import csv
from werkzeug.security import generate_password_hash, check_password_hash
import pwinput
import psycopg2
import os
from psycopg2 import sql
archivo_csv = 'A.csv'
Titols=["Usuario","Contraseña"]

def Crear_csv():
    with open(archivo_csv, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(Titols)


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

def Registro(USUARIO, CONTRASEÑA):
    if usuario_existente(USUARIO):
        print("El usuario ya existe.")
        return
    USUARIO_ENC = generate_password_hash(USUARIO, method='pbkdf2:sha256')
    PASWORD_ENC = generate_password_hash(CONTRASEÑA, method='pbkdf2:sha256')
    Cargar_csv(USUARIO_ENC, PASWORD_ENC)
    conn = psycopg2.connect(
        dbname="Hospital_Pruebas",
        user="ASIXProyecto",
        password="@s1xPr0y4ct0",
        host="snakeeater.equemmfoundation.top",
    )
    cur = conn.cursor()
    cur.execute(sql.SQL("CREATE ROLE {} LOGIN PASSWORD %s").format(sql.Identifier(USUARIO)), (CONTRASEÑA,))
    conn.commit()
    conn.close()

def Cargar_csv(dato1,dato2):
        with open(archivo_csv, 'a', newline='',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([dato1,dato2])
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
                    conn = psycopg2.connect(
                        dbname="BDDD",
                        user=USUARIO,
                        password=CONTRASEÑA,
                        host="192.168.56.110"
                    )

                    credenciales_validas = True  

        if credenciales_validas==False:
            print("Credenciales no válidas")
    except Exception as e:
        return False
    
