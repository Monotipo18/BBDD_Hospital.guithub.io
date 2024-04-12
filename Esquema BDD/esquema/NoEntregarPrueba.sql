CREATE TABLE Paciente
(
  ID_Paciente INT NOT NULL,
  DNI INT NOT NULL,
  Nom INT NOT NULL,
  1r_Cognom INT NOT NULL,
  N_ºSeguretat_Social INT NOT NULL,
  PRIMARY KEY (ID_Paciente),
  UNIQUE (N_ºSeguretat_Social)
);

CREATE TABLE Planta
(
  Nº_Planta INT NOT NULL,
  PRIMARY KEY (Nº_Planta)
);

CREATE TABLE Habitacion
(
  Nº_Habitacion INT NOT NULL,
  Nº_Planta INT NOT NULL,
  PRIMARY KEY (Nº_Habitacion),
  FOREIGN KEY (Nº_Planta) REFERENCES Planta(Nº_Planta)
);

CREATE TABLE Reserva_Habitacion
(
  ID_Reserva INT NOT NULL,
  DIa_Ingresa INT NOT NULL,
  Dia_Sortida INT NOT NULL,
  Nº_Habitacion INT NOT NULL,
  ID_Paciente INT NOT NULL,
  PRIMARY KEY (ID_Reserva),
  FOREIGN KEY (Nº_Habitacion) REFERENCES Habitacion(Nº_Habitacion),
  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente)
);

CREATE TABLE Personal
(
  Curriculum INT NOT NULL,
  Estudis INT NOT NULL,
  DNI INT NOT NULL,
  NOM INT NOT NULL,
  Primer_Cognom INT NOT NULL,
  Segon_cognom INT NOT NULL,
  Telefon INT NOT NULL,
  ID_PERSONAL INT NOT NULL,
  PRIMARY KEY (DNI),
  UNIQUE (ID_PERSONAL)
);

CREATE TABLE Personal_vari
(
  Tipus_Personal INT NOT NULL,
  DNI INT NOT NULL,
  PRIMARY KEY (DNI),
  FOREIGN KEY (DNI) REFERENCES Personal(DNI)
);

CREATE TABLE Metge_Metgessa
(
  DNI INT NOT NULL,
  ID_Paciente INT NOT NULL,
  PRIMARY KEY (DNI),
  FOREIGN KEY (DNI) REFERENCES Personal(DNI),
  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente)
);

CREATE TABLE Visitas_Programadas
(
  ID_Visita INT NOT NULL,
  Diagnostic INT NOT NULL,
  Medicaments INT NOT NULL,
  Fecha INT NOT NULL,
  Hora INT NOT NULL,
  Ya_Visitat INT NOT NULL,
  ID_Paciente INT NOT NULL,
  ID_Paciente INT NOT NULL,
  DNI INT NOT NULL,
  PRIMARY KEY (ID_Visita),
  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente),
  FOREIGN KEY (DNI) REFERENCES Metge_Metgessa(DNI)
);

CREATE TABLE Especialidad
(
  Nom_Especialitat INT NOT NULL,
  ID_Especialidad INT NOT NULL,
  DNI INT NOT NULL,
  FOREIGN KEY (DNI) REFERENCES Metge_Metgessa(DNI)
);

CREATE TABLE Quirofano
(
  NºQuirofano INT NOT NULL,
  Nº_Planta INT NOT NULL,
  PRIMARY KEY (NºQuirofano),
  FOREIGN KEY (Nº_Planta) REFERENCES Planta(Nº_Planta)
);

CREATE TABLE Aparells_Medics
(
  ID_Aparells_Medics INT NOT NULL,
  Nombre_Aperell_Medic INT NOT NULL,
  NºQuirofano INT NOT NULL,
  PRIMARY KEY (ID_Aparells_Medics),
  FOREIGN KEY (NºQuirofano) REFERENCES Quirofano(NºQuirofano)
);

CREATE TABLE Reserva_Quirofan_
(
  Nº_Reserva_Quirofan INT NOT NULL,
  NºQuirofano INT NOT NULL,
  PRIMARY KEY (Nº_Reserva_Quirofan),
  FOREIGN KEY (NºQuirofano) REFERENCES Quirofano(NºQuirofano)
);

CREATE TABLE Operaciones
(
  ID_Opereaciones INT NOT NULL,
  Data INT NOT NULL,
  Hora INT NOT NULL,
  Tipus_Operacio INT NOT NULL,
  ID_Paciente INT NOT NULL,
  NºQuirofano INT NOT NULL,
  DNI INT NOT NULL,
  PRIMARY KEY (ID_Opereaciones),
  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente),
  FOREIGN KEY (NºQuirofano) REFERENCES Quirofano(NºQuirofano),
  FOREIGN KEY (DNI) REFERENCES Metge_Metgessa(DNI)
);

CREATE TABLE Personal_Infermeria
(
  DNI INT NOT NULL,
  DNI INT NOT NULL,
  Nº_Planta INT NOT NULL,
  ID_Opereaciones INT NOT NULL,
  PRIMARY KEY (DNI),
  FOREIGN KEY (DNI) REFERENCES Personal(DNI),
  FOREIGN KEY (DNI) REFERENCES Metge_Metgessa(DNI),
  FOREIGN KEY (Nº_Planta) REFERENCES Planta(Nº_Planta),
  FOREIGN KEY (ID_Opereaciones) REFERENCES Operaciones(ID_Opereaciones)
);
