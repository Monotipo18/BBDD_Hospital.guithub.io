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
#### Roles y Permisos
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

Ademas de ver los permisos que tienen los roles de usuario y grupo de la BD , lo ideal seria crear un script ```.sql``` para implementar la creacion Usuarios, grupos y permisoa 
de una sola vez para asi no ir implentando tantos comandos de uno en uno.

> [!NOTE]  
> El Script ```.sql``` tambien se encuentra en el mismo Bloque que la documentacion de permisos( el enlace adjuntado), tambien hay una tabla en excel para entender mejor los permisos.

#### SSL-TLS

Primer de tot cal aclarir una cosa SSL, avui dia no s'utilitza, ja que el protocol TLS (Transport Layer Security) el va substituir en 1999, a dia d'avui, 12 d'abril de 2024, és l'estàndard en la seva versió TLS 1.3, però el terme SSL es continua utilitzant per a referir-se a connexions segures.

Una vez los roles y permisos esten creados, se ha de implementar una encriptacion del trafico de la BD, porque?, por la sencilla razon de que SSL permite cifrar el tráfico de datos, eso es muy conveniente
ya que si los datos no esta cifrados un intermediarios podria interceptar los datos ( Man in the Middle) y eso en una BD de un hospital es totalmente inpensable.

Pero antes de aplicar un certificado SSL, se ha decido utilizar un domino con ```Cloudfare``` para que sea un poco mas seguro (se evitan ataques DDDOS) y ademas la renovacion automatica del certificado sera mas facil.

> [!NOTE]  
> Cloudfare es el servicio que se esta utilizandpo en este caso, pero se pueden utilizar otras opciones distintasa que ofrecen el mismo servicio
> aunque por nuestra parte se recomienda utilizar este servicio.

Es muy importante configurar el firewall donde este instalado la BD ya que un mala configuracion de puertos puede suponer un gran riesgo en la seguridad del sistema.

#### Generar Certificado 

Para generar el certificado SSL-TLS para la base de datos del Hospital se necesita una herramienta, en este caso se ha decidido utilizar Certbot, como la BD esta instalada en un Debian en ```PROMOX```
una vez creado y configurado el certificado SSL se tendra que configurar el Postgresql para que tambien lo implente.

Para poder hacer todos los pasos anteriormente mencionados, se recomienda seguir todos los pasos de la siguiente documentacion SSL-TLS:

  -  [Configuracion Firewall y SSL](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/tree/main/Esquema%20de%20seguretat/SSL-TLS)

#### Data Masking

Un paso muy importante que ayudara a proteger aun mas los datos de la BD, es implementar Data Masking a los datos de caracter mas importante, para poder hacer




