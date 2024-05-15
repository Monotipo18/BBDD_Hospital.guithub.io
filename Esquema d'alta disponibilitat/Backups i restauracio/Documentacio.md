# Documentación para Backup de Base de Datos
<h5><em>Always cover your back!</em></h5>
Aquest document proporciona instruccions detallades sobre com fer còpies de seguretat de la base de dades segons les característiques de la base de dades de l'hospital.

## Introducció

Degut a les característiques de la BD de l'hospital, el tràfic d'usuaris i la quantitat d'informació emmagatzemada, s'ha desenvolupat un sistema de còpies de seguretat automatitzades per a la base de dades.

Hem decidit crear scripts en Bash per fer còpies de seguretat tant localment com a la núvol, utilitzant el servei d'emmagatzematge OneDrive.
A més, s'ha configurat un crontab per executar els scripts corresponents diàriament, i finalment s'ha creat un script per a la restauració de la base de dades de manera més ràpida i senzilla.

> [!IMPORTANT]  
> En aquest cas, es realitzen 2 còpies de seguretat diàries. Una es fa durant el canvi de torn a les 2 PM,
>  i l'altra a les 12:00 PM, quan el trànsit és el més baix possible.

## Requisits del Sistema

- Sistema Operatiu: Debian
- Software necesari: Bash y servei d'enmmagetzament en el nuvol (OneDrive).

## Proces de Backup

El procés de còpia de seguretat consta de les següents etapes:

1. **Backup Complet Inicial**: Es realitzarà una còpia de seguretat completa de la base de dades una vegada (manualment o mitjançant un script).
2. **Emmagatzament Local**: Es guardaran un total de 5 còpies de seguretat localment, eliminant la més antiga quan s'arribi al límit.
3. **Emmagatzament en el nuvol**: Es crearà una còpia de seguretat a la núvol (OneDrive) cada dia que es realitzi una còpia incremental.

> [!NOTE]  
> Originalment s'havia decidit fer còpies de seguretat diferencials,
> però Postgresql no ho permet, així que es va optar per les còpies lògiques.


## Estructura de Directoris

S'ha establert la següent estructura de directoris per emmagatzemar les còpies de seguretat:

1. ** ```/etc/postgresql/15/backup``` ** (Emmagatzematge de còpies de seguretat locals)
2. **``` /home/"usuari"/OneDrive``` ** (És la ruta on s'instal·la i configura per defecte la carpeta OneDrive que es sincronitza a la núvol)

## Planificació y Automatitzacio

El procés de còpia de seguretat s'automatitza mitjançant l'eina crontab. S'han creat els seguents scripts:

1. **Script de Backup Lògic pujada a la núvol** ```(copia_local_nube_tarde.sh)```: Realitza la còpia local i al mateix temps es puja a la núvol, durant el canvi de torn a les 2 PM (OneDrive).
2. **Script de Backup Lògic pujada a la núvol** ```(copia_local_nube_noche.sh)```: Realitza la còpia local i al mateix temps es puja a la núvol, en horari nocturn 00:00 AM (OneDrive).
3. **Script de restauració** ```(restauracion.sh)```: Realitza la restauració de la base de dades a través de la còpia més recent existent (còpia lògica).

## Script

El script per configurar les còpies físiques locals i a la núvol es troba en el següent enllaç:

- [Script Backup Tarde](Esquema%20d'alta%20disponibilitat/Backups%20i%20restauracio/script_backup_local_nube.sh)
- [Script Backup de Nit](Esquema%20d'alta%20disponibilitat/Backups%20i%20restauracio/script_backup_local_nube.sh)
- [Script Restauració](Esquema%20d'alta%20disponibilitat/Backups%20i%20restauracio/script_restauracio.sh)

## Pasos i Permisos

Per poder utilitzar el servei a la núvol OneDrive, cal seguir la següent
documentació d'instal·lació, configuració i ús de OneDrive en aquest repositori de GitHub:

[Instalacio, Configuracio y Us de OneDrive](https://github.com/abraunegg/onedrive).

Un cop instal·lat i configurat, se li donaran permisos a la ruta on es guarden les còpies lògiques en local:

```
chmod 777 /ruta/del/directori
```

Després de donar permisos a la ruta de les còpies locals, també s'hauran de donar 
permisos a la ruta on es guarden les còpies a la núvol (OneDrive), on posteriorment es sincronitzaran amb l'script.

```
chmod 777 /home/"usuari"/OneDrive
```

Un cop donats els permisos a les dues rutes, també s'hauran de donar permisos tant als scripts de còpia de seguretat que s'executaran per la matinada com als scripts de la nit i de restauració.

```
chmod 777 copia_local_nube_tarda.sh
chmod 777 copia_local_nube_nit.sh 
chmod 777 restauracio.sh
```

## Crontab

Es configuraran els seguents scripts en crontab perque se executin diariament:

```
# Realizar copias de seguridad diarias
#Copia por la tarde 2PM, cambio de turno
0 14 * * * sh /ruta/del/script.sh
#Copia por la noche 0:00 AM / 12:00 PM
0 0 * * * sh /ruta/del/script.sh
```




