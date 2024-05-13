<!-- Introduccion -->
<h1>SSL/TLS x PostgreSQL</h1>
<p>Primer de tot cal aclarir una cosa SSL, avui dia no s'utilitza, ja que el protocol TLS (Transport Layer Security) el va substituir en 1999, a dia d'avui, 12 d'abril de 2024, és l'estàndard en la seva versió TLS 1.3, però el terme SSL es continua utilitzant per a referir-se a connexions segures</p>
<p>Ara bé, per què hauries d'utilitzar TLS per a PostgreSQL?
La resposta curta és seguretat, la llarga és una mica més complexa, quan et connectes amb el teu client al servidor estàs transmetent informació per la xarxa, ja sigui per WAN o LAN, de per si mateix aquesta informació no sol estar encriptada, així que posar un TLS encripta l'informació entre servidor i client, assegurant-se que la informació ni es llegeixi, ni es modifiqui.
També cal tenir en compte reglaments,estàndards i lleis, que varien segons el país, però normalment totes tenen el mateix objectiu, la seguretat d'informació confidencial i sensible</p>

<!-- Instalacion -->
<h3>Preparar domini</h3>

<p>Nosaltres utilitzarem un domini per al TLS així aconseguirem comunicació una mica més segura i a part la renovació automàtica serà més fàcil, nosaltres recomanem Cloudflare, però pots utilitzar el que més et convingui.</p>
<img src="/img/cloudflarepanel.png">
<img src="/img/cloudflareejemplodesubdominio.png">

<h3>Preparar al Firewall</h3>

<p>Important hem de tenir ben filtrat els ports, en aquest cas el 80, important cal anar amb compte a l'hora de tractar amb ports, ja pot ser una vulneravilitat de seguretat, cal permetre en la màquina, en el meu cas és PROXMOX VEU, com en l'encaminador, encara que nosaltres no vam mostrar com fer-ho en l'encaminador, ja que cada encaminador és un món igualment hi ha molta informació de com obrir un port d'encaminador, però hauria de quedar una cosa així:<p>
<p>PROXMOX VE:</p>
<img src="/img/proxmoxvefirewall.png">
<p>Router:</p>
<img src="/img/routerejemplofirewall.png">

<h3>Instalar Certbot</h3>

<p>Per a generar els certificats utilitzarem Certbot,
nosaltres utilitzarem la comanda per a sistemes basats en Ubuntu/Debian:</p>

```bash
sudo apt install certbot
```
<p>Anem a la carpeta de configuracio PostgreSQL, normalment sol ser aquesta:</p>

```bash
cd /etc/postgresql/15/main
```

<p>Generem el certificat</p>

```bash
sudo certbot certonly --standalone -d subdominio.detudominio
```

<p>Per a verificar el certificat</p>

```bash
sudo certbot certificates
```

<h3>Renovació automàticament del certificat</h3>
<p>Creem el "script" per a la renovació automàtica</p>

```bash
sudo nano /etc/letsencrypt/renewal-hooks/deploy/postgresql.deploy
```

<p>Entrem en l'arxiu amb la comanda 'nano' i introduïm el següent:</p>

```bash
#!/bin/bash
umask 0177
export DOMAIN=example.com
export DATA_DIR=/etc/postgresql/15/main
cp /etc/letsencrypt/live/$DOMAIN/fullchain.pem $DATA_DIR/server.crt
cp /etc/letsencrypt/live/$DOMAIN/privkey.pem   $DATA_DIR/server.key
chown postgres:postgres  $DATA_DIR/server.crt $DATA_DIR/server.key
# only for SELinux - CentOS, Red Hat
# chcon -t postgresql_db_t $DATA_DIR/server.crt $DATA_DIR/server.key
```

<p>Ho fem executable:</p>

```bash
sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/postgresql.deploy
```

<h3>Configurar PostgreSQL</h3>

<p>A continuació, ens dirigim a l'arxiu de configuració i canviem la part de SSL al següent:</p>

```bash
# - SSL -

ssl = on
#ssl_ca_file = ''
ssl_cert_file = 'server.crt'
#ssl_crl_file = ''
#ssl_crl_dir = ''
ssl_key_file = 'server.key'
#ssl_ciphers = 'HIGH:MEDIUM:+3DES:!aNULL' # allowed SSL ciphers
ssl_prefer_server_ciphers = on
#ssl_ecdh_curve = 'prime256v1'
#ssl_min_protocol_version = 'TLSv1.2'
#ssl_max_protocol_version = ''
#ssl_dh_params_file = ''
#ssl_passphrase_command = ''
#ssl_passphrase_command_supports_reload = off
```

<p>També hem de configurar el ‘pg_hba.conf’ si volem que tothom es connecti, al final de la línia de l'arxiu agreguem aquesta comanda:</p>

```bash
hostssl all all 0.0.0.0/0 md5
```

<p>I ja ho tindríem, ara si volem comprovar-ho podem fer-ho de diverses maneres, per exemple des de pgadmin 4:</p>

```sql
SELECT * FROM pg_catalog.pg_stat_ssl
```
