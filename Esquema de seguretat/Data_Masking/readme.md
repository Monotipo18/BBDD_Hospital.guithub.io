# Índex

1. [Instal·lació](#instal·lació)
    - [Pasos de Instalació](#pasos-de-instalació)
    - [Cómo utilizar pg_anonymize](#cómo-utilizar-pg_anonymize)
2. [Cómo utilizar pg_anonymize](#cómo-utilizar-pg_anonymize)
    - [Configuraciones Previas](#configuraciones-previas)
    - [Configuración pg_anonymize](#configuración-pg_anonymize)
3. [Webgrafía](#webgrafía)

# Instal·lació
## Pasos de instalació
Per poder realitzar la instal·lació correctament, prèviament hem de instal·lar un metapaquet anomenat build-essential amb la següent comanda:

```bash
apt-get install build-essential
```

A continuació, adjunto una captura de pantalla de com executar la comanda.

Aquest paquet serveix com a compilador del llenguatge de programació C juntament amb make, d'aquesta manera reduim les possibilitats que make pugui fallar.

Seguidament, clonem el repositori des d'aquí: [https://github.com/rjuju/pg_anonymize?tab=readme-ov-file](https://github.com/rjuju/pg_anonymize?tab=readme-ov-file). Utilitzarem la següent comanda:

```bash
git clone https://github.com/rjuju/pg_anonymize.git
```

Adjunto una captura de pantalla de com executar la comanda git Clone.

A continuació, entrem a la carpeta que hem descarregat en el pas anterior:

```bash
cd pg_anonymize
```

Adjunto una captura de pantalla de `ls`.

Seguidament, instal·lem make:

```bash
sudo apt install make
```

Adjunto una captura de pantalla de la instal·lació de make.

Un cop instal·lat make, a la carpeta descarregada anteriorment del git clone, executem la següent comanda:

```bash
sudo make
```

Seguidament, executem una altra:

```bash
sudo make install
```

Adjunto captures de pantalla dels comandaments make i make install.

Seguint els passos anteriors, ja tenim pg_anonymize instal·lat a la nostra màquina.


# Cómo utilizar pg_anonymize
## Configuraciones Previas
#### Insertar información en la base de datos, en nuestro caso creamos la tabla y le añadimos unos datos inventados
```sql
CREATE TABLE public.customer(id integer,
first_name text,
last_name text,
birthday date,
phone_number text);
INSERT INTO public.customer VALUES (1, 'Col', 'Iflor', '00-00-00', '+34 1234 5678');
INSERT INTO public.customer VALUES (2, 'Rosa', 'Melano', '00-00-00', '+34 1234 5678');
```
#### También crearemos un usuario que en nuestro caso lo llamaremos Col
```sql
CREATE ROLE Col LOGIN PASSWORD '1234'
```
#### A continuación, asignaremos permisos de conexión a la base de datos hospital y de lectura a la tabla customer.
```sql
GRANT CONNECT ON DATABASE hospital TO Col;
GRANT SELECT ON TABLE public.customer TO Col;
```
## Configuración pg_anonymize
Con los pasos anteriores realizados, nos conectamos a la Base de datos (en nuestro caso "hospital") y ejecutaremos las siguientes comandas para cargar pg_anonymize:
En primer lugar:
```sql
LOAD 'pg_anonymize';
```
Con esta comando cargamos pg_anonymize dentro de nuestra base de datos.
En segundo lugar:
```sql
SECURITY LABEL FOR pg_anonymize ON ROLE Col IS 'anonymize';
```
Con esta comando anonimizamos las datos que el señor Col podrá ver de la base de datos.
En tercer lugar:
```sql
SECURITY LABEL FOR pg_anonymize ON COLUMN public.customer.last_name
    IS $$substr(last_name, 1, 1) || '*****'$$;
```
Con esta comando, sustituimos todos los caracteres menos el inicial de la columna last_name de la tabla customers por *, de esta manera los usuarios que no tengan autorización, no podrán ver esta información.
A continuación:
```sql
SECURITY LABEL FOR pg_anonymize ON COLUMN public.customer.birthday
    IS $$date_trunc('year', birthday)::date$$;
```
Con esta comando cortamos el año de nacimiento para que solo muestre el año.
Y para acabar:
```sql
SECURITY LABEL FOR pg_anonymize ON COLUMN public.customer.phone_number
    IS $$regexp_replace(phone_number, '\d', 'X', 'g')$$;
```
Con esta comando sustituimos los números de teléfono por una X.
### Webgrafía
[https://github.com/rjuju/pg_anonymize?tab=readme-ov-file](https://github.com/rjuju/pg_anonymize?tab=readme-ov-file)
