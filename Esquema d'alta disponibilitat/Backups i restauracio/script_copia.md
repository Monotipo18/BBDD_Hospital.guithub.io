# Documentación para Backup de Base de Datos

Este documento proporciona instrucciones detalladas sobre cómo realizar backups de la base de datos según las caracteristicas del la base de datos del hospital

## Introducción

Debido a las caracteristicas de la BD del hospital trafico de usuarios y cantidad de informacion almacenado, se ha desarrollado un sistema de backup automatizado para la base de datos. 
Hemos decidido crear scripts en Bash para realizar copias de seguridad tanto en local como en la nube, utilizando el servicio de almacenamiento OneDrive.

Además, se ha configurado un crontab para ejecutar los scripts correspondientes diariamente y por ultimo se ha creado 
un script para realizar la restauracion de la base de datos de maner mas rapida y sencilla.

> [!IMPORTANT]  
> En este caso se realizan 2 copias de seguridad diarias, una en cambio de turno 2 PM y la otra
> a las 12:00 PM , donde el trafico es el mas bajo posible.

## Requisitos del Sistema

- Sistema Operativo: Debian
- Software necesario: Bash y servicio de almacenamiento en la nube (OneDrive).

## Proceso de Backup

El proceso de backup consta de las siguientes etapas:

1. **Backup Completo Inicial**: Se realizará una copia de seguridad completa de la base de datos una vez (de manera manual o a traves de un script)
2. **Almacenamiento Local**: Se guardarán un total de 5 copias de seguridad localmente, eliminando la más antigua cuando se alcance el límite.
3. **Almacenamiento en la Nube**: Se creará una copia de seguridad en la nube (OneDrive) cada día que se realice una copia incremental.

> [!NOTE]  
> Originalmente se habia decidido que se reaizarian copias de seguiridad diferenciales debido a la facilidad
> que se tiene a la hora de restaurar las copias, pero como Postgresql no se pueden realizar copias diferenciales
> se ha tenido que optar por realizar copias logicas.

## Estructura de Directorios

Se ha establecido la siguiente estructura de directorios para almacenar los backups:

1. ** ```/etc/postgresql/15/backup``` ** (Almacenamiento de copias de seguridad Locales)
2. **``` /home/"usuario"/OneDrive``` ** (Es la ruta donde se instala y configura por defecto la carpeta OneDrive que se sincroniza en la nube)

## Planificación y Automatización

El proceso de backup se automatiza mediante la herramienta crontab. Se han creado los siguientes scripts:

1. **Script de Backup Logico subida a la nube ```(copia_local_nube_tarde.sh)**```: Realiza la copia Local y al mismo tiempo se sube a la nube, en cambio de turno 2 PM (OneDrive)
2. **Script de Backup Logico subida a la nube ```(copia_local_nube_noche.sh)**```: Realiza la copia Local y al mismo tiempo se sube a la nube, en horario nocturno 00:00 AM (OneDrive)
3. **Script de restauracion ```(restauracion.sh)**```: Realiza la restauracion de la base de datos a traves de la copia mas reciente existente ( Copia Logica)

## Script

El script para configurar las copias fisicas Locales y en la nube esta en el siguiente enlace:

-  [Script Backup Tarde](Backups%20i%20restauracio/Esquema%20d'alta%20disponibilitat/script_backup_local_nube.sh)
-  [Script Backup Noche](Backups%20i%20restauracio/Esquema%20d'alta%20disponibilitat/script_backup_local_nube.sh)
-  [Script Restauracion](Backups%20i%20restauracio/Esquema%20d'alta%20disponibilitat/script_restauracio.sh)

## Pasos y Permisos

Para poder utilizar el servicio en la nube OneDrive se tiene que seguir
la siguiente documentacion de instalacion, configuracion y uso de OneDrive en este repositiorio de GitHub:

[Instalacion, Configuracion y Uso OneDrive](https://github.com/abraunegg/onedrive).

Una vez instalado y configurado, se le dara permisos a la ruta donde guardan las copias Logicas en Local
```
chmod 777 /ruta/del/directorio 
```

Despues de darle permisos a la ruta de las copias Locales , se tendra que dar tambien permisos a la ruta
donde se guardan las copias en la nube (OneDrive). Donde posteriormente se sincronizara con el script.
```
chmod 777 /home/"usuario"/OneDrive
```

Una vez dado los permisoa a las 2 rutas se tendra que dar permisoa tanto al script de backup que se ejecutara por
la mañana, como al script de la noche y al de restauracion.
```
chmod 777 copia_local_nube_tarde.sh
chmod 777 copia_local_nube_noche.sh 
chmod 777 restauracion.sh
```

## Crontab

Se configuran los siguiente scripts en crontab para que se ejecuten diariamente:

```
# Realizar copias de seguridad diarias
#Copia por la tarde 2PM, cambio de turno
0 14 * * * sh /ruta/del/script.sh
#Copia por la noche 0:00 AM / 12:00 PM
0 0 * * * sh /ruta/del/script.sh
```




