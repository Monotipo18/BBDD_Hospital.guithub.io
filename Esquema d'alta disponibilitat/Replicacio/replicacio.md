<h1>Replicació</h1>
<h5><em>The more the Better!</em></h5>
<p>Primer volia explicar una mica que és la replicació, la replicació consisteix a fer còpies de la BBDD, en aquest cas, per a assegurar que en cas que caigui una còpia, puguis continuar accedint la BBDD, cada còpia se li sol dir NODE, per a fer una replicació necessitem mínim dos NODES i si pot ser que estiguin els més lluny possible, també hi ha uns quants tipus de replicació si vols veure més pots veure'ls en la pàgina oficial de postgres, en el nostre cas és Rèplica.</p>

<p>Òbviament, necessitarem mínim dues màquines amb postgres, en el nostre cas és la versió 15, que les dues màquines es poden comunicar entre elles i paciència.</p>


<h3>Configuracio del servidor primari</h3>

<p>Primer entrarem en la configuracion de postgres</p>

```bash
sudo nano /etc/postgresql/15/main/postgresql.conf
```
<p>I canviem les següents línies perquè quedin com l'exemple:</p>

```bash
listen_addresses = '*'
wal_level = replica
max_wal_senders = 2
wal_keep_size = 1GB

```

<p>Ara ens anem a pg_hba.conf</p>

```bash
sudo nano /etc/postgresql/15/main/pg_hba.conf
```

<p>I al final de tot posem el següent:</p>

```bash	
host replication replicator [IPServidor.Secundari]/[Mascara-IP] scram-sha-256
```

<h3>Crea un usuari replicació (node principal)</h3>
<p>Se pot fer de moltes maneras aqui com hem fet:</p>

```bash	
sudo -u postgres psql
```

<p>Si us plau! Canvia la contrasenya a una cosa supersegura!</p>

```sql
CREATE USER replicator REPLICATION 
LOGIN CONNECTION LIMIT 3 ENCRYPTED 
PASSWORD 'c0ntr4s3gur4!';
```

<p>Recorda reiniciar el servei de postgres!</p>

```bash	
systemctl restart postgresql
```

<p>Configurar el segon node</p>
<p>Parem el postgre, y fem un pg_basebackup, recomano elimina o guarda en una altralloc la carpeta</p>

```bash	
pg_basebackup -h [IP.Servidor.Secunadri] -U replicator -Fp -Xs -P -R -D /var/lib/pgsql/15/data/
```

<p>Ens anem a l'arxiu de configuració del postgres i a dalt de tot posem això:</p>

```bash	
hot_standby = on
primary_conninfo = 'host=[FIRST_SERVER_IP] port=5432 user=replicator password=[YOUR_PASSWORD] sslmode=prefer'
primary_slot_name = 'standby_slot'
```

<p>Tornem a encendre el postgres i ja el tindríem</p>

<h3>Exemple de funcionalitat en Python</h3>

<p>Per fer la HA ho fem d'una manera molt fàcil amb un try i un exepct si falla una connexió entra a l'altra:</p>

```python
def conectar_bd():
    ''' Función para conectar a PostgreSQL'''
    try:
        conn = psycopg2.connect(
            dbname="asixhospitalbd",
            user="grupomaviunal",
            password="uN@i3st4fu3rtE",
            host="snakeeater1.equemmfoundation.top",
        )
        cur = conn.cursor()
        return conn, cur
    except psycopg2.Error as e:
        conn = psycopg2.connect(
            dbname="asixhospitalbd",
            user="grupomaviunal",
            password="uN@i3st4fu3rtE",
            host="revolverocelot.equemmfoundation.top",
            port="5433"
        )
        cur = conn.cursor()
        return conn, cur
```