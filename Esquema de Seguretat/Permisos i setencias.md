# Documentacio del Esquema de seguretat

## <a name="_g6jjofn67z48"></a>**Metges**

Consideramos que el grupo de médicos incluye todos los trabajadores que sean profesionales de la salud capacitados y autorizados para diagnosticar, tratar y prevenir enfermedades y lesiones 

Los médicos pueden tener especialidades de medicina interna, pediatría, cirugía, ginecología, neurología, entre otras. Además los médicos también pueden realizar cirugías, recetar medicamentos, ordenar pruebas diagnósticas y asesorar a los pacientes.

Por eso hemos decidido que los médicos pueden realizar las siguientes acciones en las tablas de la BD:

| Tablas | Permisos |
| :---:       |     :---:      |
| Aparells_medics  | `Ver y modificar la tabla`    |
| Especialitat     | `Ver la tabla`      |
| Habitacio        | `Ver y modificar`     |
| Metge_metgessa   | `Nada`       |
| Operacions       | `Ver y modificar`     |
| Pacient          | `Ver y modificar`      |
| Personal         | `Nada`    |
| Personal_infermeria|  `Ver la tabla`     |
| Personal_vari    | `Nada`     |
| Planta           |  `Ver la tabla`       |
| Quirofan         | `Ver la tabla`     |
| Reserva_habitacio| `Ver y modificar`       |
| Reserva_Quirofan | `Ver y modifica`     |
| Visites_programades | `Ver y modificar`    |

Además de eso sé si no es necesario para el médico se le aplicará data masking a los datos de carácter personal y no se le permitirá acceder a ciertas columnas (datos) que no necesita consultar, por ejemplo que no pueda consultar información privada de médicos ( compañeros de trabajo).

# <a name="_ta759hl62xx6"></a>**Enfermero**

Consideramos que el grupo de enfermeros incluye todos los trabajadores que sean profesionales de la salud capacitados y que brinden cuidados y atención directa a los pacientes, su función sería realizar asistencia en el cuidado de la salud, realizar evaluaciones, administrar medicamentos, llevar a cabo tratamientos prescritos por médicos, monitorear signos vitales, proporcionar apoyo emocional y educación al paciente y familiares, entre otras cosas.

Por eso hemos decidido que los enfermeros pueden realizar las siguientes acciones en las tablas de la BD:

| Tablas | Permisos |
| :---         |     :---:      |
| Aparells_medics  | Ver y modificar la tabla     |
| Especialitat     | Ver la tabla      |
| Habitacio        | Ver y modificar     |
| Metge_metgessa   | Nada       |
| Operacions       | Ver y modificar     |
| Pacient          | Ver y modificar      |
| Personal         | Nada    |
| Personal_infermeria|  Ver la tabla     |
| Personal_vari    | Nada     |
| Planta           |  Ver la tabla       |
| Quirofan         | Ver la tabla     |
| Reserva_habitacio| Ver y modificar       |
| Reserva_Quirofan | Ver y modifica     |
| Visites_programades | Ver y modificar    |

**Aparells\_medics:** Ver y modificar la tabla

**Especialidad:** Nada

**Habitacion:** Ver la tabla

**Metge\_metgessa:** Nada

**Operacions:**  Ver la tabla

**Paciente:** Nada

**Personal:** Nada

**personal\_Infermeria:** Nada

**personal\_vari:** Nada

**planta:** Ver la tabla

**quirofano:** Ver la tabla

**reserva\_habitacion:** Ver la tabla

**reserva\_quirofano:** Ver la tabla

**visitas\_programadas:** Ver la tabla

Además de eso sé si no es necesario para el médico se le aplicará data masking a los datos de carácter personal y no se le permitirá acceder a ciertas columnas (datos) que no necesita consultar).
# <a name="_o55kofuvhe97"></a>**Zeladors**


Consideramos que el grupo de celador incluye todos los trabajadores que sean profesionales de la salud que esten capacitados a la hora de realizar tareas de apoyo y asistencia.Sus responsabilidades pueden incluir el traslado de pacientes de un lugar a otro dentro del centro, el transporte de material médico, la ayuda en la movilización de pacientes, la distribución de suministros, entre otras funciones relacionadas con la logística y el soporte operativo en el ámbito sanitario. 

Por eso hemos decidido que los Celadores pueden realizar las siguientes acciones en las tablas de la BD:

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


# <a name="_5aixhysidyph"></a>**Administratius**

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

