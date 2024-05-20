# Document Final d'instalacio
## Hospital: Equilibri neurodivergent

## Contingut
  -  [Conectivitat i Login](#conectivitat-i-login)
  -  [Esquema BD Relacional](#esquema-bd-relacional)
  -  [Esquema de Seguretat](#esquema-de-seguretat)
  -  [Bloc de Mantenimient](#bloc-de-mantenimient)
  -  [Alta Disponibilitat](#alta-disponibilitat)
  -  [Bloc de Consultes](#bloc-de-consultas)
  -  [Dummy Data](#dummy-data)
  -  [Exportacio de Dades](#exportacio-de-dades)
  -  [Manual d'usuari](#manual-dusuari)
  -  [Extra 1: Logs](#extra-1-logs-bd)
### Projecte Intermodular
### Explicacio
La idea en aquest projecte consisteix que l'Hospital de Blanes era un hospital petit amb pocs pacients i poca dotació de personal, però l’increment d’habitants tant a Blanes com a Lloret ha canviat la realitat. Per això la Direcció del Centre es planteja començar a informatitzar l’Hospital. A partir d'aquesta idea, hem de crear tot el sistema informàtic per a l'"Hospital de Blanes", que inclou base de dades, aplicació, seguretat, esquemes de BD, exportació de dades, alta disponibilitat, etc.

Per poder implementar aquest projecte des de zero, es recomana seguir tots els passos que hi ha en aquest document per obtenir una versió final i funcional del sistema informàtic amb BD.

---

### Conectivitat i Login

Per començar, l'ideal seria crear una "Aplicació" en Python (en aquest cas no gràfica, ja que trigaria massa temps), perquè l'administrador informàtic pugui realitzar les següents tasques:

- Connectar amb una base de dades des d’un entorn de programació Python.
- Poder registrar-se i iniciar sessió al programa.
- Guardar en un fitxer separat les dades del login: usuari i contrasenya.

A part de les tasques anteriorment mencionades, s'ha de tenir en compte que al guardar les dades de login i registre s'està posant en risc la seguretat d'aquestes. És per això que s'ha d'aplicar alguna mesura de seguretat per evitar problemes.

> [!WARNING]  
> És molt important mencionar que no es recomana en el més mínim guardar dades d'inici de sessió, degut als riscos que comporta.

Per poder implementar tant les característiques de l'Aplicació com la d'Encriptació, cal instal·lar les següents llibreries de Python:

- `Pwinput`: Utilitzada per enmascarar els caràcters escrits en una cadena de text.
- `Psycopg2`: Ens permet treballar amb bases de dades PostgreSQL des de Python.
- `Werkzeug.security`: Té funcions per treballar amb seguretat i autenticació en aplicacions de tipus 'hash'.

Per poder aprendre a utilitzar aquestes llibreries, es recomana consultar la documentació del següent apartat:
  -  [Bloc de Conectivitat i Login](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/blob/main/Login/Documentacion_Login.md)
A més, en la documentació adjunta es poden utilitzar els codis ```.py``` adjuntats per utilitzar-los segons les necessitats.

> [!NOTE]  
> Com que encara no s'ha creat ni la Base de Dades ni el seu Esquema, es recomana fer proves en un entorn local..

### Esquema BD Relacional

Pràcticament, l'apartat més important d'aquest projecte, sense una base de dades no tenim cap lloc per emmagatzemar i gestionar les dades de l'"Hospital". Però per crear una base de dades, l'ideal és tenir un esquema de com serà la BD.

En aquest cas, com que s'està dissenyant una BD per a un hospital, caldrà guardar tot tipus de dades, des d'informació de pacients o metges,
fins a les habitacions disponibles de l'hospital o fins i tot els aparells mèdics que es troben a cada Quiròfan.

És per això que s'ha optat per crear l'esquema de l'Hospital de la següent manera:


![image](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/assets/161468108/a37ed38d-f391-4758-bd1d-63ff24d4aeb3)

Per obtenir una explicació molt més detallada de què contenen cada Entitat i els seus atributs, es recomana visitar el apartat de:
[Esquema BBDD](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/blob/main/Esquema_BDD/esquema/readme.md)

En aquesta documentació es troben 2 esquemes diferents (és el mateix però amb visualització diferent) i un script ```.sql``` per crear les taules
i columnes de tota la BD. Es pot modificar i ajustar l'script, però es considera que la forma en què s'ha fet és la més adient.

### Esquema de Seguretat
#### Rols i Permisos
Donat els diferents treballadors que hi ha a l'hospital, s'ha creat una Matriu de seguretat on apareixen els usuaris/rols i
els diferents permisos que tenen sobre els objectes (dades) de la BD. És per això que, a mode de resum, els rols que existiran a la BD són els següents:

- Metges
- Infermers
- Zeladors
- Administratius
- Pacients
- Conductors d'ambulància

Per veure els permisos detalladament, es recomana consultar la següent documentació de l'Esquema de seguretat:

[Usaris, Grups i Permisos](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/tree/main/Esquema%20de%20seguretat/Matriu%20de%20Seguretat)

A més de veure els permisos que tenen els rols d'usuari i grup de la BD, l'ideal seria crear
un script ```.sql``` per implementar la creació d'usuaris, grups i permisos tot d'una sola vegada, per tal de no anar implementant tants comandaments un per un.

> [!NOTE]  
> El Script ```.sql``` també es troba en el mateix bloc que la documentació de permisos (el enllaç adjuntat), també hi ha una taula en Excel per entendre millor els permisos.

#### SSL-TLS

Primer de tot, cal aclarir una cosa: SSL, avui dia no s'utilitza, ja que el protocol TLS (Transport Layer Security) el va substituir el 1999. A dia d'avui, 12 d'abril de 2024, és l'estàndard en la seva versió TLS 1.3. No obstant això, el terme SSL es continua utilitzant per referir-se a connexions segures.

Un cop els rols i els permisos estiguin creats, cal implementar una encriptació del tràfic de la BD. Per què? Per la senzilla raó que SSL permet xifrar el tràfic de dades, cosa que és molt convenient ja que si les dades no estan xifrades, un intermediari podria interceptar-les (Man in the Middle), i això en una BD d'un hospital és totalment impensable.

Però abans d'aplicar un certificat SSL, s'ha decidit utilitzar un domini amb Cloudfare perquè sigui una mica més segur (s'eviten atacs DDoS) i, a més, la renovació automàtica del certificat serà més fàcil.

> [!NOTE]  
> Cloudfare és el servei que s'està utilitzant en aquest cas, però es poden utilitzar altres opcions que ofereixin el mateix servei.
>  Tot i això, des de la nostra banda es recomana utilitzar aquest servei.

És molt important configurar el firewall on estigui instal·lada la BD, ja que una mala configuració dels ports pot suposar un gran risc en la seguretat del sistema.

#### Generar Certificat

Per generar el certificat SSL-TLS per a la base de dades de l'Hospital es necessita una eina, en aquest cas s'ha decidit utilitzar Certbot. Com que la BD està instal·lada en un Debian en PROMOX, un cop creat i configurat el certificat SSL, caldrà configurar el Postgresql perquè també ho implementi.

Per poder dur a terme tots els passos anteriorment esmentats, es recomana seguir tots els passos de la següent documentació SSL-TLS:

  -  [Configuracio Firewall i SSL](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/tree/main/Esquema%20de%20seguretat/SSL-TLS)

#### Data Masking

Un pas molt important que ajudarà a protegir encara més les dades de la BD és implementar Data Masking als dades de caràcter més important. Però abans d'aplicar Data Masking, cal saber quin tipus de dades es consideren de caràcter personal de grau alt en una base de dades d'un hospital. A continuació es presenten alguns exemples d'això:

- Informació d'Identificació Personal (PII)
- Informació Mèdica Sensible
- Informació Financera
- Informació Laboral i d'Assegurança

Un cop es sap amb quin tipus de dades es treballarà, es recomana fer un estudi per saber a quins dades de la BD s'aplicarà el Data Masking tenint en compte els apartats anteriorment esmentats.

Per poder configurar el Data Masking és necessari instal·lar i configurar una sèrie d'eines, una d'elles és el repositori de GitHub ```pg_anonymize```. Aquest repositori permet aplicar una sèrie de paràmetres i configuracions en PostgreSQL (es pot fer a través de PgAdmin) per poder anonimitzar les dades que es considerin de caràcter personal de grau alt.

Però per realitzar tot això, es recomana seguir els passos que es troben en la següent documentació:

-  [Data Masking](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/blob/main/Esquema%20de%20seguretat/Data_Masking/readme.md)

Amb aquesta documentació es podrà instal·lar les eines necessàries per poder configurar PostgreSQL per aplicar el respectiu Data Masking. A més, explica amb més detall quin tipus de dades de caràcter personal són de grau alt.

#### Legislacio AGPD

Respecte a la legislació de la AGPD, es considera dividir la protecció de dades i documentació en 3 apartats diferents:

- **Requisits Alts:** Es mascararan amb Data Masking dins de la base de dades juntament amb SSL per tenir encriptada la connexió entre el servidor i la BDD. A més, restringirem l'accés a les dades depenent de la teva professió dins de l'hospital.
- **Requisits Intermedis:** Tot i que la informació que contenen els documents és menys rellevant que els anteriors, encara s'han d'encriptar dades personals importants com DNI, telèfons, noms, etc. Utilitzarem Data Masking i el SSL com en l'anterior.
- **Requisits Baixos:** Aquests documents són necessaris i obligatoris, però poc rellevants, per tant tindran poca necessitat d'encriptació. Utilitzarem Data Masking mínimament i la encriptació SSL.

Cal esmentar que l'hospital implementa diferents tècniques per assegurar, protegir i minimitzar l'accés a tot tipus de dades de l'hospital mitjançant mesures de seguretat tècniques, anàlisi de riscos, mesures de seguretat organitzatives, gestió d'accés, protecció de la infraestructura física, revisions i actualitzacions, i per últim en Procediments de Seguretat en Cas d'Incidents.

En el següent apartat adjuntat s'explica molt més detalladament com s'apliquen aquesta sèrie de tècniques i quins tipus de dades es consideren de major o menor importància i molts més detalls.

-  [Legislacio AGPD](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/blob/main/Esquema%20de%20seguretat/Documentacion%20RGPD/Documento%20de%20seguridad.md)

### Bloc de Mantenimient

EEl bloc de manteniment és un apartat per millorar l'anterior apartat de Connectivitat i Login, per a realitzar això es planteja realitzar les següents tasques i implementar-les en l'aplicació:

1. Donar d'alta nou personal al centre (metge/ssa, infermer/a, administratiu/va, neteja…)
2. Donar d'alta nous pacients.
3. Pel personal d'infermeria, saber si depèn d'un metge/ssa o bé és de planta.
4. Per un determinat dia, saber per a cada quiròfan, les operacions que hi ha previstes, el pacient a operar, l'hora, el metge/ssa que les farà i el personal d'infermeria que intervindrà.
5. Per un determinat dia, saber les visites que hi ha planificades, l'hora d'entrada, el metge/ssa i el pacient.
6. Amb PGPLSQL crea dos procediments/funcions/triggers per gestionar/validar la informació que esteu entrant des del manteniment.
7. Donada una habitació cal saber les reserves previstes, mostrant la data ingrés, data prevista de sortida i el pacient que l'ocuparà.
8. Donat un/a pacient saber les visites que ha fet, el diagnòstic, els medicaments que li han receptat, les vegades que ha estat ingressat/da (en cas que ho hagi estat), així com saber les vegades que ha passat pel quiròfan (en cas que l'hagin operat).
9. Donat un/a metge/ssa saber les visites i les operacions que té programades i les seves hores disponibles.
10. Per a cada quiròfan es vol saber quants aparells mèdics té assignat i quina quantitat (per exemple, el quiròfan 1 de la primera planta té assignats 2 respiradors, 2 equips d'oxigen, etc.)

Per poder realitzar aquests apartats, prèviament s'han d'instal·lar les següents llibreries de Python:

  -  ```Pwinput```
  -  ```Psycopg2```
  -  ```Werkzeug.security```
  -  ```Tabulate```: La biblioteca tabulate en Python proporciona una manera convenient de formatar dades tabulars en una varietat d'estils.
  -  ```Dotenv```  : Es una eina útil en el món de Python per gestionar les variables d'entorn d'una manera senzilla i eficaç.

Per aprendre amb més detall com funcionen i com utilitzar aquestes llibreries, es recomana visitar el següent apartat. A més, compta amb les funcions, procediments i triggers juntament amb els codis millorats de l'apartat de Connectivitat i Login per poder-los modificar segons les necessitats.

  -  [Bloc de Mantenimient](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/tree/main/Bloc%20de%20Manteniment)

> [!TIP]
> Encara que aquest apartat encara no conté la versió final de l'aplicació, es recomana fer-ho per evitar confusions.

### Alta disponibilitat

#### Infraestructura Hardware

A causa de les caracteristicas de la Base de dades de l'hospital (quantitat d'informacio emmagatzemada) se ha considerado una quantitat diferent d'opcions i se ha decidido que l'opcion mes adient per a les necessitats de l'hospital és la següent:

Se ha escogido el servidor Dell PowerEdge R740XD2 que te unes caracteristiques de maquinari que s'ha aproximarian al necessari per al bon funcionament del sistema. Se ha utilitzado la pàgina web https://www.renewtech.es/dell-poweredge-r740xd2-configure-to-order.html per a personalitzar el servidor segons les necessitats.

Les caracteristicas aproximades són, una CPU de 12/16 nucleos, 64/128 GB de ram, 50/100 TB de emmagatzament i sobretot que tingui una garantia general en cas de fallada.

Considerem que aquestes especificacions són les mes adients tenint en compte el volum de dades amb el qual es treballés, a mes tenint en compte que l'hospital compta amb recursos limitats no seria molt correcte optar per una solucio mes cara.

> [!NOTE]  
> S'han escollit 2 sistemes d'emmagatzematge perquè, 1 seria per emmagatzemar el sistema operatiu (SSD 2.5) i l'altre per emmagatzemar les dades de la Base de dades (HDD SAS 2.5).
Per a més detalls dels components escollits, la quantitat comprada i els preus, es recomana revisar la següent documentació:
> 
  -  [Hardware Escogido](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/tree/main/Esquema%20d'alta%20disponibilitat/Infraestructura%20Hardware)
    
#### Replicacio 

Per a la replicació de la base de dades es proposa el següent:

Una rèplica entre dos nodes de base de dades (en actiu-actiu o actiu-passiu). A més, s'haurà de crear un diagrama del funcionament de la replicació i un manual de com s'instal·la i s'administra la rèplica entre els dos nodes. S'haurà de poder treballar amb cadascun dels dos nodes i veure com la informació es replica.

Per realitzar la replicació de la BD és necessari seguir els passos de la següent documentació:

  -  [Replicacion BD](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/tree/main/Esquema%20d'alta%20disponibilitat/Replicacio)

#### Backups i restauracio

Se ha decidit crear scripts en Bash per fer còpies de seguretat tant localment com a la núvol, utilitzant el servei d'emmagatzematge OneDrive. A més, s'ha configurat un crontab per executar els scripts corresponents diàriament, i finalment s'ha creat un script per a la restauració de la base de dades de manera més ràpida i senzilla.

Per a l'apartat de Còpies de Seguretat i Restauració s'ha proposat fer el següent:

     1. Backup Complet Inicial: Es realitzarà una còpia de seguretat completa de la base de dades una vegada (manualment o mitjançant un script).
     2. Emmagatzament Local: Es guardaran un total de 5 còpies de seguretat localment, eliminant la més antiga quan s'arribi al límit.
     3. Emmagatzament en el nuvol: Es crearà una còpia de seguretat a la núvol (OneDrive) cada dia que es realitzi una còpia incremental

El procés de còpia de seguretat s'automatitza mitjançant l'eina crontab. S'han creat els seguents scripts:

  -  Script de Backup Lògic pujada a la núvol (copia_local_nube_tarde.sh): Realitza la còpia local i al mateix temps es puja a la núvol, durant el canvi de torn a les 2 PM (OneDrive).
  -  Script de Backup Lògic pujada a la núvol (copia_local_nube_noche.sh): Realitza la còpia local i al mateix temps es puja a la núvol, en horari nocturn 00:00 AM (OneDrive).
  -  Script de restauració (restauracion.sh): Realitza la restauració de la base de dades a través de la còpia més recent existent (còpia lògica).

Per configurar els scripts i el crontab, es recomana seguir pas a pas la següent documentació::

  -  [Backups i Restauracio](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/tree/main/Esquema%20d'alta%20disponibilitat/Backups%20i%20restauracio)

A part de la documentació, es troben els 2 scripts, un per configurar un script de còpia de seguretat a la núvol i local al mateix temps i un altre script per restaurar la còpia més recent realitzada.

### Bloc de consultas 

Per al bloc de consultes es proposa complir amb els següents apartats:

- Donada una planta de l'hospital, saber quantes habitacions, quiròfans i personal d’infermeria té.
- Informe de tot el personal que treballa a l’hospital.
- Informe del nombre de visites ateses per dia.
- Ranking de metges que atenen més pacients.
- Malalties més comunes.

Per trobar els següents apartats realitzats, que són una millora de l'anterior apartat que millorava la "Aplicació", es troben en el següent enllaç:

  -  [Bloc de consultas](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/tree/main/Bloc%20de%20Consultes)

### Dummy Data

Per posar a prova la Base de dades s'ha decidit crear dades fictícies de la següent manera:

Per crear aquestes dades fictícies per validar el rendiment del sistema, es crearan (100.000 visites, 50.000 pacients, 100 metges, 200 infermeres, 100 persones de neteja i 50 persones d'administració), i es crearan els índexos que corresponguin, triant el més adequat per a cada taula. Una petita mostra d'aquesta informació estarà en alfabet ciríl·lic.

La creació de les dades fictícies es podrà executar des de l'aplicació com una opció del menú. També hi haurà una opció per eliminar tota la informació fictícia de la Base de dades.

> [!NOTE]  
> S'ha decidit emmagatzemar els currículums del personal de l'hospital a la base de dades en format PDF.

Per poder implementar el Dummy Data, s'ha d'instal·lar prèviament les següents llibreries de Python:

  -  ```Beautiful Soup```:  Aquesta biblioteca s'utilitza per extreure dades de documents HTML i XML, més concretament per extreure informació d'un HTML que s'ha format com a currículum.
  -  ```PdfKit ```       :  Permet crear i manipular arxius PDF. Pot convertir HTML o text pla a PDF, afegir contingut dinàmic com text i imatges, i controlar l'estil del document.

En el següent enllaç es troba la documentació i els codis per implementar el Dummy Data a la base de dades en PostgreSQL:

  -  [Implementacio Dummy Data](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/tree/main/Dummy_Data)

### Exportacio de Dades
#### Exportar visites XMl

Para la exportacion de datos se ha propuesto, descàrgar de totes les visites que hi ha hagut entre dues dates on figuri un identificador de visita, dia, metge que ha atès i les dades de pacient,
la descàrrega s’ha de fer amb XML y El document ha de gravar-se identat (amb tabulacions).

Para poder realziar el siguiente apartado es neccesario importar las siguientes librerias de ```python``` ( ya vienen integradas):
```
import xml.etree.ElementTree as ET
import xml.dom.minidom
```
Una vez importadas las librerias se recomiendas seguir la documentacion de Exportacion de datos para configurarlo correctamente, ademas en ese apartado se encuentran los codigos fianlizados de exportacion:

  -  [Exportacio de Dades](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/tree/main/Bloc%20d'exportacio%20de%20dades)

#### Informes en PowerBi

Per poder utilitzar Power BI, s'ha d'instal·lar a través de la pàgina web de Microsoft en el següent enllaç:

-  [PowerBi Descarga](https://www.microsoft.com/es-es/download/details.aspx?id=58494)

> [!IMPORTANT]  
> No es recomana instal·lar el programa a través de la botiga de Microsoft perquè pot donar problemes.

Un cop instal·lat, es crea un nou informe i s'obtenen dades d'una altra font, com ara una Base de Dades de PostgreSQL, on s'indica el DNS o la IP del servidor, el nom de la base de dades, el mode de connectivitat de la Base de Dades i una instrucció SQL (opcional) si només volem introduir dades d'una consulta.

Power BI ens permet inserir dades per a informes de 2 maneres:

**Importar**
Importar les dades significa que Power BI pren una còpia de les dades des de la base de dades de PostgreSQL i les emmagatzema en el seu propi model de dades en memòria.

**DirectQuery**
DirectQuery és un mètode en què Power BI no emmagatzema les dades a la seva pròpia memòria. En lloc d'això, envia consultes a la base de dades de PostgreSQL cada vegada que es necessita accedir a les dades.

> [!WARNING]  
> És possible que la configuració normal no funcioni i aparegui l'error
> "Error Certificado Remoto no Vàlid". En cas que succeeixi, es recomana fer el següent:

#### Configuracio Alternativa

En cas que la configuració convencional no funcioni, es pot optar per utilitzar eines de tercers que el mateix Microsoft permet i recomana, una d'aquestes és l'eina ODBC. Aquesta eina actua com a intermediari entre la Base de Dades i el Power BI i permet la connexió sense que aparegui l'error de **Certificado Remot no Vàlid**.

Per a més informació, es recomana revisar la següent documentació, on es troba una explicació pas a pas de com configurar l'ODBC:

  -  [ODBC Alternatiu](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/tree/main/Bloc%20d'exportacio%20de%20dades)

### Manual d'usuari

En el següent enllaç es troba el Manual d'Usuari per poder utilitzar l'aplicació sense cap tipus de dificultat:

  -  [Manual de Usuari](https://github.com/Monotipo18/BBDD_Hospital.guithub.io/blob/main/Login/Connexio%20al%20Programa/GHEN%20User%20Manual.pdf)


## Extra 1: Logs BD

Per motius de seguretat s'ha decidit implementar un sistema de logs a la Base de Dades per saber si els propis treballadors fan consultes de pacients o d'un altre tipus quan no haurien de fer-ho.

Per fer-ho, s'ha de configurar l'arxiu `/etc/postgresql/15/main/postgresql.conf`. Un cop dins, s'ha d'activar `logging_collector` per
activar el col·lector de logs, després `log_directory` i `log_statement`. Les 3 modificacions han de quedar de la següent manera:

```
logging_collector = on
log_directory = 'ruta/del/archivo'
log_statement = 'ddl'
```

> [!CAUTION]
> Projecte realitzat per: Unai, Alex, Victor i Manuel


















 
  


















