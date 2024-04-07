
# PROJECTE PROGRAMACIO Y BASE DE DADES

## Projecte Intermodular

### Contenido

- [Biblioteca](#biblioteca)
- [Pwinput, què és i per a què s'utilitza](#pwinput-què-és-i-per-a-què-sutilitza)
- [Psycopg2, què és i per a què s'utilitza](#psycopg2-què-és-i-per-a-què-sutilitza)
- [werkzeug.security, què és i per a què s'utilitza](#werkzeugsecurity-què-és-i-per-a-què-sutilitza)

#  **Biblioteca:**

### **Pwinput, què és i per a què s'utilitza**

Es una biblioteca original de Python utilizada para enmascarar los caracteres escritos en una cadena de texto, generalmente utilizada en aplicaciones donde haya que mantener una seguridad.

Esta Biblioteca utiliza dos funciones principalmente:
1. `getpass.getpass()` que oculta el password introducido por pantalla y lo devuelve como una cadena vacía.
2. `pwinput.pwinput()` que muestra un caracter a nuestra eleccion (*) en lugar del carácter introducido por password.

Para la instalacion de la biblioteca utilizamos:
`pip install pwinput`

Link oficial de la documentación
[Documentación oficial de pwinput](https://pypi.org/project/pwinput/)


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

