import psycopg2
from psycopg2 import sql
import pwinput 
import csv
import os
import simplecrypt
from werkzeug.security import generate_password_hash, check_password_hash
archivo_csv = 'A.csv'

def Crear_csv():
    with open(archivo_csv, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Usuario","Contraseña"])
def Login():
    try:
        USUARIO = input("Introduce tu Usuario: ")
        CONTRASEÑA = input("Introduce tu Contraseña: ")
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector_csv = csv.reader(csvfile, delimiter=';')
            next(lector_csv)  
            for fila in lector_csv:
                usuario_hash = fila[0]
                contraseña_hash = fila[1]
                if check_password_hash(usuario_hash, USUARIO) and check_password_hash(contraseña_hash, CONTRASEÑA):
                    print("Credenciales válidas. Conectando a la base de datos...")
                    #conn = psycopg2.connect(
                    #    dbname="pagila",
                    #    user=USUARIO,
                    #    password=CONTRASEÑA,
                    #    host="192.168.56.106"
                    #)
                    # Aqui los SELECT,UPDATES,DELTE OPERACIONES
                    #return conn
    except Exception as e:
        print("Error:", e)

#CREACION DE USUARIOS:

def Registro():
    USUARIO=input("Introduce tu Usuario: ")
    PASWORD=pwinput.pwinput("Introduce tu Contraseña: ")
    conn = psycopg2.connect(
    dbname="pagila",
    user="postgres",
    password="P@ssw0rd",
    host="192.168.56.106"
)
    cursor = conn.cursor()    
    USUARIO_ENC = generate_password_hash(USUARIO, method='pbkdf2:sha256')
    PASWORD=pwinput.pwinput("Introduce tu Contraseña: ")
    PASWORD_ENC = generate_password_hash(PASWORD, method='pbkdf2:sha256')
    #cursor.execute(sql.SQL("CREATE ROLE {} LOGIN PASSWORD %s").format(sql.Identifier(USUARIO)), (PASWORD,))
    conn.commit()
    conn.close()
    Crear_csv()
    with open(archivo_csv, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([USUARIO_ENC,PASWORD_ENC ])