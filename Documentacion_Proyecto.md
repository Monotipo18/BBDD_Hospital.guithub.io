
# PROJECTE PROGRAMACIO Y BASE DE DADES

## Projecte Intermodular


### Contenido

**No se encontraron entradas de tabla de contenido.**

#  **Input Contraseña no visible:**

[[https://pypi.org/project/pwinput/]{.underline}](https://pypi.org/project/pwinput/)

**pip install pwinput**

**{Variable}**=pwinput.pwinput(\"Introduce tu Contraseña: \")

def crearAlumne(codi, nom, cognom, data_naixement):

try:

with open(archivo_csv, \'a\', newline=\'\') as file:

writer = csv.writer(file, delimiter=\';\')

writer.writerow(\[codi, nom, cognom, data_naixement\])

except Exception as e:

print(\"Error al crear alumno:\", e)
