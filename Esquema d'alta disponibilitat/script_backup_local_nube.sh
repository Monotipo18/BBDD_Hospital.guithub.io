#!/bin/bash

# Datos de acceso al servidor PostgreSQL
USER="postgres"
export PGPASSWORD="unai"
SERVER="192.168.1.137"
DATABASE="hr"

# Ruta donde guardaremos los archivos de respaldo
BACKUP_PATH="/etc/postgresql/15/backup1"
DATE=$(date +"%d-%b-%Y")

# Creamos el directorio de respaldo si no existe
mkdir -p $BACKUP_PATH

# Realizamos la copia de seguridad de la base de datos específica
pg_dump -h $SERVER -U $USER $DATABASE > $BACKUP_PATH/$DATABASE-$DATE.sql


ONEDRIVE_DIR="/home/unai/OneDrive/CopiasBD"

# Nombre del archivo de copia de seguridad
BACKUP_FILE="$DATABASE-$DATE.sql"

# Mantener solo las últimas 5 copias de seguridad locales
cd $BACKUP_PATH 
ls -t | tail -n +6 | xargs rm -f

# Copiar el respaldo local al directorio de OneDrive
cp "$BACKUP_PATH/$BACKUP_FILE" "$ONEDRIVE_DIR/$DATE.sql"

# Sincronizar con OneDrive

onedrive --synchronize --upload-only
