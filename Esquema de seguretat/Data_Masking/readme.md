# Instalació
Per poder fer l'instalacio correctament prèviament hem d'instal·lar un metapaquet que es diu build-essential amb la seguent comanda:
```apt-get install build-essential ```
Captura de pantalla de como hago el comando
Aquest paquet serveix com a compilador juntament amb make, fent aixo reduim les posibilitats que el make pugui fallar

Seguidament hem de clonar el repositori aquests de aqui: https://github.com/rjuju/pg_anonymize?tab=readme-ov-file.
Utilitzarem la seguent comanda:
``` git clone https://github.com/rjuju/pg_anonymize.git ```
Captura de pantall de como hago el git Clone  
- A continuacio hem d'entrar a la carpeta que hem descaregat en el pas anterior:
```bash cd pg_anonymize ```
Captura de pantall de LS
- Seguidament intalem make.
  ``` apt install make```
  (Captura instalacion make)
- Quan tenim instal·lat el make, en la carpeta descarregada anteriorment del guitclone executem la següent comanda:
 ``` sudo make```
 Seguidament exucutem un altre
 ``` sudo make install```
- (Captura make i make install) 
- Seguin els pasos anteriors ya tenim el pg_anonymize instal·lat ala nostra maquina
  


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
