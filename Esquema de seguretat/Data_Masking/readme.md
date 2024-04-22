# Índex

# Índice

1. [Instal·lació](#instal·lació)
    - [Pasos de Instal·lació](#pasos-de-instalació)
2. [Com utilitzar pg_anonymize](#com-utilitzar-pg_anonymize)
    - [Configuracions Prèvies](#configuracions-prèvies)
    - [Configuració pg_anonymize](#configuració-pg_anonymize)
3. [Dades de caràcter personal de grau alt](#dades-de-caràcter-personal-de-grau-alt)
    - [Aquestes són les dades que enmascararem](#aquestes-són-les-dades-que-enmascararem)
4. [Enmascarament de les dades de caràcter personal de grau alt](#enmascarament-de-les-dades-de-caràcter-personal-de-grau-alt)
5. [Webgrafía](#webgrafía)



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

## Etiquetes de seguretat per a rols i columnes

### Rol metges
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE metges IS 'anonymize';
```

#### Anonimització de dades dels pacients per als metges
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Pacient.DNI
    IS $$REPEAT('*', LENGTH(DNI))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Pacient.telefon
    IS $$REPEAT('*', LENGTH(telefon))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Pacient.Num_Seguretat_Social
    IS $$REPEAT('*', LENGTH(Num_Seguretat_Social))::VARCHAR$$;
```

### Rol administratius
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE Administratius IS 'anonymize';
```

#### Anonimització de dades dels pacients per als administratius
``` sql
    SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Pacient.DNI
    IS $$REPEAT('*', LENGTH(DNI))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Pacient.telefon
    IS $$REPEAT('*', LENGTH(telefon))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Pacient.Num_Seguretat_Social
    IS $$REPEAT('*', LENGTH(Num_Seguretat_Social))::VARCHAR$$;
```


#### Personal metge i administratiu
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE Administratius IS 'anonymize';
```

#### Anonimització de dades del personal
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.Estudis
    IS $$CAST(REPEAT('*', LENGTH(Estudis)) AS TEXT)$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.DNI
    IS $$REPEAT('*', LENGTH(DNI))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.Nom
    IS $$REPEAT('*', LENGTH(Nom))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.Primer_Cognom
    IS $$REPEAT('*', LENGTH(Primer_Cognom))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.Segon_Cognom
    IS $$REPEAT('*', LENGTH(Segon_Cognom))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.Telefon
    IS $$REPEAT('*', LENGTH(Telefon))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.Curriculum
    IS $$E'\\052'::bytea$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal.email
    IS $$REPEAT('*', LENGTH(email))::VARCHAR$$;
```
#### Personal variat
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE Administratius IS 'anonymize';
```

#### Anonimització de dades del personal variat
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal_vari.DNI
    IS $$REPEAT('*', LENGTH(DNI))::VARCHAR$$;
```

#### Metges i metgesses
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE Administratius IS 'anonymize';
```

#### Anonimització de dades dels metges i metgesses
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Metge_Metgessa.DNI
    IS $$REPEAT('*', LENGTH(DNI))::VARCHAR$$;
```
#### Visites programades
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE Administratius IS 'anonymize';
```

#### Anonimització de dades de les visites programades
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visites_Programades.Diagnostic
    IS $$REPEAT('*', LENGTH(Diagnostic))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visites_Programades.Medicaments
    IS $$REPEAT('*', LENGTH(Medicaments))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visites_Programades.Fecha
    IS $$CAST(REPEAT('*', LENGTH(TO_CHAR(Fecha, 'YYYY-MM-DD'))) AS TEXT)$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visites_Programades.Hora
    IS $$REPEAT('*', LENGTH(TO_CHAR(Hora, 'HH24:MI:SS')))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visites_Programades.DNI
    IS $$REPEAT('*', LENGTH(DNI))::VARCHAR$$;
```
### Rols específics

#### Rol pacient
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE metges IS 'anonymize';
```

#### Anonimització de dades dels pacients per als pacients
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visites_Programades.DNI
    IS $$REPEAT('*', LENGTH(DNI))::VARCHAR$$;
```
### Rol infermer/a
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE infermers IS 'anonymize';
```

#### Anonimització de dades dels pacients i visites programades per als infermers
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visites_Programades.DNI
    IS $$REPEAT('*', LENGTH(DNI))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visites_Programades.Diagnostic
    IS $$REPEAT('*', LENGTH(Diagnostic))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Visites_Programades.Medicaments
    IS $$REPEAT('*', LENGTH(Medicaments))::VARCHAR$$;
```
### Especialitat mèdica

#### Rol metge
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE metges IS 'anonymize';
```
#### Anonimització de dades de l'especialitat mèdica per als metges
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.especialitat.dni_metge
    IS $$REPEAT('*', LENGTH(dni_metge))::VARCHAR$$;
```
#### Rol administratiu
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE administratius IS 'anonymize';
```

#### Anonimització de dades de l'especialitat mèdica per als administratius
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.especialitat.dni_metge
    IS $$REPEAT('*', LENGTH(dni_metge))::VARCHAR$$;
```

### Personal d'infermeria
#### Rol metge
``` sql
SECURITY LABEL FOR pg_anonymize ON metges  IS 'anonymize';
```
#### Anonimització de dades del personal d'infermeria per als metges
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal_Infermeria.DNI
    IS $$REPEAT('*', LENGTH(DNI))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal_Infermeria.DNI_Medic
    IS $$REPEAT('*', LENGTH(DNI_Medic))::VARCHAR$$;
```

#### Rol Administratius
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE administratius IS 'anonymize';
```

#### Anonimització de dades del personal d'infermeria per als administratius
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal_Infermeria.DNI
    IS $$REPEAT('*', LENGTH(DNI))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Personal_Infermeria.DNI_Medic
    IS $$REPEAT('*', LENGTH(DNI_Medic))::VARCHAR$$;
```
### Operacions

#### Rol metge
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE metges IS 'anonymize';
```
#### Anonimització de dades d'operacions per als metges
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operacions.dni_metge
    IS $$REPEAT('*', LENGTH(dni_metge))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operacions.DNI_metge
    IS $$REPEAT('*', LENGTH(DNI_metge))::VARCHAR$$;
```
#### Rol administratiu
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE administratius IS 'anonymize';
```
#### Anonimització de dades d'operacions per als administratius
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.operacions.id_operacions
    IS $$REPEAT('*', LENGTH(id_operacions::VARCHAR))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operacions.Data
    IS $$CAST(REPEAT('*', LENGTH(TO_CHAR(Data, 'YYYY-MM-DD'))) AS TEXT)$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operacions.Hora
    IS $$REPEAT('*', LENGTH(TO_CHAR(Hora, 'HH24:MI:SS')))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operacions.Tipus_Operacio
    IS $$REPEAT('*', LENGTH(Tipus_Operacio))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operacions.ID_Pacient
    IS $$REPEAT('*', LENGTH(CAST(ID_Pacient AS VARCHAR)))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operacions.Num_Quirofan
    IS $$REPEAT('*', LENGTH(CAST(Num_Quirofan AS VARCHAR)))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operacions.DNI_metge
    IS $$REPEAT('*', LENGTH(DNI_metge))::VARCHAR$$;
```
#### Rol infermer/a
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE infermers IS 'anonymize';
```
#### Anonimització de dades d'operacions per als infermers
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operacions.DNI_metge
    IS $$substr(DNI_metge, 1, 1) || '*****'$$;
```
#### Rol celador
``` sql
SECURITY LABEL FOR pg_anonymize ON ROLE celador  IS 'anonymize';
```
#### Anonimització de dades d'operacions per als celadors
``` sql
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operacions.DNI_metge
    IS $$REPEAT('*', LENGTH(DNI_metge))::VARCHAR$$;
SECURITY LABEL FOR pg_anonymize ON COLUMN hospital.Operacions.Tipus_Operacio
    IS $$REPEAT('*', LENGTH(Tipus_Operacio))::VARCHAR$$;
```

### Webgrafía
[https://github.com/rjuju/pg_anonymize?tab=readme-ov-file](https://github.com/rjuju/pg_anonymize?tab=readme-ov-file)
