# Bloc d’exportació de dades
## Projecte Intermodular
### Contingut


## Descarregar Visites entre 2 datas
### Conexto
Como el hospital dispone de muchas visitas a lo largo de los dias, meses y años es posible que nos interese poder visiualizar las visitas que han 
habido entre 2 fechas como un informe, por si mas tarde se requiere enviar el informe a otro hospital o otros sitios que se requieran.
Es por eso que lo idea es guardar los datos en formato Xml para que el traspaso de datos sea mas sencillo.

### Que es xml.etree.ElementTree y xml.dom.minidom 

Para poder guardar la informacion en Xml y que esten indentados es necessario utilizar la libreria integrada/estandart de pyhton ```xml.etree.ElementTree``` y tambien ```xml.dom.minidom ```.

```xml.etree.ElementTree``` es una librería en Python que nos permite trabajar con archivos XML de manera simple y rápida, algunas funciones son:

  -  **Leer XML**: Abrir y lee archivos XML para que se puedan trabajar desde Python.
  -  **Modificar XML**: Cambia el contenido del XML, añade o elimina contenido.
  -  **Guardar XML**: Escribir los cambios en un archivo XML nuevo o que ya exista.

```xml.dom.minidom```  es otra librería en Python que también trabaja con XML pero de una manera más detallada, sirve para:
  -  **Formatear XML**: Hace que el XML sea más fácil de leer.
  -  **Control detallado**: Te permite manipular el XML con más precisión.
Las 2 librerias se implementan de la siguiente manera:
```
import xml.etree.ElementTree as ET
import xml.dom.minidom
```
### Funcionamiento

Para empezar todo documento Xml ha de tener el elemento raiz, en este caso deberia ser:
```
root = ET.Element("visitas")
```
Despues de crear el elemento raiz es neccesario crear subelementos raiz ( en este caso 1, que se repetira tantas veces como sea necesario)
  -   Propósito: Añadir un subelemento bajo el elemento raíz "visitas" para cada visita.
  -   Qué hace: Crea un nuevo elemento XML llamado "visita" como hijo del elemento raíz "visitas". Este elemento representará una visita específica.
```
visita = ET.SubElement(root, "visita")
```
Añadir subelementos con datos específicos de la visita
  -  Propósito: Añadir detalles específicos de cada visita como subelementos del elemento "visita".
  -  Qué hace: Para cada dato crea un subelemento dentro de"visita" con el nombre correspondiente.
```
ET.SubElement(visita, "ID").text = str(resultado[0])
ET.SubElement(visita, "Fecha").text = resultado[1].strftime("%Y-%m-%d")
ET.SubElement(visita, "NomMetge").text = resultado[2]
ET.SubElement(visita, "PrimerCognomMetge").text = resultado[3]
ET.SubElement(visita, "NomPacient").text = resultado[4]
ET.SubElement(visita, "PrimerCognomPacient").text = resultado[5]
```
Crear el árbol XML y guardarlo en un archivo

  -  Propósito: Guardar el contenido del árbol XML en un archivo.
  -  Qué hace: Crea un objeto ElementTree a partir del elemento raíz root , escribe el árbol XML en un archivo con el nombre especificado por nombre_archivo.
     El archivo se guarda con codificación UTF-8 e incluye una declaración XML (<?xml version='1.0' encoding='utf-8'?>).
```
xml_tree = ET.ElementTree(root)
xml_tree.write(f"{nombre_archivo}.xml", encoding="utf-8", xml_declaration=True)
```
Formatear el XML para que esté bien indentado y tabulado

  -  Propósito: Formatear el archivo XML para que sea más legible, con indentación y nuevas líneas.
  -  Qué hace: Usa minidom para parsear el archivo XML que se acaba de escribir.
     oprettyxml() convierte el XML en una cadena de texto con una bonita indentación.
     Abre el archivo XML nuevamente en modo escritura ("w") y escribe la cadena de texto formateada, reemplazando el contenido anterior.
```
dom = xml.dom.minidom.parse(f"{nombre_archivo}.xml")
with open(f"{nombre_archivo}.xml", "w", encoding="utf-8") as file:
    file.write(dom.toprettyxml())
```
## Resumen

  -  1.Crea la estructura del XML: Elementos "visitas" y "visita", y añade subelementos con detalles específicos.
  -  2.Guarda el XML: Escribe el árbol XML en un archivo con codificación UTF-8.
  -  3.Formatea el XML: Usa minidom para agregar indentación y hacer que el XML sea más legible.

### Que es random.sampele

La función sample se utiliza para obtener una lista de elementos seleccionados aleatoriamente de una secuencia (como una lista, tupla, o cadena). 
La función no modifica la secuencia original y no permite duplicados, es decir, cada elemento seleccionado es único.

### Funcionamiento

En el siguiente codigo podemos ver una funcion que hace uso de ```sample``` :
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
Como vemos la funcion de sample se utiliza en este trozo de codigo:
```
    # Llamamos la función sample() utilizando la secuencia, y la longitud
    password_union = sample(secuencia, longitud)
```
  -  Propósito: Seleccionar una muestra aleatoria de longitud caracteres únicos de la cadena secuencia.
  -  Qué hace: sample(secuencia, longitud) devuelve una lista de longitud caracteres elegidos aleatoriamente de secuencia. Cada carácter en la lista es único y la selección se hace sin reemplazo.
     Por ejemplo, si longitud es 8, sample podría devolver una lista como ['a', 'G', '1', 'b', 'Z', '3', 'x', '5'].











