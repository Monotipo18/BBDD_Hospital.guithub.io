# Documentacio del Esquema de seguretat
## Projecte Intermodular
### Contingut
- ### [Metges](#Metges)
- ### [Infermer](#Infermer)
- ### [Zeladors](#Zeladors)
- ### [Administratius](#Administratius)
# Permisos
## **Metges**

Considerem que el grup de metges inclou tots els treballadors que siguin professionals de la salut capacitats i autoritzats per a diagnosticar, tractar i prevenir malalties i lesions 

Els metges poden tenir especialitats de medicina interna, pediatria, cirurgia, ginecologia, neurologia, entre altres. A més els metges també poden realitzar cirurgies, receptar medicaments, ordenar proves diagnòstiques i assessorar els pacients.

Per això hem decidit que els metges poden realitzar les següents accions en les taules de la BD:

| Tablas | Permisos |
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

| Tablas | Permisos |
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

Per això hem decidit que els Zeladors poden realitzar les següents accions en les taules de la *BD:

- **Aparells\_medics:** Ver y modificar la tabla
- **Especialidad:** Nada
- **Habitacion:** Ver la tabla
- **Metge\_metgessa:** Nada
- **Operacions:**  Ver la tabla
- **Paciente:** Nada
- **Personal:** Nada
- **personal\_Infermeria:** Nada
- **personal\_vari:** Nada
- **planta:** Ver la tabla
- **quirofano:** Ver la tabla
- **reserva\_habitacion:** Ver la tabla
- **reserva\_quirofano:** Ver la tabla
- **visitas\_programadas:** Ver la tabla


# **Administratius**

- **Aparells\_medics:** Todo
- **Especialidad:** Todo
- **Habitacion:** Todo
- **Metge\_metgessa:** Todo
- **Operacions:**  Todo
- **Paciente:** Todo
- **Personal:** Todo
- **personal\_Infermeria:** Todo
- **personal\_vari:** Todo
- **planta:** Todo
- **quirofano:** Todo
- **reserva\_habitacion:** Todo
- **reserva\_quirofano:** Todo
- **visitas\_programadas:** Todo

# <a name="_nnorx95tsa1c"></a>Conductors ambulancia

- **Aparells\_medics:** Nada
- **Especialidad:** Nada
- **Habitacion:** Nada
- **Metge\_metgessa:** Nada
- **Operacions:**  Nada
- **Paciente:** Nada
- **Personal:** Nada
- **personal\_Infermeria:** Nada
- **personal\_vari:** Nada
- **planta:** Nada
- **quirofano:** Nada
- **reserva\_habitacion:** Nada
- **reserva\_quirofano:** Nada
- **visitas\_programadas:** Nada

# <a name="_iif1a84nkwag"></a>Pacients


- **Aparells\_medics:** Nada
- **Especialidad:** Nada
- **Habitacion:** Nada
- **Metge\_metgessa:** Nada
- **Operacions:**  Nada
- **Paciente:** Ver su campo  en la tabla
- **Personal:** Nada
- **personal\_Infermeria:** Nada
- **personal\_vari:** Nada
- **planta:** Nada
- **quirofano:** Nada
- **reserva\_habitacion:** Nada
- **reserva\_quirofano:** Nada
- **visitas\_programadas:** Nada

# <a name="_xl5wh6yizu39"></a>**Roles de Grupo**
## <a name="_ok0bj5a5yab7"></a>Metges

CREATE ROLE medicos WITH

`	`NOLOGIN

`	`NOSUPERUSER

`	`NOCREATEDB

`	`NOCREATEROLE

`	`INHERIT

`	`NOREPLICATION

`	`CONNECTION LIMIT -1;

grant connect on database asixhospitalbd to medicos;

grant usage on schema hospital to medicos;

## <a name="_oaylasd4aovt"></a>Enfermeros

CREATE ROLE enfermeros WITH

`	`NOLOGIN

`	`NOSUPERUSER

`	`NOCREATEDB

`	`NOCREATEROLE

`	`INHERIT

`	`NOREPLICATION

`	`CONNECTION LIMIT -1;

grant connect on database asixhospitalbd to enfermeros;

grant usage on schema hospital toenfermeros;






## <a name="_yqep9tpuumzp"></a>Celadores

CREATE ROLE celadores WITH

`	`NOLOGIN

`	`NOSUPERUSER

`	`NOCREATEDB

`	`NOCREATEROLE

`	`INHERIT

`	`NOREPLICATION

`	`CONNECTION LIMIT -1;

grant connect on database asixhospitalbd to celadores;

grant usage on schema hospital to celadores;

## <a name="_9cq1v3izgtip"></a>Administratius

CREATE ROLE administrativos WITH

`	`NOLOGIN

`	`NOSUPERUSER

`	`NOCREATEDB

`	`NOCREATEROLE

`	`INHERIT

`	`NOREPLICATION

`	`CONNECTION LIMIT -1;

grant connect on database asixhospitalbd to administrativos;

grant usage on schema hospital to administrativos;










## <a name="_gk3xbxij49ab"></a>Conductores de Ambulancia

CREATE ROLE conductores\_ambulancia WITH

`	`NOLOGIN

`	`NOSUPERUSER

`	`NOCREATEDB

`	`NOCREATEROLE

`	`INHERIT

`	`NOREPLICATION

`	`CONNECTION LIMIT -1;

grant connect on database asixhospitalbd to conductores\_ambulancia;

grant usage on schema hospital to conductores\_ambulancia;
## <a name="_z9t8ww1ycaku"></a>Pacientes

CREATE ROLE pacientes WITH

`	`NOLOGIN

`	`NOSUPERUSER

`	`NOCREATEDB

`	`NOCREATEROLE

`	`INHERIT

`	`NOREPLICATION

`	`CONNECTION LIMIT -1;




grant connect on database asixhospitalbd to pacientes;

grant usage on schema hospital to pacientes;


#
#
# <a name="_rvg3eja156ps"></a><a name="_b59kukf3nv5s"></a><a name="_5ppwavudzaf8"></a>Permisos de roles en tablas:

## <a name="_7i1ez4cmyur"></a>Rol medicos

|<p>GRANT SELECT, INSERT, UPDATE ON hospital.aparells\_medics TO medicos</p><p>GRANT SELECT ON hospital.especialidad TO medicos</p><p>GRANT SELECT, INSERT, UPDATE ON hospital.habitacion TO medicos</p><p>GRANT SELECT, INSERT, UPDATE ON hospital.operaciones TO medicos</p><p>GRANT SELECT, INSERT, UPDATE ON hospital.paciente TO medicos</p><p>GRANT SELECT ON hospital.personal\_infermeria TO medicos</p><p>GRANT SELECT ON hospital.planta TO medicos</p><p>GRANT SELECT ON hospital.quirofano TO medicos</p><p>GRANT SELECT, INSERT, UPDATE ON hospital.reserva\_habitacion TO medicos</p><p>GRANT SELECT, INSERT, UPDATE ON hospital.reserva\_quirofan TO medicos</p><p>GRANT SELECT, INSERT, UPDATE ON hospital.visitas\_programadas TO medicos</p>|
| :- |

Rol enfermeros

||
| :- |

