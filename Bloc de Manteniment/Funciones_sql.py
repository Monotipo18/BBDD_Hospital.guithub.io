import psycopg2
import os
import time
from psycopg2 import sql
from tabulate import tabulate
usuario_BBDD = os.getenv("usuario_BBDD")
contraseña_BBDD = os.getenv("contraseña_BBDD")
hostname_BBDD = os.getenv("hostname_BBDD")
def conectar_bd():
    conn = psycopg2.connect(
        dbname="asixhospitalbd",
        user="grupomaviunal",
        password="uN@i3st4fu3rtE",
        host="snakeeater.equemmfoundation.top",
    )
    cur = conn.cursor()
    return conn, cur

def cerrar_bd(conn, cur):
    conn.commit()
    cur.close()
    conn.close()
#1
def select_personal_infermeria(DNI):
    conn, cur = conectar_bd()
    cur.execute("""
        SELECT 
            DNI,
            CASE 
                WHEN DNI_Medic IS NULL THEN 'Personal de planta'
                ELSE 'Depende de un médico/médica'
            END AS Dependencia
        FROM
            hospital.Personal_Infermeria
        WHERE DNI = %s::VARCHAR
    """, (DNI,))
    result = cur.fetchall()  # Fetch all rows
    cerrar_bd(conn, cur)
    if result:
        headers = ["DNI", "Dependencia"]
        print(tabulate(result, headers=headers, tablefmt="fancy_grid"))
    else:
        print("DNI no valido")

#ejemplo de uso
#2
def obtener_operaciones_por_quirofano(fecha):
    conn, cur = conectar_bd()
    sql_query = """
    SELECT 
        q.Num_Quirofano AS "Quirófano",
        o.Tipus_Operacio AS "Tipo de Operación",
        p.Nom AS "Nombre del Paciente",
        o.Hora AS "Hora de la Operación",
        CONCAT(m.NOM, ' ', m.Primer_Cognom) AS "Médico/a",
        CONCAT(i.NOM, ' ', i.Primer_Cognom) AS "Personal de Enfermería"
    FROM 
        hospital.Operaciones o
    INNER JOIN 
        hospital.Quirofano q ON o.Num_Quirofano = q.Num_Quirofano
    INNER JOIN 
        hospital.Metge_Metgessa mm ON o.DNI_metge = mm.DNI
    INNER JOIN 
        hospital.Personal m ON mm.DNI = m.DNI
    INNER JOIN 
        hospital.Paciente p ON o.ID_Paciente = p.ID_Paciente
    INNER JOIN 
        hospital.Personal_Infermeria pi ON o.id_operaciones = pi.id_operaciones
    INNER JOIN 
        hospital.Personal i ON pi.DNI = i.DNI
    WHERE 
        o.Data = %s
    """
    try:
        cur.execute(sql_query, (fecha,))
        rows = cur.fetchall()
        if rows:
            headers = [desc[0] for desc in cur.description] 
            print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))
        else:
            print("No se encontraron operaciones para la fecha especificada.")
    except psycopg2.Error as e:
        print("Error al ejecutar la consulta SQL:", e)
    finally:
        cerrar_bd(conn, cur)


#3
def obtener_visitas_programadas_por_dia(fecha):
    conn, cur = conectar_bd()
    if not conn or not cur:
        return
    
    try:
        # Sentencia SQL para obtener las visitas programadas por día
        sql_query = """
            SELECT 
                v.Fecha AS "Fecha de la Visita",
                v.Hora AS "Hora de la Visita",
                CONCAT(m.NOM, ' ', m.Primer_Cognom) AS "Médico/a",
                CONCAT(p.Nom, ' ', p.Primer_Cognom, ' ', p.Segon_Cognom) AS "Paciente"
            FROM 
                hospital.Visitas_Programadas v
            INNER JOIN 
                hospital.Metge_Metgessa mm ON v.DNI = mm.DNI
            INNER JOIN 
                hospital.Personal m ON mm.DNI = m.DNI
            INNER JOIN 
                hospital.Paciente p ON v.ID_Paciente = p.ID_Paciente
            WHERE 
                v.Fecha = %s
            """
        
        # Ejecutar la consulta SQL
        cur.execute(sql_query, (fecha,))
        
        # Obtener los resultados
        rows = cur.fetchall()
        
        # Mostrar los resultados usando tabulate
        if rows:
            headers = ["Fecha de la Visita", "Hora de la Visita", "Médico/a", "Paciente"]
            print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
        else:
            print("No hay visitas programadas para la fecha especificada.")
            
    except psycopg2.Error as e:
        print("Error al ejecutar la consulta SQL:", e)
    finally:
        # Cerrar la conexión y el cursor
        cerrar_bd(conn, cur)
#4
def obtener_reservas_por_habitacion(num_habitacion):
    conn, cur = conectar_bd()
    if conn and cur:
        try:
            # Consulta SQL para obtener las reservas previstas por habitación
            sql_query = """
                SELECT 
                    rh.Dia_Ingresa,
                    rh.Dia_Sortida,
                    CONCAT(p.Nom, ' ', p.Primer_Cognom, ' ', p.Segon_Cognom) AS paciente
                FROM 
                    hospital.Reserva_Habitacion rh
                INNER JOIN 
                    hospital.Paciente p ON rh.ID_Paciente = p.ID_Paciente
                WHERE 
                    rh.Num_Habitacion = %s;
            """

            # Ejecutar la consulta SQL
            cur.execute(sql_query, (num_habitacion,))
            
            # Obtener los resultados
            rows = cur.fetchall()

            # Mostrar los resultados en forma tabular
            if rows:
                headers = ["Fecha de ingreso", "Fecha prevista de salida", "Paciente"]
                print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
            else:
                print("No hay reservas para la habitación", num_habitacion)

        except psycopg2.Error as e:
            print("Error al ejecutar la consulta SQL:", e)
        finally:
            # Cerrar la conexión y el cursor
            cerrar_bd(conn, cur)
#5
def obtener_informacion_paciente(dni_paciente):
    conn, cur = conectar_bd()
    if conn and cur:
        try:
            # Consulta SQL para obtener las visitas del paciente
            sql_visitas = """
            SELECT 
                Fecha AS "Fecha de la Visita",
                Diagnostic AS "Diagnóstico",
                Medicaments AS "Medicamentos"
            FROM 
                hospital.Visitas_Programadas
            WHERE 
                ID_Paciente = (
                    SELECT ID_Paciente
                    FROM hospital.Paciente
                    WHERE DNI = %s
                );
            """

            # Consulta SQL para obtener los ingresos del paciente
            sql_ingresos = """
                SELECT COUNT(*) 
                FROM hospital.reserva_habitacion
                WHERE ID_Paciente = (
                    SELECT ID_Paciente
                    FROM hospital.paciente
					WHERE DNI = %s
                );
            """

            # Consulta SQL para obtener las operaciones del paciente
            sql_operaciones = """
                SELECT COUNT(*) 
                FROM hospital.Operaciones 
                WHERE ID_Paciente = (
                    SELECT ID_Paciente 
                    FROM hospital.paciente 
                    WHERE DNI = %s
                );
            """

            # Ejecutar las consultas SQL
            cur.execute(sql_visitas, (dni_paciente,))
            visitas = cur.fetchall()

            cur.execute(sql_ingresos, (dni_paciente,))
            ingresos = cur.fetchone()[0]

            cur.execute(sql_operaciones, (dni_paciente,))
            operaciones = cur.fetchone()[0]
            
            # Mostrar los resultados en forma tabular
            print("Visitas:")
            headers = ["Fecha de la Visita", "Diagnóstico", "Medicamentos"]
            print(tabulate(visitas, headers=headers, tablefmt="fancy_grid"))
            
            print("\nIngresos:", ingresos)
            print("Operaciones:", operaciones)

        except psycopg2.Error as e:
            print("Error al ejecutar las consultas SQL:", e)
        finally:
            # Cerrar la conexión y el cursor
            cerrar_bd(conn, cur)
#6
def obtener_equipos_por_quirofano(num_quirofano=None):
    conn, cur = conectar_bd()
    if not conn or not cur:
        return
    
    try:
        # Construir la parte de la consulta SQL condicionalmente
        where_clause = "WHERE q.Num_Quirofano = %s" if num_quirofano else ""
        
        # Consulta SQL para obtener la cantidad de equipos médicos por quirófano
        sql_query = """
            SELECT 
                q.Num_Quirofano AS "Quirófano",
                am.Nom AS "Equipo Médico",
                COUNT(*) AS "Cantidad"
            FROM 
                hospital.Aparells_Medics am
            INNER JOIN 
                hospital.Quirofano q ON am.Num_Quirofano = q.Num_Quirofano
            {}
            GROUP BY 
                q.Num_Quirofano, am.Nom
            ORDER BY 
                q.Num_Quirofano;
        """.format("WHERE q.Num_Quirofano = %s" if num_quirofano else "")

        # Ejecutar la consulta SQL
        cur.execute(sql_query, (num_quirofano,) if num_quirofano else None)
        
        # Obtener los resultados
        equipos_por_quirofano = cur.fetchall()
        
        # Mostrar los resultados en forma tabular

        if not equipos_por_quirofano:
            print("No se encontró información para el número de quirófano proporcionado.")
            return
        else:
            headers = ["Quirófano", "Equipo Médico", "Cantidad"]
            print(tabulate(equipos_por_quirofano, headers=headers, tablefmt="fancy_grid"))
            
    except psycopg2.Error as e:
        print("Error al ejecutar la consulta SQL:", e)
    finally:
        # Cerrar la conexión y el cursor
        cerrar_bd(conn, cur)


#7
def obtener_informacion_medico(dni_medico):
    conn, cur = conectar_bd()
    if conn and cur:
        try:
            # Consulta SQL para obtener las visitas programadas, operaciones programadas y horas disponibles del médico
            sql = """
                SELECT 
                    cm.hora AS hora_cita_medica,
                    vp.hora AS hora_visita,
                    op.hora AS hora_operacion
                FROM hospital.metge_metgessa mm
                LEFT JOIN hospital.cita_medica cm ON mm.dni = cm.dni
                LEFT JOIN hospital.visitas_programadas vp ON mm.dni = vp.dni
                LEFT JOIN hospital.operaciones op ON mm.dni = op.dni_metge
                WHERE mm.dni = %s
                ORDER BY cm.hora;
            """

            # Ejecutar la consulta SQL
            cur.execute(sql, (dni_medico,))
            resultados = cur.fetchall()
            
            # Mostrar los resultados en forma tabular si se utiliza la biblioteca tabulate
            if 'tabulate' in globals():
                headers = ["Hora de la Cita Médica", "Hora de la Visita", "Hora de la Operación"]
                print(tabulate(resultados, headers=headers, tablefmt="fancy_grid"))
            else:
                for resultado in resultados:
                    print(resultado)

        except psycopg2.Error as e:
            print("Error al ejecutar la consulta SQL:", e)
        finally:
            # Cerrar la conexión y el cursor
            cerrar_bd(conn, cur)
