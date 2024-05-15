# Esquema d'alta disponibilitat
<h5><em>LTT have mercy!</em></h5>
## Index
-   [Hardware](#hardware)
-   [Componentes](#componentes)
-   [Precios](#preus)
-   [Precio Total](#preu-total) 

## Hardware

A causa de les caracteristicas de la Base de dades de l'hospital (quantitat d'informacio emmagatzemada) hem considerat una quantitat diferent d'opcions i considerem que l'opcion mes adient per a les necessitats de l'hospital és la següent:

### Servidor

Hem triat el servidor Dell PowerEdge R740XD2 pel fet que hem pogut personalitzar per a unes caracteristiques de maquinari que s'ha aproximarian al necessari per al bon funcionament del sistema. Hem utilitzat la pàgina web https://www.renewtech.es/dell-poweredge-r740xd2-configure-to-order.html per a personalitzar el servidor segons les necessitats.

Les caracteristicas aproximades són, una CPU de 12/16 nucleos, 64/128 GB de ram, 50/100 TB de emmagatzament i sobretot que tingui una garantia general en cas de fallada.

Considerem que aquestes especificacions són les mes adients tenint en compte el volum de dades amb el qual es treballés, a mes tenint en compte que l'hospital compta amb recursos limitats no seria molt correcte optar per una solucio mes cara.

> [!NOTE]  
> Hem triat 2 sistemes d'emmagatzematge perquè, 1 seria per a emmagatzemar el sistema operatiu (SSD 2.5)
> i l'altre per a emmagatzemar les dades de la Base de dades (HDD SAS 2.5)
## Componentes
En la siguiente tabla se encuentra la informacion/caracteristicas de cada componente.

| Componente      | Descripción                                                                         |
|-----------------|-------------------------------------------------------------------------------------|
| Chasis          | DELL - PowerEdge R740XD2 26x3.5 1xPCI MINI MONO                                    |
| CPU             | DELL - Intel Gold 5218 2.30GHz 16C 22M 125W                                         |
| Memoria         | DELL - 64GB 2Rx4 PC4-25600AA-R DDR4-3200MHz                        |
| Raid Controller | DELL - H730P 12Gb/s SAS 2GB Mini Mono R740XD2 C6420                                 |
| Harddrives      | DELL - 2.4TB 10K 2.5 SAS 12G ST2400MM0159 ME4 ME5 SERIES         |
|                 | DELL - 200GB SSD 2.5 SAS 12G WI PX02SSF020                                           |
| Network Card    | DELL - BC5720 1GB 2PORT LP                                                          |
| IDRAC           | DELL - iDRAC Enterprise License                                                     |
| Power Supply    | DELL - PSU 1100W R530 R630 R730 R730 R930 T630 R640 R740              |

## Preus

A mes hem fet una taula amb la quantitat i els preus de cada component.

| Componente        | Cantidad | Precio unitario (€) | Precio total (€) |
|-------------------|----------|---------------------|------------------|
| Chasis            | 1        | 2800,00             | 2800,00          |
| CPU               | 1        | 595,00              | 595,00           |
| Memoria           | 2        | 392,00              | 784,00           |
| Controlador RAID  | 1        | 203,00              | 203,00           |
| Discos Duros      | 26       | 6370,00             | 6370,00          |
| SSD               | 1        | 203,00              | 203,00           |
| Tarjeta de Red    | 1        | 28,00               | 28,00            |
| iDRAC             | 1        | 0,00                | 0,00             |
| Fuente de Alimentación | 2   | 98,00               | 196,00           |

## Preu Total

Per ultim una taula amb el preu total i un descompte aplicat pel venedor

| Detalles          |   Precio total (€) |
|-------------------|--------------------|
| **Total**         |  **10.689,00**    |
| **Descuento HPE (15%)**|  **-1603,35**     |
| **Precio final**  |  **9085,65**      |

> [!IMPORTANT]  
> Com per seguretat hem de replicar la Base de dades en un altre servidor (com a minim)
> de manera Activa-Activa o Activa-Passiva hem de comprar un 2 servidor (si és possible igual)
> pel que el preu total seria el següent:

| Servidor                   | Cantidad | Precio total (€) |
|----------------------------|----------|------------------|
| **Dell PowerEdge R740XD2**| 2        | 21.378,00        |
| **Descuento HPE (15%)**   | 1         | -3.206,70        |

El Cost total dels 2 servidors mes el descompte aplicat per l'empresa ascendeix a : ``` **18.171,3** ``` euros.
