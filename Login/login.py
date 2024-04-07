import csv
from werkzeug.security import generate_password_hash, check_password_hash
import pwinput
import psycopg2
import os
from psycopg2 import sql

# Define el nombre del archivo CSV
archivo_csv = 'A.csv'

# Definimos los títulos para el archivo CSV
Titols=["Usuario","Contraseña"]

#Creamos archivo CSV si no existe
def Crear_csv():
    with open(archivo_csv, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(Titols)

# Verificamos si el usuario ya existe en el archivo CSV
def usuario_existente(usuario):
    try:
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector_csv = csv.reader(csvfile, delimiter=';')
            next(lector_csv)  # Saltamos la primera fila (títulos)
            for fila in lector_csv:
                hash_usuario = fila[0]
                if check_password_hash(hash_usuario, usuario):
                    return True
    except Exception as e:
        print("Usuario Existente")
        return False

# Registramos un nuevo usuario en el sistema
def Registro(USUARIO, CONTRASEÑA):
    if usuario_existente(USUARIO):
        print("El usuario ya existe.")
        return
    USUARIO_ENC = generate_password_hash(USUARIO, method='pbkdf2:sha256') #Encriptamos usuario
    PASWORD_ENC = generate_password_hash(CONTRASEÑA, method='pbkdf2:sha256') #Encriptamos contraseña
    Cargar_csv(USUARIO_ENC, PASWORD_ENC)
    
    # Conexión a la base de datos PostgreSQL
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

# Cargamos datos en el archivo CSV
def Cargar_csv(dato1,dato2):
    with open(archivo_csv, 'a', newline='',encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([dato1,dato2])

# Iniciamos sesión de un usuario
def Login(USUARIO, CONTRASEÑA):
    try:
        credenciales_validas = False  
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector_csv = csv.reader(csvfile, delimiter=';')
            next(lector_csv)
            for fila in lector_csv: #Recorremos el fichero para comprobar credenciales
                hash_usuario = fila[0]
                hash_contraseña = fila[1]
                if check_password_hash(hash_usuario, USUARIO) and check_password_hash(hash_contraseña, CONTRASEÑA): 
                    print("Credenciales válidas. Conectando a la base de datos...")
                    credenciales_validas = True  

        if credenciales_validas == False:
            print("Credenciales no válidas")
    except Exception as e:
        return False
