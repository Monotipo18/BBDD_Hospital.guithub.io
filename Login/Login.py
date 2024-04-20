import csv
from werkzeug.security import generate_password_hash, check_password_hash
import pwinput
import psycopg2
import os
from psycopg2 import sql
archivo_csv = 'Patata.csv'

#CREACIÓ DEL FITXER
def Crear_csv():
    Titols=["Usuario","Contraseña"]
    with open(archivo_csv, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(Titols)

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
        return False
        print("Usuario Existente")
#Registre del usuari
def Registro(USUARIO, CONTRASEÑA):
    if usuario_existente(USUARIO):
        print("El usuario ya existe.")
        return
    USUARIO_ENC = generate_password_hash(USUARIO, method='pbkdf2:sha256')
    PASWORD_ENC = generate_password_hash(CONTRASEÑA, method='pbkdf2:sha256')
    Cargar_csv(USUARIO_ENC, PASWORD_ENC)
    #conn = psycopg2.connect(
    #    dbname="Redis",
    #    user="postgres",
    #    password="P@ssw0rd",
    #    host="192.168.56.106",
    #)
    #cur = conn.cursor()
    #cur.execute(sql.SQL("CREATE ROLE {} LOGIN PASSWORD %s").format(sql.Identifier(USUARIO)), (CONTRASEÑA,))
    #conn.commit()
    #conn.close()
#Carrega de informació al CSV
def Cargar_csv(dato1,dato2):
        with open(archivo_csv, 'a', newline='',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([dato1,dato2])
#Inici de sesió 
def Login(USUARIO, CONTRASEÑA):
    try:
        credenciales_validas = False  
        Salir_CSV=False
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector_csv = csv.reader(csvfile, delimiter=';')
            next(lector_csv)  
            for fila in lector_csv:
                hash_usuario = fila[0]
                hash_contraseña = fila[1]
            Salir_CSV=True
            if check_password_hash(hash_usuario, USUARIO) and check_password_hash(hash_contraseña, CONTRASEÑA):
                print("Credenciales válidas. Conectando a la base de datos...")
                #conn = psycopg2.connect(
                #    dbname="BDDD",
                #    user=USUARIO,
                #    password=CONTRASEÑA,
                #    host="192.168.56.110"
                #)
                credenciales_validas = True 
        if credenciales_validas==False:
            print("Credenciales no válidas")
    except Exception as e:
        return False
