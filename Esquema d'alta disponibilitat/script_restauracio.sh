#!/bin/bash

# Datos de acceso al servidor PostgreSQL
USER="postgres"
export PGPASSWORD="unai"
SERVER="192.168.1.137"
DATABASE="hr"

# Ruta donde se encuentran los archivos de respaldo
BACKUP_PATH="/etc/postgresql/15/backup1"

# Encontrar la copia de seguridad más reciente
LATEST_BACKUP=$(ls -t $BACKUP_PATH | head -1)

# Restaurar la copia de seguridad más reciente
psql -h $SERVER -U $USER -d $DATABASE -f "$BACKUP_PATH/$LATEST_BACKUP"

echo "La copia de seguridad más reciente ($LATEST_BACKUP) ha sido restaurada."
