# Documentacio del Esquema de seguretat
## Projecte Intermodular
### Contingut
-  [Permisos Teorics](#permisos)
    -  [Metges](#Metges)
    -  [Infermer](#Infermer)
    -  [Zeladors](#Zeladors)
    -  [Administratius](#Administratius)
    -  [Conductors d'ambulancia](#conductors-ambulancia)
    -  [Pacients](#pacients)
-  [Permisos de sistema](#permisos-de-sistema)
    -  [Rol Metges](#grup-metges)
    -  [Rol Infermers](#grup-infermers)
    -  [Rol Celadors](#grup-celadors)
    -  [Rol Administratius](#grup-administratius)
    -  [Rol Conductor d'ambulancia](#grup-conductors-dambulancia)
    -  [Rol Pacients](#grup-pacients)
-  [Permisos de Dades](#permisos-de-roles-en-tablas)
    -  [Rol Metges](#rol-metges)
    -  [Rol Infermers](#rol-infermers)
    -  [Rol Administratius](#rol-administratius)
    -  [Rol Pacients](#rol-pacients)
    -  [Rol Conductors d'ambulancia](#rol-conductors-dambulancia)
    -  [Rol Celadors](#rol-celadors)
    

# Permisos
## **Metges**

Considerem que el grup de metges inclou tots els treballadors que siguin professionals de la salut capacitats i autoritzats per a diagnosticar, tractar i prevenir malalties i lesions 

Els metges poden tenir especialitats de medicina interna, pediatria, cirurgia, ginecologia, neurologia, entre altres. A més els metges també poden realitzar cirurgies, receptar medicaments, ordenar proves diagnòstiques i assessorar els pacients.

Per això hem decidit que els metges poden realitzar les següents accions en les taules de la BD:

| Taules | Permisos |
| :---:       |     :---:      |
| Aparells_medics  | `Veure y modificar`    |
| Especialitat     | `Veure la taula`      |
| Habitacio        | `Veure y modificar`     |
| Metge_metgessa   | `Res`       |
| Operacions       | `Veure y modificar`     |
| Pacient          | `Veure y modificar`      |
| Personal         | `Res`    |
| Personal_infermeria|  `Veure la taula`     |
| Personal_vari    | `Res`     |
| Planta           |  `Veure la taula`       |
| Quirofan         | `Veure la taula`     |
| Reserva_habitacio| `Veure y modificar`       |
| Reserva_Quirofan | `Veure y modificar`     |
| Visites_programades | `Veure y modificar`    |

A més d'això sé si no és necessari per al metge se li aplicarà data masking a les dades de caràcter personal i no se li permetrà accedir a unes certes columnes (dades) que no necessita consultar, per exemple que no pugui consultar informació privada de metges ( companys de treball).

# **Infermer**

Considerem que el grup d'infermers inclou tots els treballadors que siguin professionals de la salut capacitats i que brindin cures i atenció directa als pacients, la seva funció seria realitzar assistència en la cura de la salut, realitzar avaluacions, administrar medicaments, dur a terme tractaments prescrits per metges, monitorar signes vitals, proporcionar suport emocional i educació al pacient i familiars, entre altres coses.

Per això hem decidit que els infermers poden realitzar les següents accions en les taules de la BD:

| Taules | Permisos |
| :---:         |     :---:      |
| Aparells_medics  | `Ver i modificar la tabla`     |
| Especialitat     | `Res`      |
| Habitacio        | `Veure la taula`     |
| Metge_metgessa   | `Res`       |
| Operacions       | `Veure la taula`    |
| Pacient          | `Res`      |
| Personal         | `Res`    |
| Personal_infermeria|  `Res`     |
| Personal_vari    | `Res`     |
| Planta           |  `Veure la taula`       |
| Quirofan         | `Veure la taula`     |
| Reserva_habitacio| `Veure la taula`       |
| Reserva_Quirofan | `Veure la taula`    |
| Visites_programades | `Veure la taula `   |

A més, si no és necessari per al metge se li aplicarà data masking a les dades de caràcter personal i no se li permetrà accedir a unes certes columnes (dades) que no necessita consultar.

# **Zeladors**

Considerem que el grup de zelador inclou tots els treballadors que siguin professionals de la salut que *esten capacitats a l'hora de fer tasques de suport i assistència.Les seves responsabilitats poden incloure el trasllat de pacients d'un lloc a un altre dins del centre, el transport de material mèdic, l'ajuda en la mobilització de pacients, la distribució de subministraments, entre altres funcions relacionades amb la logística i el suport operatiu en l'àmbit sanitari. 

Per això hem decidit que els Zeladors poden realitzar les següents accions en les taules de la BD:

| Taules | Permisos |
| :---:       |     :---:      |
| Aparells_medics  | `Veure y modificar`    |
| Especialitat     | `Res`      |
| Habitacio        | `Veure la taula`     |
| Metge_metgessa   | `Res`       |
| Operacions       | `Veure la taula`     |
| Pacient          | `Veure la taula`      |
| Personal         | `Res`    |
| Personal_infermeria|  `Res`     |
| Personal_vari    | `Res`     |
| Planta           |  `Veure la taula`       |
| Quirofan         | `Veure la taula`     |
| Reserva_habitacio| `Veure la taula`       |
| Reserva_Quirofan | `Veure la taula`     |
| Visites_programades | `Veure la taula`    |

# **Administratius**

| Taules | Permisos |
| :---:       |     :---:      |
| Aparells_medics  | `Tot`    |
| Especialitat     | `Tot`      |
| Habitacio        | `Tot`     |
| Metge_metgessa   | `Tot`       |
| Operacions       | `Tot`     |
| Pacient          | `Tot`      |
| Personal         | `Tot`    |
| Personal_infermeria|  `Tot`     |
| Personal_vari    | `Tot`     |
| Planta           |  `Tot`       |
| Quirofan         | `Tot`     |
| Reserva_habitacio| `Tot`       |
| Reserva_Quirofan | `Tot`     |
| Visites_programades | `Tot`    |

# Conductors ambulancia

| Taules | Permisos |
| :---:       |     :---:      |
| Aparells_medics  | `Res`    |
| Especialitat     | `Res`      |
| Habitacio        | `Res`     |
| Metge_metgessa   | `Res`       |
| Operacions       | `Res`     |
| Pacient          | `Res`      |
| Personal         | `Res`    |
| Personal_infermeria|  `Res`     |
| Personal_vari    | `Res`     |
| Planta           |  `Res`       |
| Quirofan         | `Res`     |
| Reserva_habitacio| `Res`       |
| Reserva_Quirofan | `Res`     |
| Visites_programades | `Res`    |

# Pacients
| Taules | Permisos |
| :---:       |     :---:      |
| Aparells_medics  | `Res`    |
| Especialitat     | `Res`      |
| Habitacio        | `Res`     |
| Metge_metgessa   | `Res`       |
| Operacions       | `Res`     |
| Pacient          | `Nomes veure el seu camp a la taula`      |
| Personal         | `Res`    |
| Personal_infermeria|  `Res`     |
| Personal_vari    | `Res`     |
| Planta           |  `Res`       |
| Quirofan         | `Res`     |
| Reserva_habitacio| `Res`       |
| Reserva_Quirofan | `Res`     |
| Visites_programades | `Res`    |

# **Rols de Grup**
### Permisos de sistema
## Grup Metges

Hem decidit crear el rol de metges per adjuntar tots el usuaris que siguin metges (o derivats d'aquest o similars) perque tinguin tots els mateixos permisos.

El rol/grup no ha de poder iniciar sesio pero si els usuaris(aixo s'indica a l'hora de crear l'usuari), no seran superusuaris ni podran crear BD ni rols, pero els usuaris membres del rol podran heredar els seus permisos tant a nivell de sitema com a nivell de dades i per ultim no podrian fer replicas de la BD.

> [!NOTE]
> Els permis de NOLOGIN no s'hereda , es per aixo que el usuari quan es crea s'ha d'indicar que pot iniciar sessio.

```
CREATE ROLE medicos WITH
	 NOLOGIN
	 NOSUPERUSER
	 NOCREATEDB
	 NOCREATEROLE
	 INHERIT
	 NOREPLICATION
	 CONNECTION LIMIT -1;
```
Els membres del grup podran conectarse a la BD
```
grant connect on database asixhospitalbd to medicos;
```
Els membres del grup podran fer servir l'schema 'hospital' (on es troben les dades).
```
grant usage on schema hospital to medicos;
```
## Grup Infermers

Hem decidit crear el rol de infermers per adjuntar tots el usuaris que siguin infermers (o derivats d'aquest o similars) perque tinguin tots els mateixos permisos.

El rol/grup no ha de poder iniciar sesio pero si els usuaris(aixo s'indica a l'hora de crear l'usuari), no seran superusuaris ni podran crear BD ni rols, pero els usuaris membres del rol podran heredar els seus permisos tant a nivell de sitema com a nivell de dades i per ultim no podrian fer replicas de la BD.

> [!NOTE]
> Els permis de NOLOGIN no s'hereda , es per aixo que el usuari quan es crea s'ha d'indicar que pot iniciar sessio.

```
CREATE ROLE enfermeros WITH
    NOLOGIN
    NOSUPERUSER
    NOCREATEDB
    NOCREATEROLE
    INHERIT
    NOREPLICATION
    ONNECTION LIMIT -1;
```
Els membres del grup podran conectarse a la BD

```
grant connect on database asixhospitalbd to enfermeros;
```
Els membres del grup podran fer servir l'schema 'hospital' (on es troben les dades).
```
grant usage on schema hospital to enfermeros;
```
## Grup Celadors

Hem decidit crear el rol de celadors per adjuntar tots el usuaris que siguin celadors, perque tinguin tots els mateixos permisos.

El rol/grup no ha de poder iniciar sesio pero si els usuaris(aixo s'indica a l'hora de crear l'usuari), no seran superusuaris ni podran crear BD ni rols, pero els usuaris membres del rol podran heredar els seus permisos tant a nivell de sitema com a nivell de dades i per ultim no podrian fer replicas de la BD.

> [!NOTE]
> Els permis de NOLOGIN no s'hereda , es per aixo que el usuari quan es crea s'ha d'indicar que pot iniciar sessio.

```
CREATE ROLE celadores WITH
    NOLOGIN
    NOSUPERUSER
    NOCREATEDB
    NOCREATEROLE
    INHERIT
    NOREPLICATION
    CONNECTION LIMIT -1;
```
Els membres del grup podran conectarse a la BD
```
grant connect on database asixhospitalbd to celadores;
```
Els membres del grup podran fer servir l'schema 'hospital' (on es troben les dades).
```
grant usage on schema hospital to celadores;
```
## Grup Administratius

Hem decidit crear el rol de Administratius per adjuntar tots el usuaris que siguin Administradors del hospital, perque tinguin tots els mateixos permisos.

El rol/grup no ha de poder iniciar sesio pero si els usuaris(aixo s'indica a l'hora de crear l'usuari), no seran superusuaris ni podran crear BD ni rols, pero els usuaris membres del rol podran heredar els seus permisos tant a nivell de sitema com a nivell de dades i per ultim no podrian fer replicas de la BD.

> [!NOTE]
> Els permis de NOLOGIN no s'hereda , es per aixo que el usuari quan es crea s'ha d'indicar que pot iniciar sessio.

```
CREATE ROLE administrativos WITH
    NOLOGIN
    NOSUPERUSER
    NOCREATEDB
    NOCREATEROLE
    INHERIT
    NOREPLICATION
    CONNECTION LIMIT -1;
```
Els membres del grup podran conectarse a la BD
```
grant connect on database asixhospitalbd to administrativos;
```
Els membres del grup podran fer servir l'schema 'hospital' (on es troben les dades).
```
grant usage on schema hospital to administrativos;
```

## Grup Conductors d'ambulancia

Hem decidit crear el rol de conductors d'ambulancia per adjuntar tots el usuaris que siguin con del mateix sector, perque tinguin tots els mateixos permisos.

El rol/grup no ha de poder iniciar sesio pero si els usuaris(aixo s'indica a l'hora de crear l'usuari), no seran superusuaris ni podran crear BD ni rols, pero els usuaris membres del rol podran heredar els seus permisos tant a nivell de sitema com a nivell de dades i per ultim no podrian fer replicas de la BD.

> [!NOTE]
> Els permis de NOLOGIN no s'hereda , es per aixo que el usuari quan es crea s'ha d'indicar que pot iniciar sessio.

```
CREATE ROLE conductores_ambulancia WITH
    NOLOGIN
    NOSUPERUSER
    NOCREATEDB
    NOCREATEROLE
    INHERIT
    NOREPLICATION
    CONNECTION LIMIT -1;
```
Els membres del grup podran conectarse a la BD
```
grant connect on database asixhospitalbd to conudctores_ambulancia;
```
Els membres del grup podran fer servir l'schema 'hospital' (on es troben les dades).
```
grant usage on schema hospital to grant connect on database asixhospitalbd to conudctores_ambulancia;
```

## Grup Pacients

Hem decidit crear el rol de Pacients per adjuntar tots el usuaris pacients del hospital, cada usuario nomes podra mirar el seu camp d'informacio.

El rol/grup no ha de poder iniciar sesio pero si els usuaris(aixo s'indica a l'hora de crear l'usuari), no seran superusuaris ni podran crear BD ni rols, pero els usuaris membres del rol podran heredar els seus permisos tant a nivell de sitema com a nivell de dades i per ultim no podrian fer replicas de la BD.

> [!NOTE]
> Els permis de NOLOGIN no s'hereda , es per aixo que el usuari quan es crea s'ha d'indicar que pot iniciar sessio.

```
CREATE ROLE pacientes WITH
    NOLOGIN
    NOSUPERUSER
    NOCREATEDB
    NOCREATEROLE
    INHERIT
    NOREPLICATION
    CONNECTION LIMIT -1;
```
Els membres del grup podran conectarse a la BD
```
grant connect on database asixhospitalbd to pacientes;
```
Els membres del grup podran fer servir l'schema 'hospital' (on es troben les dades).
```
grant usage on schema hospital to pacientes;
```

# Permisos de roles en tablas:
## Rol metges

Els permisos a nivell de dades del rol de metges son els seguents:
```
GRANT SELECT, INSERT, UPDATE ON hospital.aparells_medics TO medicos
GRANT SELECT ON hospital.especialidad TO medicos
GRANT SELECT, INSERT, UPDATE ON hospital.habitacion TO medicos
GRANT SELECT, INSERT, UPDATE ON hospital.operaciones TO medicos
GRANT SELECT, INSERT, UPDATE ON hospital.paciente TO medicos
GRANT SELECT ON hospital.personal_infermeria TO medicos
GRANT SELECT ON hospital.planta TO medicos
GRANT SELECT ON hospital.quirofano TO medicos
GRANT SELECT, INSERT, UPDATE ON hospital.reserva_habitacion TO medicos
GRANT SELECT, INSERT, UPDATE ON hospital.reserva_quirofan TO medicos
GRANT SELECT, INSERT, UPDATE ON hospital.visitas_programadas TO medicos
```
## Rol Infermers

Els permisos a nivell de dades del rol de Infermers son els segunets:
```
GRANT SELECT, INSERT, UPDATE ON hospital.aparells_medics TO enfermeros
GRANT SELECT ON hospital.habitacion TO enfermeros
GRANT SELECT ON hospital.operaciones TO enfermeros
GRANT SELECT ON hospital.planta TO enfermeros
GRANT SELECT ON hospital.quirofano TO enfermeros
GRANT SELECT ON hospital.reserva_habitacion TO enfermeros
GRANT SELECT ON hospital.reserva_quirofan TO enfermeros
GRANT SELECT ON hospital.visitas_programadas TO enfermeros
```
## Rol Administratius

Els permisos a nivell de dades del rol de Administratius son els seguents:
```
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA hospital TO administrativos
```
## Rol Pacients

Els permisos a nivell de dades del rol de Pacients son els seguents:
```
GRANT SELECT(nom, primer_cognom, segon_cognom, telefon, data_naixement) ON hospital.paciente TO pacientes
GRANT SELECT ON hospital.cita_medica TO pacients
```
## Rol Conductors d'ambulancia

Els usuaris membres dels rols d'ambulancia no poden fer res actualment pero si en un futur l'hospital vol fer cambis
grans ja tindran el rol amb els permisos.

## Rol Celadors

Els permisos a nivell de dades del rol de Celadors son els seguents:
```
GRANT SELECT ON hospital.operaciones TO celadores
GRANT SELECT ON hospital.planta TO celadores
GRANT SELECT ON hospital.quirofano TO celadores
GRANT SELECT ON hospital.reserva_habitacion TO celadores
GRANT SELECT ON hospital.reserva_quirofan TO celadores
```

