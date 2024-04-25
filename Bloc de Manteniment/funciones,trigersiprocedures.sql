--Procedimiento para insertar operaciones programadas

CREATE OR REPLACE PROCEDURE insertar_operacion_programada(
    fecha_operacion DATE,
    hora_operacion TIME,
    tipo_operacion VARCHAR(25),
    id_paciente INT,
    num_quirofano INT,
    dni_medico VARCHAR(9)
)
AS $$
BEGIN
    -- Validar si el paciente existe
    IF NOT EXISTS (SELECT 1 FROM Paciente WHERE ID_Paciente = id_paciente) THEN
        RAISE EXCEPTION 'El paciente con ID % no existe', id_paciente;
    END IF;

    -- Validar si el quirófano existe
    IF NOT EXISTS (SELECT 1 FROM Quirofano WHERE Num_Quirofano = num_quirofano) THEN
        RAISE EXCEPTION 'El quirófano con número % no existe', num_quirofano;
    END IF;

    -- Validar si el médico existe
    IF NOT EXISTS (SELECT 1 FROM Metge_Metgessa WHERE DNI = dni_medico) THEN
        RAISE EXCEPTION 'El médico/a con DNI % no existe', dni_medico;
    END IF;

    -- Insertar la operación programada si pasa las validaciones
    INSERT INTO Operaciones (Data, Hora, Tipus_Operacio, ID_Paciente, Num_Quirofano, DNI_metge)
    VALUES (fecha_operacion, hora_operacion, tipo_operacion, id_paciente, num_quirofano, dni_medico);
END;
$$ LANGUAGE plpgsql;



 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 --Trigger para mantener la integridad de los datos

CREATE OR REPLACE FUNCTION validar_operacion_programada();
RETURNS TRIGGER AS $$
BEGIN
    -- Validar que la fecha de la operación no esté en el pasado
    IF NEW.Data < CURRENT_DATE THEN
        RAISE EXCEPTION 'No se pueden programar operaciones en fechas pasadas';
    END IF;

    -- Validar la disponibilidad del médico/a para la fecha y hora especificadas
    IF NOT EXISTS (
        SELECT 1 FROM Metge_Metgessa 
        WHERE DNI = NEW.DNI_metge 
        AND NOT EXISTS (
            SELECT 1 FROM hospital.operaciones
            WHERE Data = NEW.Data AND Hora = NEW.Hora AND DNI_metge = NEW.DNI_metge
        )
    ) THEN
        RAISE EXCEPTION 'El médico/a no está disponible en la fecha y hora especificadas';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER validar_operacion_programada
BEFORE INSERT OR UPDATE ON hospital.operaciones
FOR EACH ROW
EXECUTE FUNCTION validar_operacion_programada();
-------------------------------------------------------------------------------------------------------------------------aa---------------------------------


--Función para obtener el próximo día hábil

CREATE OR REPLACE FUNCTION proximo_dia_habil(desde_fecha DATE)
RETURNS DATE AS $$
DECLARE
    siguiente_fecha DATE := desde_fecha + INTERVAL '1' DAY;
BEGIN
    -- Iterar hasta encontrar el próximo día hábil
    WHILE EXTRACT(DOW FROM siguiente_fecha) IN (0, 6) LOOP
        siguiente_fecha := siguiente_fecha + INTERVAL '1' DAY;
    END LOOP;

    RETURN siguiente_fecha;
END;
$$ LANGUAGE plpgsql;



