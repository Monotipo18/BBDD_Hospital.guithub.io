# Índex

1. [Instal·lació](#instal·lació)
    - [Pasos de Instalació](#pasos-de-instalació)
    - [Cómo utilizar pg_anonymize](#cómo-utilizar-pg_anonymize)
2. [Cómo utilizar pg_anonymize](#cómo-utilizar-pg_anonymize)
    - [Configuracions Previas](#configuracions-previas)
    - [Configuración pg_anonymize](#configuración-pg_anonymize)
3. [Dades de caràcter personal de grau alt](#dades-de-caràcter-personal-de-grau-alt)
    - [Aquestes son les dades que enmascararem](#aquestes-son-les-dades-que-enmascararem)
4. [Webgrafía](#webgrafía)

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


# Com utilizar pg_anonymize
## Configuracions Previas
#### Insertar informació a la base de dades, en el nuestre cas creem la taula y posem unes dades inventades
```sql
CREATE TABLE public.customer(id integer,
first_name text,
last_name text,
birthday date,
phone_number text);
INSERT INTO public.customer VALUES (1, 'Col', 'Iflor', '00-00-00', '+34 1234 5678');
INSERT INTO public.customer VALUES (2, 'Rosa', 'Melano', '00-00-00', '+34 1234 5678');
```
#### També creem un usuari que en el nostre cas l'anomenarem Col
```sql
CREATE ROLE Col LOGIN PASSWORD '1234'
```
#### A continuació, asignarem permisos de conexió a la base de dades hospital y de lectura a la taula customer.
```sql
GRANT CONNECT ON DATABASE hospital TO Col;
GRANT SELECT ON TABLE public.customer TO Col;
```
## Configuració pg_anonymize
Amb els passos anteriors realitzats, ens connectem a la Base de dades (en el nostre cas "hospital") i executarem les següents comandes per carregar pg_anonymize:

En primer lloc:
```sql
LOAD 'pg_anonymize';
```
Amb aquesta comanda carreguem pg_anonymize dins de la nostra base de dades.

En segon lloc:
```sql
SECURITY LABEL FOR pg_anonymize ON ROLE Col IS 'anonymize';
```
Amb aquesta comanda anonimitzem les dades que el senyor Col podrà veure de la base de dades.

En tercer lloc:
```sql
SECURITY LABEL FOR pg_anonymize ON COLUMN public.customer.last_name
    IS $$substr(last_name, 1, 1) || '*****'$$;
```
Amb aquesta comanda, substituïm tots els caràcters excepte l'inicial de la columna last_name de la taula customers per *, d'aquesta manera els usuaris que no tinguin autorització no podran veure aquesta informació.

A continuació:
```sql
SECURITY LABEL FOR pg_anonymize ON COLUMN public.customer.birthday
    IS $$date_trunc('year', birthday)::date$$;
```
Amb aquesta comanda, retallem l'any de naixement per mostrar només l'any.

Y per finalitzar:
```sql
SECURITY LABEL FOR pg_anonymize ON COLUMN public.customer.phone_number
    IS $$regexp_replace(phone_number, '\d', 'X', 'g')$$;
```
Amb aquesta comanda, substituïm els números de telèfon per una X

## Dades de caràcter personal de grau alt.
### Aquestes son les dades que enmascararem:

**Informació d'Identificació Personal (PII):**

- Noms complets dels pacients.
- Números d'identificació personal (com ara números de la Seguretat Social, números d'identificació nacional, etc.).
- Dates de naixement.
- Adreces residencials i de contacte.
- Números de telèfon.

**Informació Mèdica Sensible:**

- Històries clíniques i mèdiques.
- Resultats de proves mèdiques, com ara anàlisis de sang, proves de diagnòstic per imatges, etc.
- Diagnòstics mèdics.
- Informació sobre tractaments mèdics i medicaments recetats.
- Informació sobre al·lèrgies i condicions mèdiques cròniques.

**Informació Financera:**

- Informació de següros mèdics i de salut.
- Facturació i registres de serveis mèdics.
- Informació de targetes de credit o dèbit utilitzades per pagar serveis mèdics.

**Informació Laboral i d'Assegurança:**

- Informació laboral relacionada amb beneficis de salut i llicències mèdiques.
- Detalls sobre reclamacions de compensació laboral.

Dins de la nostra base de dades hi ha informació esmentada anteriorment que encara no estem utilitzant. Aquest document és per a futurs usos i en cas de continuar ampliant la BDD, s'haurà de tenir en compte.

# Enmascarament de les dades de caràcter personal de grau alt

## Rol Médico
```sql
SECURITY LABEL FOR pg_anonymize ON ROLE medicos IS 'anonymize';
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Paciente.DNI
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Paciente.telefon
    IS $$substr(telefon, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Paciente.Num_Seguretat_Social
    IS $$substr(Num_Seguretat_Social, 1, 1) || '*****'$$;
```
## Rol Administrativo
```sql
SECURITY LABEL FOR pg_anonymize ON ROLE Administratius IS 'anonymize';
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Paciente.DNI
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Paciente.telefon
    IS $$substr(telefon, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Paciente.Num_Seguretat_Social
    IS $$substr(Num_Seguretat_Social, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.Estudis
    IS $$substr(Estudis, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.DNI
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.Nom
    IS $$substr(Nom, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.Primer_Cognom
    IS $$substr(Primer_Cognom, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.Segon_Cognom
    IS $$substr(Segon_Cognom, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.Telefon
    IS $$substr(Telefon, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.Curriculum
    IS $$substr(Curriculum, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.email
    IS $$substr(email, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal_vari.DNI
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Metge_Metgessa.DNI
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visitas_Programadas.Diagnostic
    IS $$substr(Diagnostic, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visitas_Programadas.Medicaments
    IS $$substr(Medicaments, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visitas_Programadas.Fecha
    IS $$substr(Fecha, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visitas_Programadas.Hora
    IS $$substr(Hora, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visitas_Programadas.DNI
    IS $$substr(DNI, 1, 1) || '*****'$$;
```
## Rol Paciente
```sql
SECURITY LABEL FOR pg_anonymize ON ROLE medicos IS 'anonymize';
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visitas_Programadas.DNI
    IS $$substr(DNI, 1, 1) || '*****'$$;
```
## Rol Enfermero
```sql
SECURITY LABEL FOR pg_anonymize ON ROLE enfermero IS 'anonymize';
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visitas_Programadas.DNI
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visitas_Programadas.Diagnostic
    IS $$substr(Diagnostic, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visitas_Programadas.Medicaments
    IS $$substr(Medicaments, 1, 1) || '*****'$$;
```
## Tabla Especialidad
```sql
SECURITY LABEL FOR pg_anonymize ON ROLE medicos IS 'anonymize';
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Especialidad.DNI
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON ROLE administratius IS 'anonymize';
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Especialidad.DNI
    IS $$substr(DNI, 1, 1) || '*****'$$;
```
## Otras Directivas
### Tabla Personal Infermeria
```sql
SECURITY LABEL FOR pg_anonymize ON medicos IS 'anonymize';
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal_Infermeria.DNI
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal_Infermeria.DNI_Medic
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON Administratius IS 'anonymize';
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal_Infermeria.DNI
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal_Infermeria.DNI_Medic
    IS $$substr(DNI, 1, 1) || '*****'$$;
```
### Tabla Operaciones
```sql
SECURITY LABEL FOR pg_anonymize ON medicos IS 'anonymize';
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operaciones.DNI
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operaciones.DNI_metge
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR Administratius IS 'anonymize';
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operaciones.ID_Opereaciones
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operaciones.Data
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operaciones.Hora
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operaciones.Tipus_Operacio
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operaciones.ID_Paciente
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operaciones.Num_Quirofano
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operaciones.DNI_metge
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR enfermeros IS 'anonymize';
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operaciones.DNI_metge
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR Celador IS 'anonymize';
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operaciones.DNI_metge
    IS $$substr(DNI, 1, 1) || '*****'$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operaciones.Tipus_Operacio
    IS $$substr(DNI, 1, 1) || '*****'$$;
```

### Webgrafía
[https://github.com/rjuju/pg_anonymize?tab=readme-ov-file](https://github.com/rjuju/pg_anonymize?tab=readme-ov-file)
