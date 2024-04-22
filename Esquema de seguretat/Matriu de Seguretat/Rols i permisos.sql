grant connect on database "Hospital_Pruebas" to medicos;
grant usage on schema hospital to medicos;
grant connect on database "Hospital_Pruebas" to enfermeros;
grant usage on schema hospital to enfermeros;
grant connect on database "Hospital_Pruebas" to celadores;
grant usage on schema hospital to celadores;
grant connect on database "Hospital_Pruebas" to administrativos;
grant usage on schema hospital to administrativos;
--grant connect on database "Hospital_Pruebas" to conudctores_ambulancia;
--grant usage on schema hospital to grant connect on database Hospital_Pruebas to conudctores_ambulancia;
grant connect on database "Hospital_Pruebas" to pacientes;
grant usage on schema hospital to pacientes;
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
GRANT SELECT ON hospital.reserva_quirofan TO enfermeros;
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

GRANT SELECT(nom, primer_cognom, segon_cognom, telefon, data_naixement) ON hospital.pacient TO pacient;
GRANT SELECT ON hospital.cita_medica TO pacients
--Modifiquem per que només el pacient pugui veure la seva fitxa
CREATE VIEW pacient_usuario_conectado AS
SELECT nom, primer_cognom, segon_cognom, telefon, data_naixement
FROM hospital.pacient
WHERE usuario = current_user;

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
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA hospital TO administrativos


--Celadors
CREATE ROLE Celador WITH
	NOLOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1;
GRANT SELECT ON hospital.operaciones TO celadores;
GRANT SELECT ON hospital.planta TO celadores;
GRANT SELECT ON hospital.quirofano TO celadores;
GRANT SELECT ON hospital.reserva_habitacion TO celadores;
GRANT SELECT ON hospital.reserva_quirofan TO celadores;
