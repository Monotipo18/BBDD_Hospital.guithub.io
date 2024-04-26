# Esquema d'alta disponibilitat
-   [Hardware](#hardware)
## Hardware

Debido a las caracteristicas de la Base de Datos del hospital (cantidad de informacion almacenada) hemos considerado una cantidad distinta de opciones y consideramos que la opcion mas adiente para las necesidades del hospital es la siguiente:

### Servidor

Hemos escogido el servidor Dell PowerEdge R740XD2 debido a que hemos podido personalizar para unas caracteristicas de hardware que se aproximarian a lo necesario para el buen funcionamiento del sistema.

Las caracteristicas aproximades eran, una CPU de 12/16 nucleos, 64/128 GB de ram, 50/100 TB de almencamiento y sobretodo que tenga una garantia general en caso de fallada.

> [!NOTE]  
> Hemos escogido 2 sistema de almacenamiento porque, 1 sera para almacenar el sistema operativo (SSD 2.5)
> y el otro para almacenar los datos de la Base de Datos (HDD SAS 2.5)

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

Aparte hemos hecho una tabla con la cantidad y los precios de cada componente.

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

Por ultimo una tabla con el precio total y un descuento aplicado por el vendedor

| Detalles          |   Precio total (€) |
|-------------------|--------------------|
| **Total**         |  **10.689,00**    |
| **Descuento HPE (15%)**|  **-1603,35**     |
| **Precio final**  |  **9085,65**      |

> [!IMPORTANT]  
> Como por seguridad hemos de replicar la Base de datos en otro servidor (como minimo)
> de manera Activa-Activa o Activa-Passiva hemos de comprar un 2 servidor (si es posible igual)
> por lo que el precio total sera el siguiente:

| Servidor                   | Cantidad | Precio total (€) |
|----------------------------|----------|------------------|
| **Dell PowerEdge R740XD2**| 2        | 21.378,00        |
| **Descuento HPE (15%)**   | 2         | -3.206,70        |
