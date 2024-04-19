# Instalació 
            -Prèviament hem d'instal·lar un metapaquete que es diu ```bash apt-get install build-essential ```
            ```bash as ```
            Captura de pantalla de como hago el comando
             que serveix com a compilador juntament amb make si no fem això és molt probable que el make
             pugui fallar
            - Previament hem de clonar el repositori aquests de aqui: https://github.com/rjuju/pg_anonymize?tab=readme-ov-file
              amb ```bash git clone https://github.com/rjuju/pg_anonymize.git ```
            Captura de pantall de como hago el git Clone  
            - Cuan hem fet això hem d'entrar ala carpeta que hem descaregat ```bash cd pg_anonymize ```
            Captura de pantall de LS

#Configuració pg_anonymize
    ## Configuracions Previes
    ### - Previament hem d'insertar informació ala base de dades en el meu cas afegire la taula i li afegire també unes dades inventades
        ``` sql
        CREATE TABLE public.customer(id integer,
            first_name text,
            last_name text,
            birthday date,
            phone_number text);
        INSERT INTO public.customer VALUES (1, 'Manu', 'Alvarez', '00-00-00', '+34 1234 5678');
        INSERT INTO public.customer VALUES (2, 'Alex', 'Martinez', '00-00-00', '+34 1234 5678');
        ```
    ### També hem de crear un usuario que en el meu cas el nom de usuario sera alex
    ``` sql
        CREATE ROLE Alex1 LOGIN PASSWORD '1234'
    ```
    ### Li assignarem permisos de conexio ala base de dades hospital i de nomes lectura ala taula customer
    ``` sql
        GRANT CONNECT ON DATABASE hospital TO Alex;
        GRANT SELECT ON TABLE public.customer TO Alex;
    ```
    ### Configuració pg_anonymize
        




### Webgrafia
https://github.com/rjuju/pg_anonymize?tab=readme-ov-file


ALTER ROLE Alex SET session_preload_libraries = 'pg_anonymize';
-- pg_anonymize need to be loaded before declaring SECURITY LABEL
LOAD 'pg_anonymize';
SECURITY LABEL FOR pg_anonymize ON ROLE Alex IS 'anonymize';

SECURITY LABEL FOR pg_anonymize ON COLUMN public.customer.last_name
    IS $$substr(last_name, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN public.customer.birthday
    IS $$date_trunc('year', birthday)::date$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN public.customer.phone_number
    IS $$regexp_replace(phone_number, '\d', 'X', 'g')$$;