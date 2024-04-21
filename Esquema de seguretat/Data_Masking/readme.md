# Instal·lació

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


# Com utlitzar pg_anonymize
## Configuracions Previes
#### - Previament hem d'insertar informació ala base de dades en el meu cas afegire la taula i li afegire també unes dades inventades
``` sql
CREATE TABLE public.customer(id integer,
first_name text,
last_name text,
birthday date,
phone_number text);
INSERT INTO public.customer VALUES (1, 'Manu', 'Alvarez', '00-00-00', '+34 1234 5678');
INSERT INTO public.customer VALUES (2, 'Alex', 'Martinez', '00-00-00', '+34 1234 5678');
```
#### També hem de crear un usuario que en el meu cas el nom de usuario sera alex
``` sql
CREATE ROLE Alex LOGIN PASSWORD '1234'
```
#### Li assignarem permisos de conexio ala base de dades hospital i de nomes lectura ala taula customer
``` sql
GRANT CONNECT ON DATABASE hospital TO Alex;
GRANT SELECT ON TABLE public.customer TO Alex;
```
#### Configuració pg_anonymize
Quan hem fet el pasos anteriors hem d'entrar a la Base de dades en el nostre cas hospital i exucutar les següents comandes per carregar pg_anonymize i dirle al 
postgres que X usuario tindra certas filas no visibles
``` sql
LOAD 'pg_anonymize';
SECURITY LABEL FOR pg_anonymize ON ROLE Alex IS 'anonymize';
SECURITY LABEL FOR pg_anonymize ON COLUMN public.customer.last_name
    IS $$substr(last_name, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN public.customer.birthday
    IS $$date_trunc('year', birthday)::date$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN public.customer.phone_number
    IS $$regexp_replace(phone_number, '\d', 'X', 'g')$$;
```

### Webgrafia
https://github.com/rjuju/pg_anonymize?tab=readme-ov-file

### Instalació detellada
