import psycopg2
from psycopg2 import sql
import pwinput 
import csv
import os
import simplecrypt
archivo_csv = 'A.csv'

def encrypt(plaintext, password):
    Texto_Cifrado = simplecrypt.encrypt(password, plaintext)
    return Texto_Cifrado

def decrypt(ciphertext, password):
    Texto_Plano = simplecrypt.decrypt(password, ciphertext)
    return Texto_Plano

def Login():
    try:
        USUARIO = input("Introduce tu Usuario: ")
        PASWORD=pwinput.pwinput("Introduce tu Contraseña: ")
        conn = psycopg2.connect(
            dbname="pagila",
            user=USUARIO,
            password=PASWORD,
            host="192.168.56.106"
        )
        print("Login Correctament")
    except:
        print("Error:")

#CREACION DE USUARIOS: 
def Registro():
    conn = psycopg2.connect(
    dbname="pagila",
    user="postgres",
    password="P@ssw0rd",
    host="192.168.56.106"
)
    cursor = conn.cursor()    
    USUARIO=input("Introduce tu Usuario: ")
    PASWORD=pwinput.pwinput("Introduce tu Contraseña: ")
    PASWORD_ENC = encrypt(PASWORD, 'password')
    cursor.execute(sql.SQL("CREATE ROLE {} LOGIN PASSWORD %s").format(sql.Identifier(USUARIO)), (PASWORD,))
    conn.commit()
    conn.close()
    with open(archivo_csv, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(["Usuario","Contraseña"])
            writer.writerow([USUARIO,PASWORD_ENC ])