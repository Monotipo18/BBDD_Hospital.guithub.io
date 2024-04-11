CREATE TABLE Visitas_Programadas
(
  ID_Visita INT NOT NULL,
  Diagnostic INT NOT NULL,
  Medicaments INT NOT NULL,
  Fecha INT NOT NULL,
  Hora INT NOT NULL,
  Ya_Visitat INT NOT NULL,
  ID_Paciente INT NOT NULL,
  PRIMARY KEY (ID_Visita)
);

CREATE TABLE Paciente
(
  ID_Paciente INT NOT NULL,
  DNI INT NOT NULL,
  Nom INT NOT NULL,
  Primer_Cognom INT NOT NULL,
  N_ºSeguretat_Social INT NOT NULL,
  PRIMARY KEY (ID_Paciente),
  UNIQUE (N_ºSeguretat_Social)
);

CREATE TABLE Personal_Vari
(
  ID_Personal_Vari INT NOT NULL,
  Tipus_de_feina INT NOT NULL,
  PRIMARY KEY (ID_Personal_Vari)
);

CREATE TABLE Personal
(
  Nom INT NOT NULL,
  Primer_Cognom INT NOT NULL,
  Segon_Cognom INT NOT NULL,
  Telefón INT NOT NULL,
  DNI INT NOT NULL,
  PRIMARY KEY (DNI)
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

CREATE TABLE Reserva_Quirofan_
(
  Nº_Reserva_Quirofan INT NOT NULL,
  PRIMARY KEY (Nº_Reserva_Quirofan)
);

CREATE TABLE Pot_Tenir2
(
  ID_Paciente INT NOT NULL,
  ID_Visita INT NOT NULL,
  PRIMARY KEY (ID_Paciente, ID_Visita),
  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente),
  FOREIGN KEY (ID_Visita) REFERENCES Visitas_Programadas(ID_Visita)
);

CREATE TABLE Hi_ha1
(
  DNI INT NOT NULL,
  ID_Personal_Vari INT NOT NULL,
  PRIMARY KEY (DNI, ID_Personal_Vari),
  FOREIGN KEY (DNI) REFERENCES Personal(DNI),
  FOREIGN KEY (ID_Personal_Vari) REFERENCES Personal_Vari(ID_Personal_Vari)
);

CREATE TABLE Metge_Metgessa
(
  ID_Personal_Medic INT NOT NULL,
  Estudis INT NOT NULL,
  Curriculum INT NOT NULL,
  ID_Paciente INT NOT NULL,
  PRIMARY KEY (ID_Personal_Medic),
  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente)
);

CREATE TABLE Especialidad
(
  Nom_Especialitat INT NOT NULL,
  ID_Especialidad INT NOT NULL,
  ID_Personal_Medic INT NOT NULL,
  FOREIGN KEY (ID_Personal_Medic) REFERENCES Metge_Metgessa(ID_Personal_Medic)
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

CREATE TABLE Fa
(
  ID_Personal_Medic INT NOT NULL,
  ID_Visita INT NOT NULL,
  PRIMARY KEY (ID_Personal_Medic, ID_Visita),
  FOREIGN KEY (ID_Personal_Medic) REFERENCES Metge_Metgessa(ID_Personal_Medic),
  FOREIGN KEY (ID_Visita) REFERENCES Visitas_Programadas(ID_Visita)
);

CREATE TABLE Hi_ha2
(
  DNI INT NOT NULL,
  ID_Personal_Medic INT NOT NULL,
  PRIMARY KEY (DNI, ID_Personal_Medic),
  FOREIGN KEY (DNI) REFERENCES Personal(DNI),
  FOREIGN KEY (ID_Personal_Medic) REFERENCES Metge_Metgessa(ID_Personal_Medic)
);

CREATE TABLE Pot_Tenir
(
  Nº_Reserva_Quirofan INT NOT NULL,
  NºQuirofano INT NOT NULL,
  PRIMARY KEY (Nº_Reserva_Quirofan, NºQuirofano),
  FOREIGN KEY (Nº_Reserva_Quirofan) REFERENCES Reserva_Quirofan_(Nº_Reserva_Quirofan),
  FOREIGN KEY (NºQuirofano) REFERENCES Quirofano(NºQuirofano)
);

CREATE TABLE Operaciones
(
  ID_Opereaciones INT NOT NULL,
  Data INT NOT NULL,
  Hora INT NOT NULL,
  Tipus_Operacio INT NOT NULL,
  ID_Personal_Medic INT NOT NULL,
  ID_Paciente INT NOT NULL,
  NºQuirofano INT NOT NULL,
  PRIMARY KEY (ID_Opereaciones),
  FOREIGN KEY (ID_Personal_Medic) REFERENCES Metge_Metgessa(ID_Personal_Medic),
  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente),
  FOREIGN KEY (NºQuirofano) REFERENCES Quirofano(NºQuirofano)
);

CREATE TABLE Personal_Infermeria
(
  ID_Personal_Infermeria INT NOT NULL,
  Estudis INT NOT NULL,
  Curriculum INT NOT NULL,
  ID_Personal_Medic INT NOT NULL,
  ID_Opereaciones INT NOT NULL,
  PRIMARY KEY (ID_Personal_Infermeria),
  FOREIGN KEY (ID_Personal_Medic) REFERENCES Metge_Metgessa(ID_Personal_Medic),
  FOREIGN KEY (ID_Opereaciones) REFERENCES Operaciones(ID_Opereaciones)
);

CREATE TABLE Hi_ha3
(
  DNI INT NOT NULL,
  ID_Personal_Infermeria INT NOT NULL,
  PRIMARY KEY (DNI, ID_Personal_Infermeria),
  FOREIGN KEY (DNI) REFERENCES Personal(DNI),
  FOREIGN KEY (ID_Personal_Infermeria) REFERENCES Personal_Infermeria(ID_Personal_Infermeria)
);

CREATE TABLE Te_Assignat
(
  Nº_Planta INT NOT NULL,
  ID_Personal_Infermeria INT NOT NULL,
  PRIMARY KEY (Nº_Planta, ID_Personal_Infermeria),
  FOREIGN KEY (Nº_Planta) REFERENCES Planta(Nº_Planta),
  FOREIGN KEY (ID_Personal_Infermeria) REFERENCES Personal_Infermeria(ID_Personal_Infermeria)
);
