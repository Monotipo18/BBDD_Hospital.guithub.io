from Funciones_Login import *
import psycopg2
import os
import time
from psycopg2 import sql
from tabulate import tabulate
usuario_BBDD = os.getenv("usuario_BBDD")
contraseña_BBDD = os.getenv("contraseña_BBDD")
hostname_BBDD = os.getenv("hostname_BBDD")
#1
def select_personal_infermeria(usuario, contraseña, DNI):
    '''Te dice si el personal de enfermeria esta asociado a planta o a medico'''
    conn, cur = login(usuario, contraseña)
    if conn and cur:
        try:
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
            if result:
                headers = ["DNI", "Dependencia"]
                print(tabulate(result, headers=headers, tablefmt="fancy_grid"))
            else:
                print("DNI no válido")
        except psycopg2.Error as e:
            print("Error al ejecutar la consulta SQL:", e)
        finally:
            cerrar_bd(conn, cur)
    

#ejemplo de uso
#2
def obtener_operaciones_por_quirofano(usuario, contraseña, fecha):
    '''Selecciona los datos Quirófano,Tipo de Operación, Nombre del Paciente, Hora de la Operación, Médico, Personal de Enfermería i los muestra en una tabla'''
    conn, cur = login(usuario, contraseña)
    if conn and cur:
        try:
            cur.execute( """
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
            """,(fecha,))
            results = cur.fetchall()
            if results:
                headers = [desc[0] for desc in cur.description] 
                print(tabulate(results, headers=headers, tablefmt='fancy_grid'))
            else:
                print("No se encontraron operaciones para la fecha especificada.")
        except psycopg2.Error as e:
            print("Error al ejecutar la consulta SQL:", e)
        finally:
                cerrar_bd(conn, cur)

#3
def obtener_visitas_programadas_por_dia(usuario, contraseña, fecha):
    '''Muestra las visitas programadas para el paciente i el medico que lo atendera'''
    conn, cur = login(usuario, contraseña,fecha)
    if conn and cur:
        try:
            # Sentencia SQL para obtener las visitas programadas por día
            cur.execute("""
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
                """,(fecha,))
            # Obtener los resultados
            results = cur.fetchall()
            # Mostrar los resultados usando tabulate
            if results:
                headers = ["Fecha de la Visita", "Hora de la Visita", "Médico/a", "Paciente"]
                print(tabulate(results, headers=headers, tablefmt="fancy_grid"))
            else:
                print("No hay visitas programadas para la fecha especificada.")   
        except psycopg2.Error as e:
            print("Error al ejecutar la consulta SQL:", e)
        finally:
                cerrar_bd(conn, cur)
#4
def obtener_reservas_por_habitacion(usuario, contraseña, num_habitacion):
    conn, cur = login(usuario, contraseña)
    if conn and cur:
        try:
            # Consulta SQL para obtener las reservas previstas por habitación
            cur.execute("""
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
            """,(num_habitacion,))
            results = cur.fetchall()
            if results:
                headers = ["Fecha de ingreso", "Fecha prevista de salida", "Paciente"]
                print(tabulate(results, headers=headers, tablefmt="fancy_grid"))
            else:
                print("No hay reservas para la habitación", num_habitacion)

        except psycopg2.Error as e:
            print("Error al ejecutar la consulta SQL:", e)
        finally:
            cerrar_bd(conn, cur)
#5
def obtener_informacion_paciente(usuario, contraseña, dni_paciente):
    conn, cur = login(usuario, contraseña)
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
            cerrar_bd(conn, cur)
#6
def obtener_equipos_por_quirofano(usuario, contraseña, num_quirofano=None):
    conn, cur = login(usuario, contraseña)
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
            cerrar_bd(conn, cur)

#7
def obtener_informacion_medico(usuario, contraseña, dni_medico):
    conn, cur = login(usuario, contraseña)
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
            cerrar_bd(conn, cur)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Bloc de consultes i informes

#Donada una planta de l'hospital, saber quantes habitacions, quiròfans i personal d'infermeria té.
#1
def informacion_de_la_planta(usuario, contraseña, planta):
    conn, cur = login(usuario, contraseña)

    if conn and cur:
        try:
            # Consulta numero de quirofanos
            query_quirofanos = """
            SELECT COUNT(num_quirofano) 
            FROM hospital.quirofano 
            JOIN hospital.planta ON planta.num_planta = quirofano.num_planta 
            WHERE planta.num_planta=%s
            """

            # Consulta numero de enfermeras en planta
            query_enfermeras = """
            SELECT COUNT(dni) 
            FROM hospital.personal_infermeria 
            JOIN hospital.planta ON planta.num_planta = personal_infermeria.num_planta 
            WHERE dni_medic IS NULL AND planta.num_planta=%s
            """

            # Consulta Numero de Habitaciones
            query_habitaciones = """
            SELECT COUNT(num_habitacion) 
            FROM hospital.habitacion 
            WHERE num_planta=%s
            """

            # Ejecutar las consultas
            cur.execute(query_quirofanos, (planta,))
            num_quirofanos = cur.fetchone()[0]

            cur.execute(query_enfermeras, (planta,))
            num_enfermeras = cur.fetchone()[0]

            cur.execute(query_habitaciones, (planta,))
            num_habitaciones = cur.fetchone()[0]

            # Tabular los resultados
            resultados = [(num_habitaciones, num_quirofanos, num_enfermeras)]

            # Imprimir los resultados tabulados
            headers = ["Numero De Habitaciones", "Numero de Quirofanos", "Numero de enfermeras Disponibles"]
            print(tabulate(resultados, headers=headers, tablefmt="fancy_grid"))
        except psycopg2.Error as e:
            print("Error al ejecutar la consulta SQL:", e)
        finally:
            cerrar_bd(conn, cur)
#Informe de nombre de visites ateses per dia
#2
def Informe_nombre_visites_ateses(usuario, contraseña):
    '''Totes les visites'''
    conn, cur = login(usuario, contraseña)
    if conn and cur:
        try:
            sql = """
                SELECT
                Fecha,
                COUNT(id_visita) AS Num_Visitas
                FROM
                hospital.Visitas_Programadas
                WHERE
                Ya_Visitat = 'S'
                GROUP BY
                Fecha,Ya_Visitat
                ORDER BY
                Fecha;
            """
            # Ejecutar la consulta SQL
            cur.execute(sql)
            resultados = cur.fetchall()
            
            # Mostrar los resultados en forma tabular si se utiliza la biblioteca tabulate
            if 'tabulate' in globals():
                headers = ["Fecha","Num_Visitas"]
                print(tabulate(resultados, headers=headers, tablefmt="fancy_grid"))
            else:
                for resultado in resultados:
                    print(resultado)

        except psycopg2.Error as e:
            print("Error al ejecutar la consulta SQL:", e)
        finally:
            cerrar_bd(conn, cur)

def Informe_nombre_visites_ateses_per_data(usuario, contraseña, data):
    '''Totes les visites'''
    conn, cur = login(usuario, contraseña)
    if conn and cur:
        try:
            sql = """
                SELECT
                    Fecha,
                    COUNT(id_visita) AS Num_Visitas
                FROM
                    hospital.Visitas_Programadas
                WHERE
                    Ya_Visitat = 'S' AND fecha=%s
                GROUP BY
                    Fecha
                ORDER BY
                    Fecha;
            """
            # Ejecutar la consulta SQL
            cur.execute(sql, (data,))
            resultados = cur.fetchall()
            
            # Mostrar los resultados en forma tabular si se utiliza la biblioteca tabulate
            if 'tabulate' in globals():
                headers = ["Fecha","Num_Visitas"]
                print(tabulate(resultados, headers=headers, tablefmt="fancy_grid"))
            else:
                for resultado in resultados:
                    print(resultado)

        except psycopg2.Error as e:
            print("Error al ejecutar la consulta SQL:", e)
        finally:
            cerrar_bd(conn, cur)
#Data=input("Data: ")
#Informe_nombre_visites_ateses_per_data(Data)
#Informe de tot el personal que treballa a l'hospital
#2
def informe_personal(usuario, contraseña):
    conn, cur = login(usuario, contraseña)
    '''Informe del personal'''
    if conn and cur:
        try:
            sql = """
            SELECT
                P.Nom,
                P.Primer_Cognom,
                P.Segon_Cognom,
                P.Estudis,
                P.tipus_personal,
                E.Nom_Especialitat AS Especialidad
            FROM
                hospital.Personal P
            LEFT JOIN
                hospital.Especialidad E ON P.DNI = E.DNI_Metge;
            """
            # Ejecutar la consulta SQL
            cur.execute(sql)
            resultados = cur.fetchall()
            
            # Mostrar los resultados en forma tabular si se utiliza la biblioteca tabulate
            if 'tabulate' in globals():
                headers = ["Nom","Primer Cognom","Segon Cognom","Estudis","Tipus personal","Especialidad"]
                print(tabulate(resultados, headers=headers, tablefmt="fancy_grid"))
            else:
                for resultado in resultados:
                    print(resultado)

        except psycopg2.Error as e:
            print("Error al ejecutar la consulta SQL:", e)
        finally:
            cerrar_bd(conn, cur)
#3
def Ranking_metges_mes_pacients(usuario, contraseña):
    '''Ranking de metges que atenen més pacients.'''
    conn, cur = login(usuario, contraseña)
    if conn and cur:
        try:
            sql = """
                    SELECT 
                    CONCAT(per.nom,' ',per.primer_cognom,' ', per.segon_cognom) AS Nom_Metge,
                    COUNT(id_paciente) AS Quantitat_Visites
                    FROM
                    hospital.Visitas_Programadas vp
                    JOIN hospital.personal per on per.dni = vp.dni
                    WHERE
                    Ya_Visitat = 'S'
                    GROUP BY
                    per.nom,per.primer_cognom, per.segon_cognom
                    ORDER BY 
                    Quantitat_Visites DESC
            """
            # Ejecutar la consulta SQL
            cur.execute(sql)
            resultados = cur.fetchall()
            
            # Mostrar los resultados en forma tabular si se utiliza la biblioteca tabulate
            if 'tabulate' in globals():
                headers = ["Nom_Metge","Quantitat_Visites"]
                print(tabulate(resultados, headers=headers, tablefmt="fancy_grid"))
            else:
                for resultado in resultados:
                    print(resultado)

        except psycopg2.Error as e:
            print("Error al ejecutar la consulta SQL:", e)
        finally:
            cerrar_bd(conn, cur)
#4
#Malalties més comunes.
def Malalties_mes_comunes(usuario, contraseña):
    conn, cur = login(usuario, contraseña)
    '''Malalties més comunes'''
    if conn and cur:
        try:
            sql = """
                SELECT
                Diagnostic,
                COUNT(diagnostic) AS Diagnostic_mes_comu
                FROM
                hospital.Visitas_Programadas
                GROUP BY
                Diagnostic
                ORDER BY
                Diagnostic_mes_comu DESC;
            """
            # Ejecutar la consulta SQL
            cur.execute(sql)
            resultados = cur.fetchall()
            
            # Mostrar los resultados en forma tabular si se utiliza la biblioteca tabulate
            if 'tabulate' in globals():
                headers = ["Diagnostic","Diagnostic_mes_comu"]
                print(tabulate(resultados, headers=headers, tablefmt="fancy_grid"))
            else:
                for resultado in resultados:
                    print(resultado)

        except psycopg2.Error as e:
            print("Error al ejecutar la consulta SQL:", e)
        finally:
            cerrar_bd(conn, cur)

def vaciar_tablas(usuario, contraseña):
    '''Funcion para vaciar las tablas de toda la BDD'''
    conn, cur = login(usuario, contraseña)
    try:
        sql = """
            TRUNCATE TABLE hospital.paciente CASCADE;
            TRUNCATE TABLE hospital.personal CASCADE;
            TRUNCATE TABLE hospital.metge_metgessa CASCADE;
            TRUNCATE TABLE hospital.planta CASCADE;
            TRUNCATE TABLE hospital.visitas_programadas CASCADE;
            TRUNCATE TABLE hospital.especialidad CASCADE;
            TRUNCATE TABLE hospital.cita_medica CASCADE;
            TRUNCATE TABLE hospital.quirofano CASCADE;
            TRUNCATE TABLE hospital.operaciones CASCADE;
            TRUNCATE TABLE hospital.personal_infermeria CASCADE;
            TRUNCATE TABLE hospital.reserva_quirofano CASCADE;
            TRUNCATE TABLE hospital.habitacion CASCADE;
            TRUNCATE TABLE hospital.reserva_habitacion CASCADE;
            TRUNCATE TABLE hospital.aparells_medics CASCADE;
            TRUNCATE TABLE hospital.agenda_metge CASCADE;
        """
    # Ejecutar la consulta SQL
        cur.execute(sql,)
    except psycopg2.Error as e:
        print("Error al ejecutar la consulta SQL:", e)
    finally:
        cerrar_bd(conn, cur)