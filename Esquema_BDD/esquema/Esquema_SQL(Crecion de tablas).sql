CREATE TABLE Paciente
(
  ID_Paciente SERIAL NOT NULL,
  DNI VARCHAR(9) NOT NULL,
  Nom VARCHAR(25) NOT NULL,
  Primer_Cognom VARCHAR(50) NOT NULL,
  Segon_Cognom VARCHAR(50) NOT NULL,
  Telefon VARCHAR(15) NOT NULL,
  Data_Naixement DATE NOT NULL,
  Sexe VARCHAR(1) NOT NULL,
  Num_Seguretat_Social VARCHAR(12) NOT NULL,
  PRIMARY KEY (ID_Paciente),
  UNIQUE (Num_Seguretat_Social)
);

CREATE TABLE Planta
(
  Num_Planta SERIAL NOT NULL,
  PRIMARY KEY (Num_Planta)
);

CREATE TABLE Habitacion
(
  Num_Habitacion VARCHAR(25) NOT NULL,
  Num_Planta INT NOT NULL,
  PRIMARY KEY (Num_Habitacion),
  FOREIGN KEY (Num_Planta) REFERENCES Planta(Num_Planta)
);

CREATE TABLE Reserva_Habitacion
(
  ID_Reserva SERIAL NOT NULL,
  Dia_Ingresa DATE NOT NULL,
  Dia_Sortida DATE NOT NULL,
  Num_Habitacion VARCHAR(25) NOT NULL,
  ID_Paciente INT NOT NULL,
  PRIMARY KEY (ID_Reserva),
  FOREIGN KEY (Num_Habitacion) REFERENCES Habitacion(Num_Habitacion),
  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente)
);

CREATE TABLE Personal
(
  Curriculum BYTEA NOT NULL,
  Estudis TEXT NOT NULL,
  DNI VARCHAR(9) NOT NULL,
  NOM VARCHAR(25) NOT NULL,
  Primer_Cognom VARCHAR(50) NOT NULL,
  Segon_cognom VARCHAR(50) NOT NULL,
  Telefon VARCHAR(9) NOT NULL,
  ID_PERSONAL INT NOT NULL,
  PRIMARY KEY (DNI),
  UNIQUE (ID_PERSONAL)
  Tipus_Personal VARCHAR(50) NOT NULL,
);

CREATE TABLE Personal_vari
(
  DNI VARCHAR(9) NOT NULL,
  PRIMARY KEY (DNI),
  FOREIGN KEY (DNI) REFERENCES Personal(DNI)
);

CREATE TABLE Metge_Metgessa
(
  DNI VARCHAR(9) NOT NULL,
  ID_Paciente INT NOT NULL,
  PRIMARY KEY (DNI),
  FOREIGN KEY (DNI) REFERENCES Personal(DNI),
  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente)
);

CREATE TABLE Visitas_Programadas
(
  ID_Visita SERIAL NOT NULL,
  Diagnostic TEXT NOT NULL,
  Medicaments VARCHAR(80) NOT NULL,
  Fecha DATE NOT NULL,
  Hora TIME NOT NULL,
  Ya_Visitat CHAR(1) CHECK (Ya_Visitat IN ('S', 'N')),
  ID_Paciente INT NOT NULL,
  DNI VARCHAR(9) NOT NULL,
  PRIMARY KEY (ID_Visita),
  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente),
  FOREIGN KEY (DNI) REFERENCES Metge_Metgessa(DNI)
);

CREATE TABLE Especialidad
(
  Nom_Especialitat VARCHAR(50) NOT NULL,
  ID_Especialidad INT NOT NULL,
  DNI VARCHAR(9) NOT NULL,
  PRIMARY KEY (ID_Especialidad),
  FOREIGN KEY (DNI) REFERENCES Metge_Metgessa(DNI)
);

CREATE TABLE Quirofano
(
  Num_Quirofano SERIAL NOT NULL,
  Num_Planta INT NOT NULL,
  PRIMARY KEY (Num_Quirofano),
  FOREIGN KEY (Num_Planta) REFERENCES Planta(Num_Planta)
);

CREATE TABLE Aparells_Medics
(
  ID_Aparells_Medics SERIAL NOT NULL,
  Nombre_Aperell_Medic VARCHAR(250) NOT NULL,
  Num_Quirofano INT NOT NULL,
  PRIMARY KEY (ID_Aparells_Medics),
  FOREIGN KEY (Num_Quirofano) REFERENCES Quirofano(Num_Quirofano)
);

CREATE TABLE Reserva_Quirofan
(
  Num_reserva_Quirofan SERIAL NOT NULL,
  Num_Quirofano INT NOT NULL,
  PRIMARY KEY (Num_reserva_Quirofan),
  FOREIGN KEY (Num_Quirofano) REFERENCES Quirofano(Num_Quirofano)
);

CREATE TABLE Operaciones
(
  ID_Opereaciones SERIAL NOT NULL,
  Data DATE NOT NULL,
  Hora TIME NOT NULL,
  Tipus_Operacio VARCHAR(250) NOT NULL,
  ID_Paciente INT NOT NULL,
  Num_Quirofano INT NOT NULL,
  DNI_metge VARCHAR(9) NOT NULL,
  PRIMARY KEY (ID_Opereaciones),
  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente),
  FOREIGN KEY (Num_Quirofano) REFERENCES Quirofano(Num_Quirofano),
  FOREIGN KEY (DNI_metge) REFERENCES Metge_Metgessa(DNI)
);

CREATE TABLE Personal_Infermeria
(
  DNI VARCHAR(9) NOT NULL,
  DNI_Medic VARCHAR(9),
  Num_Planta INT NOT NULL,
  ID_Opereaciones INT NOT NULL,
  PRIMARY KEY (DNI),
  FOREIGN KEY (DNI) REFERENCES Personal(DNI),
  FOREIGN KEY (DNI) REFERENCES Metge_Metgessa(DNI),
  FOREIGN KEY (Num_Planta) REFERENCES Planta(Num_Planta),
  FOREIGN KEY (ID_Opereaciones) REFERENCES Operaciones(ID_Opereaciones)
);
CREATE TABLE Agenda_Metge
(
  id_Agenda_Metge SERIAL NOT NULL,
  Fecha DATE NOT NULL,
  Hora TIME NOT NULL,
  DNI_Metge VARCHAR(9) NOT NULL,
  PRIMARY KEY (id_Agenda_Metge),
  FOREIGN KEY (DNI_Metge) REFERENCES hospital.metge_metgessa(DNI),
  UNIQUE (Fecha),
  UNIQUE (Hora)
);
