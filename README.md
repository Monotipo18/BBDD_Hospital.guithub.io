# Document Final d'instalacio
## Contingut

### Projecte Intermodular
### Explicacio
La idea en este proyecto consiste en que el Hospital de Blanes era hospital petit amb pocs pacients i poca dotació de personal, però l’increment d’habitants tant a Blanes com a Lloret ha canviat la realitat. Per això la Direcció del Centre es planteja començar a informatitzar l’Hospital, a partir de esta idea tenemos que crear todo el sistema informatico para el "Hospital de Blanes", eso incluye Base de Datos, aplicacion, seguridad, esquemas de BD, Exportacion de datos, alta disponibilidad etc.

Para poder implentar este proyecto desde 0, se recomienda seguir todos los pasos que hay en este documento para obtener una version final y funcional de sistema informatica con BD.

### Conectividad y Login

Para empezar lo ideal seria crear una "Aplicacion" en Python (en este caso no grafico debido a que se tardaria demasiado tiempo), para que el Administrador informatico pueda realizar las siguientes tareas:

  -  Connectar amb una base de dades des d’un entorn de programació Python.
  -  Poder registrar-se i iniciar sessió al programa.
  -  Guardar en un fitxer separat les dades del login: usuari i contrasenya.

Aparte de las tareas anteriormente mencionadas, se ha de tener en cuenta que al guardar los datos de login y registro se esta poniendo en riesgo la seguridad de estas.
Es por eso que se tiene que aplicar alguna medida de seguridad para evitar problemas innecesarios, una manera de hacerlo seria encriptando los datos de login y registro
que se guardan en el fichero aparte.

> [!WARNING]  
> Es muy importante mencionar que no se recomienda en lo mas minimo guardar datos de inicio de sesion, debido a los riesgos que conlleva.
>
Para poder implentar tanto las caracteristicas de la "Aplicacion" como la de Encriptacion se han de instalar las siguientes librerias de Python
  -  ```Pwinput``` :  Utilizada para enmascarar los caracteres escritos en una cadena de texto.
  -  ```Psycopg2```:  Ens permet treballar amb bases de dades PostgreSQL des de Python
  -  ```Werkzeug.security```: Te funcions per treballar amb seguretat i autenticació en aplicacions de tipus 'hash'

Para poder aprender a utilizar estas librerias se recomienda consultar la Documentacion del apartado de:
[Bloque de Conectividad y Login](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/blob/main/Login/Documentacion_Login.md)
Ademas en la documentacion adjuntado se puede utilizar los codigos ```.py``` adjuntados para utilizarlos segun las necesidades.

> [!NOTE]  
> Como aun no se ha creado ni la Base de Datos ni su Esquema se recomienda hacer pruebas en un entorno Local.

### Esquema BD Relacional

Practicamente el apartado mas importante de este proyecto, sin base de datos no tenemos lugar para almacenar y administrar los datos del "Hospital",
pero para crear una base de datos lo ideal es tener un esquema de como sera la BD.

En este caso como se esta diseñando una BD para un hospital se requiere que se guarde todo tipo de Datos, desde informacion de pacientes o medicos, hasta las habitaciones disponibles del hospital o incluso los aparatos 
medicos que se encuentran en cada Quirofano.

Es por eso que se ha optado por creado crear el esquema del Hospital de la siguiene manera:

![image](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/assets/161468108/a37ed38d-f391-4758-bd1d-63ff24d4aeb3)

Para obtener una mejor explicacion mucho mas detallada de que contienen cada Entidad y sus atributos se recomienda visitar el apartado de :
[Esquema BBDD](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/blob/main/Esquema_BDD/esquema/readme.md)

En esa documentacion se encuentran 2 esquemas distintos (es el mismo pero diferente visualizacion) y un script ```.sql``` para crear las tablas y columnas de toda la BD, se puede modificar y ajustar el
script pero se considera que la forma que se ha hecho es la mas adiente.

### Esquema de Seguridad

Dado los diferentes trabajadores que hay en el hospital se ha hecho una Matriu de seguretat on apareixin els usuaris/rols i los diferentes permissos que tenen sobre els objectes(datos) de la BD.
Es por eso que ha modo de resumen los roles que van a existtir en la BD son los siguientes:

  -  Metges
  -  Infermers
  -  Zeladors
  -  Administratius
  -  Pacients
  -  Conductors d'ambulancia

Para ver los permisos detalladamente se recomienda consultar la siguiente documentacion del Esquema de seguridad:

[Usarios, Grupos y Permisos](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/tree/main/Esquema%20de%20seguretat/Matriu%20de%20Seguretat)



