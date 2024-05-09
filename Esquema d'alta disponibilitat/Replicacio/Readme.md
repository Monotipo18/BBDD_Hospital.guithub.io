# Replicacio
## Projecte Intermodular
## Index


Añadir el repositorio PostgreSQL al sistema
```
dnf install -y [https://download.postgresql.org/pub/r...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbEhHdHV3dllrN0lfbFJTVVVvc25KcEU0VXhWd3xBQ3Jtc0tselBvRG5VZVNmTVBjN1h0Sk1DRDJmVzNOa2NkZnpTVXJqT3ZJcFdBMlF0YnZfU1VnOG5vTXQ5V0tndWQzZ0VYeHZDY2JsaEVmT2g1SXhHLUxQU0JteklSZkpEVDRJOXpVT2FQMDl0dlB2U1dmWVZnMA&q=https%3A%2F%2Fdownload.postgresql.org%2Fpub%2Frepos%2Fyum%2Freporpms%2FEL-9-x86_64%2Fpgdg-redhat-repo-latest.noarch.rpm&v=GIsD1BgFnWc)
```

Desactivar el módulo PostgreSQL integrado
```
sudo dnf -qy module disable postgresql
```

Instalar PostgreSQL 15 tanto el servidor primario como en el secundario.
```
dnf install -y postgresql15-server postgresql15
```

Inicializar la base de datos
```
/usr/pgsql-15/bin/postgresql-15-setup initdb
```

Iniciar el servicio PostgreSQL y habilitarlo para que se inicie automáticamente al arrancar.
```
systemctl enable --now postgresql-15
```

Editar el archivo de configuración de PostgreSQL en el servidor primario para permitir la replicación.
```
vi /var/lib/pgsql/15/data/postgresql.conf
```
```
listen_addresses = '*'
wal_level = replica
max_wal_senders = 10
wal_keep_segments = 8
hot_standby = on
```

Guardar los cambios en el archivo y salir.

Ahora se crea un usuario de replicación en el servidor primario.
```
sudo su - postgres
psql
CREATE USER replicator REPLICATION LOGIN ENCRYPTED PASSWORD 'replicator_password';
\q
```

Añadir una regla en el archivo de autenticación basada en host
```
vi /var/lib/pgsql/15/data/pg_hba.conf
host    replication     replicator      192.168.100.75/32       trust
```

Ahora se guarda y se sale
```
restart the PostgreSQL service
systemctl restart postgresql-15
```

Firewall

Añada una nueva regla al cortafuegos de los servidores primario y secundario
```
firewall-cmd --zone=public --add-port=5432/tcp --permanent
firewall-cmd --reload
```

Ahora que se ha creado el usuario de replicación y configurado el servidor primario, se puede pasar a configurar el servidor secundario.

Cambia como usuario postgres y ejecute el comando ```pg_basebackup```.
```
sudo su - postgres
pg_basebackup -h 192.168.100.72 -U replicator -Fp -Xs -P -R -D /var/lib/pgsql/15/data/
```

Ejecuta el comando ```systemctl`` para iniciar y habilitar en el arranque el servicio PostgreSQL en el servidor secundario.
```
systemctl enable --now postgresql-15
```

En este punto, se ha configurado el servidor secundario y activado la replicación asíncronizada.

Verficicacion

Para probar la configuración de la replicación, se insertan algunos datos en la base de datos primaria y luego se comprueba que aparecen en el servidor secundario.
```
su - postgres
psql -c "CREATE TABLE test1 (id serial PRIMARY KEY, data text);"
psql -c "INSERT INTO test (data) VALUES ('test data');"
psql -c "SELECT * FROM test;"
```

Si la replicación funciona correctamente, la sentencia SELECT debería devolver la fila insertada tanto en el servidor primario como en el secundario.

Se Pueden hacer pruebas adicionales realizando una acción **'WRITE'** desde el servidor **'SLAVE'**.
```
psql -c "CREATE TABLE test1 (id serial PRIMARY KEY, data text);"
```
El resultado debería ser ```'No se puede ejecutar CREATE TABLE'``` como se muestra aquí.

Para verificar el estado de streaming de un servidor secundario.
```
psql -x -c "SELECT * FROM pg_stat_replication;"
```

Para ver el estado del proceso receptor de WAL en un servidor secundario en PostgreSQL, se puede utilizar este comando:
```
psql -x -c "select * from pg_stat_wal_receiver;"
```

Conmutación por error

Para realizar una conmutación por error de un servidor PostgreSQL primario a un servidor secundario, es necesario promover el servidor secundario ejecutando el comando pg_ctl promote como usuario postgres.

El comando ``pg_ctl`` promote se utiliza para iniciar el proceso de conmutación por error. Indica al servidor en espera que se convierta en el nuevo servidor primario y comience a aceptar conexiones de lectura-escritura.

Para activar las sugerencias de registro de **WAL**, puede establecer el parámetro en el archivo ```postgresql.conf```.
```
vi /var/lib/pgsql/15/data/postgresql.conf
wal_log_hints = on
```

**SECONDARY**
En el servidor secundario, se comprueba que sigue en estado de sólo lectura ejecutando el siguiente comando.
```
psql -c "SELECT pg_is_in_recovery();"

/usr/pgsql-15/bin/pg_ctl promote
```
