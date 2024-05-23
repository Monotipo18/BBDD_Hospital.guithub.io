# PROJECTE PROGRAMACIÓ I BASE DE DADES

## Projecte internodular

### Contingut
### Índex
#### Explicació del Codi (Inserció de dades)
En la nostra Base de dades decidim emmagatzemar els currículums del personal de l'hospital. Per aquesta raó, ens vam veure obligats a utilitzar llistes.

En el codi, trobem una quantitat considerable de llistes, i això té un motiu. Per a realitzar una creació i inserció massiva de dades, es poden utilitzar biblioteques com Faker (que és el nostre cas). No obstant això, sorgeix un problema quan volem generar un arxiu PDF per a crear aquest currículum.

Intentem de diferents maneres la creació del currículum, tanmateix, les dades que generava eren totalment aleatoris i no coincidien amb els que teníem dins de la Base de dades. Per a solucionar aquest problema, decidim crear llistes. D'aquesta manera, en inserir les dades dins del currículum, seguirien un patró d'ordre juntament amb la inserció de dades en la BD.

En aquest treball, hem utilitzat noves biblioteques no esmentades fins ara. Aquestes són:

**Beautiful Soup**, en concret, hem importat bs4.
Aquesta biblioteca s'utilitza per a extreure dades de documents HTML i XML, més concretament per a extreure informació d'un HTML que li hem donat format en currículum (arxiu.HTML) que es troba en aquest repositori.

**PdfKit**
PdfKit és una biblioteca de Python que et permet crear i manipular arxius PDF. Pots convertir HTML o text pla a PDF, agregar contingut dinàmic com a text i imatges, i controlar l'estil del document. És útil per a generar documents PDF personalitzats des de la nostra aplicació. Segueix el patró del text i passa'l tot a markdown.

Utilitzen aquestes dues llibreries podem generar els currículums en format PDF
