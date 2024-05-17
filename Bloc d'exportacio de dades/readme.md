# Bloc d’exportació de dades
## Projecte Intermodular
### Contingut


## Descarregar Visites entre 2 datas
### Conexto
Como el hospital dispone de muchas visitas a lo largo de los dias, meses y años es posible que nos interese poder visiualizar las visitas que han 
habido entre 2 fechas como un informe, por si mas tarde se requiere enviar el informe a otro hospital o otros sitios que se requieran.
Es por eso que lo idea es guardar los datos en formato Xml para que el traspaso de datos sea mas sencillo.

Para poder guardar la informacion en Xml y que esten indentados es necessario utilizar la libreria integrada/estandart de pyhton ```xml.etree.ElementTree``` y tambien ```xml.dom.minidom ```.

```xml.etree.ElementTree``` es una librería en Python que nos permite trabajar con archivos XML de manera simple y rápida, algunas funciones son:

  -  **Leer XML**: Abrir y lee archivos XML para que se puedan trabajar desde Python.
  -  **Modificar XML**: Cambia el contenido del XML, añade o elimina contenido.
  -  **Guardar XML**: Escribir los cambios en un archivo XML nuevo o que ya exista.

```xml.dom.minidom```  es otra librería en Python que también trabaja con XML pero de una manera más detallada, sirve para:
  -  **Formatear XML**: Hace que el XML sea más fácil de leer.
  -  **Control detallado**: Te permite manipular el XML con más precisión.
La libreria se implementa de la siguiente manera:
```
import xml.etree.ElementTree as ET
```
Y tambien :
```
import xml.dom.minidom
```
