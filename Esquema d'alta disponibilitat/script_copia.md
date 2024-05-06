# Documentación para Backup de Base de Datos

Este documento proporciona instrucciones detalladas sobre cómo realizar backups de la base de datos según las caracteristicas del la base de datos del hospital

## Introducción

Debido a las caracteristicas de la BD del hospital trafico de usuarios y cantidad de informacion almacenado, se ha desarrollado un sistema de backup automatizado para la base de datos. 
Hemos decidido crear scripts en Bash para realizar copias de seguridad tanto en local como en la nube, utilizando el servicio de almacenamiento OneDrive.
Además, se ha configurado un crontab para ejecutar los scripts correspondientes diariamente.

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

1. ** /etc/postgresql/15/backup ** (Almacenamiento de copias de seguridad Locales)
2. ** /home/"usuario"/OneDrive ** (Es la ruta donde se instala y configura por defecto la carpeta OneDrive que se sincroniza en la nube)

## Planificación y Automatización

El proceso de backup se automatiza mediante la herramienta crontab. Se han creado los siguientes scripts:

1. **Script de Backup Logico subida a la nube (copia_local_nube.sh)**: Realiza la copia Local y al mismo tiempo se sube a la nube (OneDrive)
2. **Script de restauracion (restauracion.sh)**: Realiza la restauracion de la base de datos a traves de la copia mas reciente existente ( Copia Logica)

## Script

El script para configurar las copias fisicas Locales y en la nube esta en el siguiente enlace:
- [Script Backup](#Esquema d'alta disponibilitat/script_backup_local_nube.sh)

## Pasos y Permisos

Para poder utilizar el servicio en la nube OneDrive se tiene que seguir
la siguiente documentacion de instalacion, configuracion y uso de OneDrive en este repositiorio de GitHub:

[Documentacion](https://github.com/abraunegg/onedrive).

Una vez instalado y configurado, se le dara permisos a la ruta donde guardan las copias locales
```
chmod 777 /ruta/del/directorio 
```

Despues de darle permisos a la ruta de las copisa Locales , se tendra que dar tambien permisos a la ruta
donde se guardan las copias en la nube
```
chmod 777 /home/"usuario"/OneDrive
```

Una vez dado los permisoa a las 2 rutas se tendra que dar permisoa tanto al script de backup como al de restauracion
```
chmod 777 copia_local_nube.sh 
chmod 777 restauracion.sh
```

## Crontab

Se configuran els siguiente crontab para ejecutar el script diariamente:

```
# Realizar copias de seguridad diarias
0 0 * * * sh /ruta/del/script.sh
```




