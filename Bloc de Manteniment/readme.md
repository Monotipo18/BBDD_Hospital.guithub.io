# PROJECTE PROGRAMACIO Y BASE DE DADES

## Projecte Intermodular

### Contenido

1. [Biblioteca](#biblioteca)
    - [Pwinput, què és i per a què s'utilitza](#pwinput-què-és-i-per-a-què-sutilitza)
    - [Psycopg2, què és i per a què s'utilitza](#psycopg2-què-és-i-per-a-què-sutilitza)
    - [werkzeug.security, què és i per a què s'utilitza](#werkzeugsecurity-què-és-i-per-a-què-sutilitza)
    - [Tabulate, què és i per a què s'utilitza](#Tabulate-què-és-i-per-a-què-sutilitza)
    - [Dotenv, què és i per a què s'utilitza](#Dotenv-què-és-i-per-a-què-sutilitza)

#  **Biblioteca:**

### **Pwinput, què és i per a què s'utilitza**


És una biblioteca original de Python utilitzada per enmascarar els caràcters escrits en una cadena de text, generalment utilitzada en aplicacions on cal mantenir una seguretat.

Aquesta biblioteca utilitza principalment dues funcions:
1. `getpass.getpass()` que oculta la contrasenya introduïda per pantalla i la retorna com a una cadena buida..
2. `pwinput.pwinput()` que mostra un caràcter a la nostra elecció (*) en lloc del caràcter introduït per la contrasenya.

Per instal·lar la biblioteca, utilitzem:
`pip install pwinput`

### **Psycopg2, què és i per a què s'utilitza**

La biblioteca psycopg2 és un adaptador entre PostgreSQL i Python. És a dir, ens permet treballar amb bases de dades PostgreSQL des de Python.

Per instal·lar la biblioteca utilitzem:
`pip install psycopg2`

### **Werkzeug.security, què és i per a què s'utilitza**

És un mòdul de la biblioteca Werkzeug, una col·lecció d'utilitats WSGI (Web Server Gateway Interface) per a Python, proporcionant funcions per treballar amb seguretat i autenticació en aplicacions de tipus 'hash'.
Ofereixen funcionalitats entre les que destaquen:

1. `generate_password_hash`: Utilitzada per generar un hash segur d'una contrasenya. Això és útil per emmagatzemar contrasenyes de forma segura en un arxiu.
   
   exemple de funcionament:
   
        password = "contraseña123"
        hashed_password = generate_password_hash(password)
        
        print("Contraseña original:", password)
        print("Hash generado:", hashed_password)

2. `check_password_hash`: Utilitzada per verificar si una contrasenya proporcionada coincideix amb un hash emmagatzemat a la base de dades.
   
   exemple de funcionament:
   
       password = "contraseña123"
       hashed_password = generate_password_hash(password)
       password_to_check = "contraseña123"
       if check_password_hash(hashed_password, password_to_check):
         print("La contraseña es válida.")
       else:
         print("La contraseña no es válida.")
   
3. `generate_password_reset_token`: Utilitzada per generar un token segur per restablir una contrasenya oblidada.
   
   exemple de funcionament:
   
         user_id = 123
         reset_token = generate_password_reset_token(user_id)
         print("Token de restablecimiento de contraseña:", reset_token)
   
4. `validate_password_reset_token`: Utilitzada per validar un token de restabliment de contrasenya abans de permetre que es canviï la contrasenya.

   exemple de funcionament:
   
        reset_token = "token_generado_anteriormente"
        user_id = 123
        
        if validate_password_reset_token(reset_token, user_id):
          print("El token es válido. Se puede restablecer la contraseña.")
        else:
          print("El token no es válido o ha caducado.")

La probabilitat de col·lisió és infíma, al voltant de 2^128, ja que `werkzeug.security` utilitza algoritmes de hash segurs, com ara SHA-256 i SHA-512, i també aplica un "salt" que crea una cadena aleatòria única a la nostra encriptació fent-la encara més efectiva contra atacs de força bruta i cerca de col·lisions.

### **Tabulate, què és i per a què s'utilitza**

La biblioteca **tabulate** en Python proporciona una manera convenient de formatar dades tabulars en una varietat d'estils, com ara taules ASCII, Markdown, HTML i més. És especialment útil quan necessites imprimir dades tabulars de manera llegible a la consola o generar taules en diferents formats per a ús en documents, informes o pàgines web.

Aquesta biblioteca pren una llista de llistes o una llista de tuples que representen files d'una taula, i opcionalment una llista que especifica els encapçalaments de columna. Llavors, formateja aquestes dades en una taula amb vores, alineació de columnes i altres estils segons les preferències especificades.

Per exemple, pots utilitzar **tabulate** per imprimir dades d'una base de dades en una taula ASCII ben formatada a la consola o generar una taula HTML per mostrar en una pàgina web.

Per instal·lar la biblioteca utilitzem:
`pip install tabulate`

### **Dotenv, què és i per a què s'utilitza**

La biblioteca **python-dotenv**, o simplement **dotenv**, és una eina útil en el món de Python per gestionar les variables d'entorn d'una manera senzilla i eficaç. Les variables d'entorn són valors que es poden utilitzar en una aplicació i que es troben fora del codi font. Això inclou informació com ara claus d'API, contrasenyes de bases de dades, URL de serveis externs, etc.

La funció principal de **python-dotenv** és llegir fitxers de configuració formats com a `.env` i carregar les seves variables d'entorn en el context de l'aplicació Python. Això facilita la gestió de configuracions sensibles, ja que les variables d'entorn es poden mantenir separades del codi font i, per tant, fora del control de versions.

Per instal·lar la biblioteca utilitzem:
`pip install python-dotenv`

#### Utilització de dotenv

Per utilitzar **python-dotenv**, primer has de crear un fitxer `.env` al directori arrel del teu projecte. Aquest fitxer contindrà les variables d'entorn en el format `NOM_VARIABLE=valor`. Després, pots importar la biblioteca al teu codi Python i cridar la funció `load_dotenv()` per carregar les variables d'entorn des del fitxer `.env`.

Exemple sencill d'ús de dotenv:

```python
from dotenv import load_dotenv
import os

load_dotenv()
# Carrega les variables d'entorn des del fitxer .env
load_dotenv()

# Accedeix a les variables d'entorn carregades
API_KEY = os.getenv("API_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")
```

D'aquesta manera, pots utilitzar les variables `API_KEY` i `DB_PASSWORD` al teu codi sense exposar les seves valors directament al codi font. Això millora la seguretat i la portabilitat de l'aplicació.

### Webgrafia

- [Documentació oficial de pwinput](https://pypi.org/project/pwinput/)
- [Documentació oficial de Psycopg2](https://www.psycopg.org)
- [Documentació de Werkzeug](https://github.com/pallets/werkzeug)
- [Documentació de Tabulate](https://python-para-impacientes.blogspot.com/2017/01/tablas-con-estilo-con-tabulate.html)
- [Documentació de Dotenv](https://pypi.org/project/python-dotenv/)