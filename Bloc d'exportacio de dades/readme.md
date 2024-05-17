# Bloc d’exportació de dades
## Projecte Intermodular
### Contingut

## Exportar Visites entre 2 dates
### Context
Com que l'hospital disposa de moltes visites al llarg dels dies, mesos i anys, és possible que ens interessi poder visualitzar les visites que hi ha hagut entre 2 dates com un informe, per si més tard es requereix enviar l'informe a un altre hospital o altres llocs que es requereixin. És per això que la idea és guardar les dades en format XML perquè el traspàs de dades sigui més senzill.

### Què és xml.etree.ElementTree i xml.dom.minidom

Per poder guardar la informació en XML i que estiguin indentats és necessari utilitzar la llibreria integrada/estàndard de Python ```xml.etree.ElementTree``` i també ```xml.dom.minidom```.

```xml.etree.ElementTree``` és una llibreria en Python que ens permet treballar amb fitxers XML de manera simple i ràpida, algunes funcions són:

  -  **Llegir XML**: Obrir i llegir fitxers XML per tal que es puguin treballar des de Python.
  -  **Modificar XML**: Canvia el contingut de l'XML, afegeix o elimina contingut.
  -  **Guardar XML**: Escriure els canvis en un fitxer XML nou o que ja existeixi.

```xml.dom.minidom``` és una altra llibreria en Python que també treballa amb XML però d'una manera més detallada, serveix per:
  -  **Formatejar XML**: Fa que l'XML sigui més fàcil de llegir.
  -  **Control detallat**: Et permet manipular l'XML amb més precisió.

Les dues llibreries s'implementen de la següent manera:

```
import xml.etree.ElementTree as ET
import xml.dom.minidom
```
### Funcionament

Per començar, tot document XML ha de tenir l'element arrel, en aquest cas hauria de ser:
```
root = ET.Element("visitas")
```
Després de crear l'element arrel és necessari crear subelements arrel (en aquest cas 1, que es repetirà tantes vegades com sigui necessari)
  -  **Propòsit**: Afegir un subelement sota l'element arrel "visites" per a cada visita.
  -  **Què fa**: Crea un nou element XML anomenat "visita" com a fill de l'element arrel "visites". Aquest element representarà una visita específica.
```
visita = ET.SubElement(root, "visita")
```
Afegir subelements amb dades específiques de la visita
  -  **Propòsit**: Afegir detalls específics de cada visita com subelements de l'element "visita".
  -  **Què fa**: Per a cada dada crea un subelement dins de "visita" amb el nom corresponent.
```
ET.SubElement(visita, "ID").text = str(resultado[0])
ET.SubElement(visita, "Fecha").text = resultado[1].strftime("%Y-%m-%d")
ET.SubElement(visita, "NomMetge").text = resultado[2]
ET.SubElement(visita, "PrimerCognomMetge").text = resultado[3]
ET.SubElement(visita, "NomPacient").text = resultado[4]
ET.SubElement(visita, "PrimerCognomPacient").text = resultado[5]
```
Crear l'arbre XML i guardar-lo en un fitxer

  -  **Propòsit**: Guardar el contingut de l'arbre XML en un fitxer.
  -  **Què fa**: Crea un objecte ElementTree a partir de l'element arrel `root`, escriu l'arbre XML en un fitxer amb el nom especificat per `nom_fitxer`.
     El fitxer es guarda amb codificació UTF-8 i inclou una declaració XML (`<?xml version='1.0' encoding='utf-8'?>`).
```
xml_tree = ET.ElementTree(root)
xml_tree.write(f"{nombre_archivo}.xml", encoding="utf-8", xml_declaration=True)
```
Formatejar l'XML perquè estigui ben indentat i tabulat

  -  **Propòsit**: Formatejar el fitxer XML perquè sigui més llegible, amb indentació i noves línies.
  -  **Què fa**: Utilitza `minidom` per parsejar el fitxer XML que s'acaba d'escriure.
     `toprettyxml()` converteix l'XML en una cadena de text amb una bonica indentació.
     Obre el fitxer XML novament en mode escriptura ("w") i escriu la cadena de text formatejada, reemplaçant el contingut anterior.
```
dom = xml.dom.minidom.parse(f"{nombre_archivo}.xml")
with open(f"{nombre_archivo}.xml", "w", encoding="utf-8") as file:
    file.write(dom.toprettyxml())
```
## Resum

  -  1. Crea l'estructura de l'XML: Elements "visites" i "visita", i afegeix subelements amb detalls específics.
  -  2. Guarda l'XML: Escriu l'arbre XML en un fitxer amb codificació UTF-8.
  -  3. Formateja l'XML: Utilitza `minidom` per afegir indentació i fer que l'XML sigui més llegible.

### Què és random.sample

La funció `sample` s'utilitza per obtenir una llista d'elements seleccionats aleatòriament d'una seqüència (com una llista, tupla o cadena).
La funció no modifica la seqüència original i no permet duplicats, és a dir, cada element seleccionat és únic.

### Funcionamient

En el següent codi podem veure una funció que fa servir ```sample``` :
```
def Generar_Nombre(longitud):
  
    # Definimos los caracteres y simbolos
    
    abc_minusculas = "abcdefghijklmnopqrstuvwxyz"
    
    # HACK: upper() transforma las letras de una cadena en mayusculas
    abc_mayusculas = abc_minusculas.upper() 
    
    numeros = "0123456789"

    
    # Definimos la secuencia
    secuencia = abc_minusculas + abc_mayusculas + numeros 
    
    # Llamamos la función sample() utilizando la secuencia, y la longitud
    password_union = sample(secuencia, longitud)
    
    # Con join insertamos los elementos de una lista en una cadena
    password_result = "".join(password_union)
    
    # Retornamos la variables "password_result"
    return password_result
```
Com veiem, la funció `sample` s'utilitza en aquest tros de codi:
```
    # Llamamos la función sample() utilizando la secuencia, y la longitud
    password_union = sample(secuencia, longitud)
```
  -  **Propòsit**: Seleccionar una mostra aleatòria de longitud caràcters únics de la cadena seqüència.
  -  **Què fa**: `sample(seqüència, longitud)` retorna una llista de longitud caràcters triats aleatòriament de seqüència. Cada caràcter a la llista és únic i la selecció es fa sense reemplaçament.
     Per exemple, si longitud és 8, `sample` podria retornar una llista com ['a', 'G', '1', 'b', 'Z', '3', 'x', '5'].

# Informes en PowerBi
## Instal·lació

Per instal·lar l'eina PowerBi es recomana instal·lar el Setup a través de la pàgina web [https://www.microsoft.com/es-es/download/details.aspx?id=58494](https://www.microsoft.com/es-es/download/details.aspx?id=58494), la versió que es troba a la Microsoft Store dóna alguns problemes.

## Configuració

Un cop instal·lat es crea un nou informe i s'obté dades d'una altra font, i que sigui a través de Base de Dades de PostgreSQL, on s'indica Dns o Ip del servidor, nom de la base de dades, Mode connectivitat de Base de dades i Instrucció SQL (opcional) si només volem introduir dades d'una consulta.

### Mode de Connectivitat de Dades

#### Importar

Importar les dades significa que Power BI pren una còpia de les dades des de la base de dades de PostgreSQL i les emmagatzema en el seu propi model de dades en memòria.

  -  **Rendiment**: Un cop les dades estan importades, les consultes i visualitzacions a Power BI són molt ràpides perquè les dades es troben a la memòria del model de dades de Power BI.
  -  **Actualització de dades**: Has de programar les actualitzacions de dades per mantenir la informació actualitzada. Això es fa mitjançant "refresh" programats, que tornen a importar les dades des de la BD.
  -  **Capacitat**: Estàs limitat per la capacitat d'emmagatzematge de Power BI. Si treballes amb conjunts de dades molt grans, podries enfrontar-te a problemes de capacitat.

#### DirectQuery

DirectQuery és un mètode en què Power BI no emmagatzema les dades a la seva pròpia memòria. En lloc d'això, envia consultes a la base de dades de PostgreSQL cada vegada que es necessita accedir a les dades.

  -  **Rendiment**: Les consultes poden ser més lentes perquè cada interacció amb les dades requereix una consulta a la base de dades. El rendiment depèn en gran mesura del rendiment de la base de dades d'origen                      i de la xarxa.
  -  **Actualització de dades**: Les dades sempre estan actualitzades perquè Power BI consulta la base de dades en temps real.
  -  **Capacitat**: No hi ha límits significatius en la quantitat de dades que es poden gestionar, ja que les dades no s'emmagatzemen a Power BI.
  -  **Seguretat**: Les polítiques de seguretat de la base de dades s'apliquen directament, la qual cosa pot ser una avantatge per a certes situacions de seguretat.

## Configuració Alternativa

Degut a que a l'hora d'intentar connectar a la Base de dades, pot donar Error de Certificat Remot (SSL) es pot optar per fer la connexió mitjançant un intermediari (eina de tercers), dins de les diferents eines es pot utilitzar ODBC.

### Instal·lació

Per instal·lar les eines de tercers ODBC s'ha d'instal·lar a través de la pàgina oficial de PostgreSQL: [https://www.postgresql.org/ftp/odbc/releases/REL-16_00_0004/](https://www.postgresql.org/ftp/odbc/releases/REL-16_00_0004/)

### Configuració

Un cop instal·lat es haurà d'executar l'ODBC (Administrador d'Origen de Dades ODBC de 64 bits) i fer el següent:


     1. Agregar...
     2. Postgresql Unicode(x64)
     3. Introduir: Nom BD, Servidor, Nom d'usuari, Mode SSL, Por, Contrasenya
     4. Guardar configuracio
     
Un cop guardada la configuració, s'accedeix a PowerBi i es segueixen els mateixos passos però s'ha de seleccionar l'opció ODBC. 
S'introdueixen les credencials i s'han de seleccionar les taules que es volen importar.


    





