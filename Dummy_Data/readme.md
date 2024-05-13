# PROJECTO PROGRAMACIÓN Y BASE DE DATOS

## Proyecto Intermodular

### Contenido
### Índice
#### Explicación del Código (Inserción de datos)
En nuestra Base de datos decidimos almacenar los currículos del personal del hospital. Por esta razón, nos vimos obligados a utilizar listas.

En el código, encontramos una cantidad considerable de listas, y esto tiene un motivo. Para realizar una creación e inserción masiva de datos, se pueden utilizar bibliotecas como Faker (que es nuestro caso). Sin embargo, surge un problema cuando queremos generar un archivo PDF para crear este currículo.

Intentamos de diferentes maneras la creación del currículo, sin embargo, los datos que generaba eran totalmente aleatorios y no coincidían con los que teníamos dentro de la Base de Datos. Para solucionar este problema, decidimos crear listas. De esta manera, al insertar los datos dentro del currículo, seguirían un patrón de orden junto con la inserción de datos en la BD.

En este trabajo, hemos utilizado nuevas bibliotecas no mencionadas hasta ahora. Estas son:

**Beautiful Soup**, en concreto, hemos importado bs4.
Esta biblioteca se utiliza para extraer datos de documentos HTML y XML, más concretamente para extraer información de un HTML que le hemos dado formato en currículum (archivo.html) que se encuentra en este repositorio.

**PdfKit**
PdfKit es una biblioteca de Python que te permite crear y manipular archivos PDF. Puedes convertir HTML o texto plano a PDF, agregar contenido dinámico como texto e imágenes, y controlar el estilo del documento. Es útil para generar documentos PDF personalizados desde nuestra aplicación. Sigue el patrón del texto y pásalo todo a markdown.

Utlitzan aquetes dues llibreries podem generar 
