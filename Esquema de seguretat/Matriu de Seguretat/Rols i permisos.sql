--Medicos
CREATE ROLE medicos WITH
	NOLOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1;
GRANT SELECT ON hospital.especialidad TO medicos;
GRANT SELECT, INSERT, UPDATE ON hospital.habitacion TO medicos;
GRANT SELECT, INSERT, UPDATE ON hospital.operaciones TO medicos;
GRANT SELECT, INSERT, UPDATE ON hospital.paciente TO medicos;
GRANT SELECT ON hospital.personal_infermeria TO medicos;
GRANT SELECT ON hospital.planta TO medicos;
GRANT SELECT ON hospital.quirofano TO medicos;
GRANT SELECT, INSERT, UPDATE ON hospital.reserva_habitacion TO medicos;
GRANT SELECT, INSERT, UPDATE ON hospital.reserva_quirofano TO medicos;
GRANT SELECT, INSERT, UPDATE ON hospital.visitas_programadas TO medicos;

--Enfermers
CREATE ROLE enfermeros WITH
	NOLOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1;
GRANT SELECT, INSERT, UPDATE ON hospital.aparells_medics TO enfermeros;
GRANT SELECT ON hospital.habitacion TO enfermeros;
GRANT SELECT ON hospital.operaciones TO enfermeros;
GRANT SELECT ON hospital.planta TO enfermeros;
GRANT SELECT ON hospital.quirofano TO enfermeros;
GRANT SELECT ON hospital.reserva_habitacion TO enfermeros;
GRANT SELECT ON hospital.reserva_quirofano TO enfermeros;
GRANT SELECT ON hospital.visitas_programadas TO enfermeros;

--Conductors d'ambulancia
CREATE ROLE conductores_ambulancia WITH
	NOLOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1;

--Pacients
CREATE ROLE pacient WITH
	NOLOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1;

GRANT SELECT(nom, primer_cognom, segon_cognom, telefon, data_naixement) ON hospital.paciente TO pacient;
GRANT SELECT ON hospital.cita_medica TO pacient;
--Modifiquem per que només el pacient pugui veure la seva fitxa
CREATE VIEW pacient_usuario_conectado AS
SELECT nom, primer_cognom, segon_cognom, telefon, data_naixement
FROM hospital.paciente
WHERE nom = current_user;

GRANT SELECT ON pacient_usuario_conectado TO pacient;

--Administratius

CREATE ROLE Administratius WITH
	NOLOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA hospital TO Administratius;


--Celadors
CREATE ROLE Celador WITH
	NOLOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1;
GRANT SELECT ON hospital.operaciones TO Celador;
GRANT SELECT ON hospital.planta TO Celador;
GRANT SELECT ON hospital.quirofano TO Celador;
GRANT SELECT ON hospital.reserva_habitacion TO Celador;
GRANT SELECT ON hospital.reserva_quirofano TO Celador;
grant connect on database asixhospitalbd to medicos;
grant usage on schema hospital to medicos;
grant connect on database asixhospitalbd to enfermeros;
grant usage on schema hospital to enfermeros;
grant connect on database asixhospitalbd to Celador;
grant usage on schema hospital to Celador;
--Nateja
CREATE ROLE Personal_Nateja WITH
	NOLOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1;
--Administratius
grant connect on database asixhospitalbd to Administratius;
grant usage on schema hospital to Administratius;
--grant connect on database asixhospitalbd to conudctores_ambulancia;
--grant usage on schema hospital to grant connect on database asixhospitalbd to conudctores_ambulancia;
--Paciente
grant connect on database asixhospitalbd to pacient;
grant usage on schema hospital to pacient;
