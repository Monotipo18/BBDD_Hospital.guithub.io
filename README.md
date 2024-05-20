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

Un paso muy importante que ayudara a proteger aun mas los datos de la BD, es implementar Data Masking a los datos de caracter mas importante. Pero antes de aplicar Data Masking
hay que saber que tipo de datos se consideran de caràcter personal de grau alt en una based de datos de un hospital, a continuacion se presenta algunaos ejemplos de ello:

  -  Informació d'Identificació Personal (PII)
  -  Informació Mèdica Sensible
  -  Informació Financera
  -  Informació Laboral i d'Assegurança

Una vez se sabe con que tipo de datos se va a trabajar, es recomendable hacer un estudio para saber a que datos de la BD se va aplicar el Data Masking teniendo en cuenta los apartados anteriormente mencionados.

Para poder configurar el Data Masking es necessario instalar y configurar una serie de herramientas, una de ellas es el repositorio de github ```pg_anonymize``` , esta repositiorio permite aplicar una serie de parametros y configuraciones en Postgresql ( se puede hacer a traves de PgAdmin) para poder anonimizar los datos que se consideren de caracter personal de grado alto.

Pero para realizar todo esto se recomienda seguir los pasos que se encuentra en la siguiente documentacion:

-  [Data Masking](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/blob/main/Esquema%20de%20seguretat/Data_Masking/readme.md)

Con esta documentacion se podran instalar las herramientas neccesarias para poder configurar Postgresql para aplicar el respectivo DataMasking. Ademas explica en mas detalle que tipo de datos de caracter personal son de grado alto.

#### Legislacion AGPD

Respecto a la legislacion AGPD es un apartado bastante extenso , es por eso que se ha considerado dividir la proteccion de datos y documentacion en 3 apartado distintos:

  -  Requisitos Altos:  Els enmascararem amb Data masking dins de la base de dades juntament amb SSL per tenir encriptada la conecció entre el servidor i la BDD. A mes restringirem el acces a les dades depenent de la teva profecio dins de l'hospital.
  -  Requisitos Intermedios: Tot i que l'informacio que contenen els documents es menys relevant que els anteriors, encara s'han d'encriptar dades personals importants com DNI, telefons, noms, etc. Utilitzarem datamasking i el SSL com en l'anterior.
  -  Requisitos Bajos: Aquest documents son necesaris i obligatoris, pero poc relevants, per tant tindran poca necesitat d'encriptació. Utilitzarem datamasking minimament i l'encriptacio SSL

Cabe mencionar que el hospital implementa diferentes tecnicas para asegurar, proteger y minimizar el acceso a todo tipos de datos del hospital mediante medidas de seguridad tenicas, 
analisis de riesgos, mediadas de seguridad organizativas, gestion de acceso, proteccion de la infraestructura fisica, revisiones y actualizaciones y por ultimo en Procediments de Seguretat en Cas d'Incidents.

En la siguiente apartado adjuntado se explica muchos mas en detalle como se aplican esta serie de tecnicas y que tipos de datos se consideran de mayor o menor importancia y muchos muchas detalles:

-  [Legislacion AGPD](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/blob/main/Esquema%20de%20seguretat/Documentacion%20RGPD/Documento%20de%20seguridad.md)

### Bloque de Mantenimiento

El bloque de mantenimiento es un apartado para mejorar el anterior apartado de Conectividadad y Login, parea realizar eso se plante realizar las siguientes tareas e implementarlas en la aplicacion:

   1. Donar d’alta nou personal al centre (metge/ssa, infermer/a, administratiu/va,neteja…)
   2. Donar d’alta nous pacients.
   3. Pel personal d’infermeria, saber si depèn d’un metge/ssa o bé és de planta.
   4. Per un determinat dia, saber per a cada quiròfan, les operacions que hi ha previstes, el pacient a operar, l’hora, el metge/ssa que les farà i el personal d’infermeria que intervindrà.
   5. Per un determinat dia, saber les visites que hi ha planificades, l’hora d’entrada, el metge/ssa i el pacient.
   6. Amb PGPLSQL crea dos procediments/funcions/triggers per gestionar/validar la informació que esteu entrant des del manteniment.
   7. Donada una habitació cal saber les reserves previstes, mostrant la data ingrés, data prevista de sortida i el pacient que l’ocuparà.
   8. Donat un/a pacient saber les visites que ha fet, el diagnòstic, els medicaments que li han receptat, les vegades que ha estat ingressat/da (en cas que ho hagi estat ), així com saber les vegades que ha passat pel quiròfan ( en cas que l’hagin operat).
   9. Donat un/a metge/ssa saber les visites i les operacions que té programades i les seves hores disponibles.
   10. Per a cada quiròfan és vol saber quants aparells mèdics té assignat i quina quantitat (per exemple, el quiròfan 1 de la primera planta té assignats 2 respiradors, 2 equips d’oxigen, etc.)

Para poder realizar estos apartados, previamente se han de instalar las siguientes librerias de pyhton:

  -  ```Pwinput```
  -  ```Psycopg2```
  -  ```Werkzeug.security```
  -  ```Tabulate```: La biblioteca tabulate en Python proporciona una manera convenient de formatar dades tabulars en una varietat d'estils.
  -  ```Dotenv```  : Es una eina útil en el món de Python per gestionar les variables d'entorn d'una manera senzilla i eficaç.

Para aprender en mas detalle como funcionan y como utilizar estas libreria es recomendable visitar el siguiente apartado, ademas cuenta con las funciones, procedimientos y triggers junto con los codigos mejorados del apartado de Conectividad y Login para poder modificarlos segun las necesidades:

  -  [Bloque de Mantenimiento](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/tree/main/Bloc%20de%20Manteniment)

> [!TIP]
> Aunque este apartado aun no contiene la version final de l'aplicacion se recomienda hacerlo para evitar confusiones.

### Alta disponibilitat


 
  


















