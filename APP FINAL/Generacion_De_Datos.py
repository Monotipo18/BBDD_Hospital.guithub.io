from faker import Faker
import random
import datetime
from datetime import datetime
faker = Faker(['es_ES'])
fakerru = Faker('ru_RU')
#Generaar Informacion de la tabla visites sin insertar en la BBDD
def Generar_Fecha(Numero_Total, Lista):
    '''Función para generar fechas aleatorias'''
    for _ in range(Numero_Total):
        fecha = faker.date_time_this_century()
        fecha=fecha.strftime('%Y-%m-%d')
        Lista.append(fecha)
#Ejemplo

'''Lista_Fecha = []
Generar_Fecha(10, Lista_Fecha)
print(Lista_Fecha[0])'''


def Generar_Caracteres(Numero_Total, lista, caracteres):
    '''Funcion Para Generar los S/N o los H/M'''
    for _ in range(Numero_Total):
        lista.append(random.choice(caracteres))
#Ejemplo
'''
Lista_Nombre = []
Generar_Caracteres(10, Lista_Nombre, ["S", "N"])
print(Lista_Nombre[0])

Lista_Nombre = []
Generar_Caracteres(10, Lista_Nombre, ["H", "M"])
print(Lista_Nombre[0])
'''

def Generar_Numeros(n, lista, inicio=1):
    '''Funcion Para Generar los ID'''
    for i in range(inicio, inicio + n):
        lista.append(i)

#Ejemplo
'''
Lista_Numeros = []
Generar_Numeros(10, Lista_Numeros, inicio=1)
print(Lista_Numeros)
'''
def Generar_Diagnosticos(Numero_Total,Lista):
    '''Genera el tipo de diagnostico'''
    diagnosticos_medicos = [ "Resfriado común", "Gripe", "Fiebre tifoidea", "Neumonía", "Bronquitis aguda", "Asma", "Infección del tracto urinario", "Cistitis", "Pielonefritis", "Gastritis", "Úlcera péptica", "Pancreatitis aguda", "Hepatitis viral", "Colecistitis aguda", "Gastroenteritis", "Apendicitis", "Diverticulitis", "Colitis ulcerosa", "Enfermedad de Crohn", "Hemorroides", "Cáncer de colon", "Cáncer de estómago", "Cáncer de páncreas", "Cáncer de hígado", "Cáncer de riñón", "Cáncer de vejiga", "Cáncer de próstata", "Cáncer de pulmón", "Cáncer de mama", "Cáncer de útero", "Cáncer de ovario", "Cáncer de cuello uterino", "Cáncer de tiroides", "Cáncer de piel", "Leucemia", "Linfoma", "Mieloma múltiple", "Anemia ferropénica", "Anemia perniciosa", "Leucemia mieloide aguda", "Leucemia mieloide crónica", "Leucemia linfoblástica aguda", "Leucemia linfoblástica crónica", "Leucemia mielomonocítica crónica", "Leucemia promielocítica aguda", "Linfoma de Hodgkin", "Linfoma no Hodgkin", "Mielofibrosis", "Mielodisplasia", "Síndrome mielodisplásico", "Síndrome mieloproliferativo", "Síndrome linfoproliferativo", "Síndrome de Lynch", "Síndrome de Cushing", "Síndrome de Marfan", "Síndrome de Turner", "Síndrome de Down", "Síndrome de Edwards", "Síndrome de Patau", "Síndrome de Klinefelter", "Síndrome de X frágil", "Síndrome de Rett", "Síndrome de Alport", "Síndrome de Bartter", "Síndrome nefrótico", "Síndrome hemolítico urémico", "Síndrome de Brugada", "Síndrome de QT largo", "Síndrome de Wolff-Parkinson-White", "Síndrome de Marfan", "Síndrome de Ehlers-Danlos", "Síndrome de Williams", "Síndrome de Tourette", "Síndrome de Asperger", "Síndrome de Rett", "Síndrome de Turner", "Síndrome de Klinefelter", "Síndrome de X frágil", "Síndrome de Prader-Willi", "Síndrome de Angelman", "Síndrome de Leigh", "Síndrome de Lesch-Nyhan", "Síndrome de Hunter", "Síndrome de Sanfilippo", "Síndrome de Hurler", "Síndrome de Morquio", "Síndrome de Gaucher", "Síndrome de Tay-Sachs", "Síndrome de Niemann-Pick", "Síndrome de Krabbe", "Síndrome de Fabry", "Síndrome de Pompe", "Síndrome de Wolman", "Síndrome de Goodpasture", "Síndrome de Behçet", "Síndrome de Churg-Strauss", "Síndrome de Takayasu", "Síndrome de Kawasaki", "Síndrome de Raynaud", "Síndrome de Sjögren", "Síndrome de Hughes-Stovin", "Síndrome de Sweet", "Síndrome de Gianotti-Crosti", "Síndrome de Aase-Smith", "Síndrome de Adams-Oliver", "Síndrome de Apert", "Síndrome de Bardet-Biedl", "Síndrome de Beckwith-Wiedemann", "Síndrome de Bloom", "Síndrome de Cockayne", "Síndrome de Coffin-Lowry", "Síndrome de DiGeorge", "Síndrome de Dubowitz", "Síndrome de Gardner", "Síndrome de Goldenhar", "Síndrome de Gorlin", "Síndrome de Joubert", "Síndrome de Kabuki", "Síndrome de Klippel-Trénaunay", "Síndrome de Larsen", "Síndrome de Laron", "Síndrome de Li-Fraumeni", "Síndrome de Meckel", "Síndrome de Meigs", "Síndrome de Mobius", "Síndrome de Mowat-Wilson", "Síndrome de Nail-Patella", "Síndrome de Pallister-Hall", "Síndrome de Poland", "Síndrome de Prune Belly", "Síndrome de Roberts", "Síndrome de Rothmund-Thomson", "Síndrome de Rubinstein-Taybi", "Síndrome de Sturge-Weber", "Síndrome de Treacher Collins", "Síndrome de VACTERL", "Síndrome de Waardenburg", "Síndrome de Walker-Warburg", "Síndrome de Werner", "Síndrome de Wiskott-Aldrich", "Síndrome de Zellweger", "Síndrome de Zollinger-Ellison", "Síndrome de Zieve", "Síndrome de Alagille", "Síndrome de deleción 22q11.2", "Síndrome de Goldenhar", "Síndrome de Joubert", "Síndrome de Klippel-Feil", "Síndrome de Möbius", "Síndrome de Poland", "Síndrome de Rubinstein-Taybi", "Síndrome de Treacher Collins", "Síndrome de Williams", "Síndrome de Aicardi", "Síndrome de Axenfeld-Rieger", "Síndrome de Dandy-Walker", "Síndrome de Donohue", "Síndrome de Hallermann-Streiff", "Síndrome de Jervell y Lange-Nielsen", "Síndrome de Joubert", "Síndrome de Kartagener", "Síndrome de Leigh", "Síndrome de Mayer-Rokitansky-Küster-Hauser", "Síndrome de Noonan", "Síndrome de Pendred", "Síndrome de Poland", "Síndrome de Prader-Willi", "Síndrome de Prune Belly", "Síndrome de Russell-Silver", "Síndrome de Stickler", "Síndrome de Treacher Collins", "Síndrome de Turner", "Síndrome de VATER", "Síndrome de Waardenburg", "Síndrome de Wolf-Hirschhorn", "Síndrome de WAGR", "Síndrome de Williams", "Síndrome de X frágil", "Síndrome de Young", "Síndrome de Zellweger", "Síndrome de Androgen Insensitivity", "Síndrome de Bardet-Biedl", "Síndrome de Bloom", "Síndrome de Cockayne", "Síndrome de Coffin-Lowry", "Síndrome de Cornelia de Lange", "Síndrome de Goldenhar", "Síndrome de Kabuki", "Síndrome de Klippel-Feil", "Síndrome de Larsen", "Síndrome de Marfan", "Síndrome de Rett", "Síndrome de Rubinstein-Taybi", "Síndrome de Stickler", "Síndrome de Treacher Collins", "Síndrome de Turner", "Síndrome de Williams", "Síndrome de Wolf-Hirschhorn", "Síndrome de Zellweger", "Síndrome de Zieve", "Síndrome de Alagille", "Síndrome de Berardinelli-Seip", "Síndrome de Charcot-Marie-Tooth", "Síndrome de Cronkhite-Canada", "Síndrome de Gilbert", "Síndrome de Kartagener", "Síndrome de McCune-Albright", "Síndrome de Moebius", "Síndrome de Pendred", "Síndrome de Schinzel-Giedion", "Síndrome de Zollinger-Ellison", "Síndrome de Cotard", "Síndrome de Couvade", "Síndrome de Felty", "Síndrome de Heerfordt", "Síndrome de Münchhausen", "Síndrome de Polonia", "Síndrome de Rapunzel", "Síndrome de Stendhal", "Síndrome de Cotard", "Síndrome de Felty", "Síndrome de Heerfordt", "Síndrome de Münchhausen", "Síndrome de Polonia", "Síndrome de Rapunzel", "Síndrome de Stendhal", "Síndrome de Alice in Wonderland", "Síndrome de Capgras", "Síndrome de Cotard", "Síndrome de Frégoli", "Síndrome de Ganser", "Síndrome de Koro", "Síndrome de París", "Síndrome de Stendhal", "Síndrome de Berlín", "Síndrome de París", "Síndrome de Estocolmo", "Síndrome de Lima", "Síndrome de Jerusalén", "Síndrome de Florencia", "Síndrome de París", "Síndrome de Estocolmo", "Síndrome de Lima", "Síndrome de Jerusalén", "Síndrome de Florencia", "Síndrome de París", "Síndrome de Estocolmo", "Síndrome de Lima", "Síndrome de Jerusalén", "Síndrome de Florencia", "Síndrome de París", "Síndrome de Estocolmo", "Síndrome de Lima", "Síndrome de Jerusalén", "Síndrome de Florencia", "Síndrome de París", "Síndrome de Estocolmo", "Síndrome de Lima", "Síndrome de Jerusalén", "Síndrome de Florencia", "Síndrome de París", "Síndrome de Estocolmo", "Síndrome de Lima", "Síndrome de Jerusalén", "Síndrome de Florencia", "Síndrome de París", "Síndrome de Estocolmo", "Síndrome de Lima", "Síndrome de Jerusalén", "Síndrome de Florencia", "Síndrome de París", "Síndrome de Estocolmo", "Síndrome de Lima", "Síndrome de Jerusalén", "Síndrome de Florencia", "Síndrome de París", "Síndrome de Estocolmo", "Síndrome de Lima", "Síndrome de Jerusalén", "Síndrome de Florencia", "Síndrome de París", "Síndrome de Estocolmo", "Síndrome de Lima", "Síndrome de Jerusalén", "Síndrome de Florencia"]
    for _ in range(Numero_Total):
        Estudio_Aleatorio=random.choice(diagnosticos_medicos)
        Lista.append(Estudio_Aleatorio)
#Ejemplo
'''
Lista_Diagnosticos=[]
Generar_Diagnosticos(10,Lista_Diagnosticos)
print(Lista_Diagnosticos)
'''
def Generar_Medicamientos(Numero_Total,Lista):
    '''Funcion para generar el tipo de medicamento rezetado aleatoriamente'''
    medicamentos = [ "Paracetamol", "Ibuprofeno", "Aspirina", "Amoxicilina", "Omeprazol", "Metformina", "Simvastatina", "Atorvastatina", "Losartán", "Levotiroxina", "Warfarina", "Captopril", "Hidroclorotiazida", "Furosemida", "Metoprolol", "Lorazepam", "Metronidazol", "Diazepam", "Clonazepam", "Amitriptilina", "Tramadol", "Citalopram", "Atenolol", "Fluoxetina", "Lisinopril", "Alprazolam", "Duloxetina", "Escitalopram", "Risperidona", "Ranitidina", "Bisoprolol", "Amiodarona", "Sildenafil", "Acetaminofén", "Clopidogrel", "Dapagliflozina", "Rosuvastatina", "Carvedilol", "Fenobarbital", "Doxiciclina", "Diltiazem", "Venlafaxina", "Pioglitazona", "Mirtazapina", "Valsartán", "Naproxeno", "Metoclopramida", "Pantoprazol", "Ciprofloxacino", "Amoxicilina / Ácido clavulánico", "Fluconazol", "Clonidina", "Acenocumarol", "Hidroxicloroquina", "Esomeprazol", "Prednisona", "Allopurinol", "Ezetimiba", "Fenitoína", "Budesonida", "Fosinopril", "Levothyroxine", "Fentanyl", "Gabapentina", "Lamotrigina", "Levofloxacino", "Nortriptilina", "Olmesartán", "Rifaximina", "Sulfametoxazol / Trimetoprima", "Tadalafilo", "Telmisartán", "Tioridazina", "Verapamilo", "Alendronato", "Amitriptilina", "Amlodipino", "Amoxicilina", "Aspirina", "Atenolol", "Atorvastatina", "Azitromicina", "Bromazepam", "Buspirona", "Candesartán", "Carbamazepina", "Carvedilol", "Ciprofloxacino", "Clonazepam", "Clopidogrel", "Dexametasona", "Diclofenaco", "Enalapril", "Escitalopram", "Esomeprazol", "Fluconazol", "Fluoxetina", "Furosemida", "Hidroclorotiazida", "Ibuprofeno", "Insulina", "Lansoprazol", "Levotiroxina", "Losartán", "Meloxicam", "Metformina", "Metoprolol", "Naproxeno", "Olanzapina", "Omeprazol", "Paracetamol", "Pregabalina", "Propranolol", "Quetiapina", "Ramipril", "Ranitidina", "Risperidona", "Rosuvastatina", "Sertralina", "Simvastatina", "Telmisartán", "Tramadol", "Trimebutina", "Valsartán", "Venlafaxina", "Zolpidem", "Ácido acetilsalicílico", "Ácido valproico", "Alprazolam", "Amlodipino", "Amoxicilina", "Atenolol", "Azitromicina", "Captopril", "Carbamazepina", "Clonazepam", "Clopidogrel", "Diclofenaco", "Enalapril", "Fluoxetina", "Furosemida", "Glibenclamida", "Hidroclorotiazida", "Insulina", "Ibuprofeno", "Lansoprazol", "Levotiroxina", "Losartán", "Metformina", "Metoprolol", "Naproxeno", "Omeprazol", "Paracetamol", "Prednisona", "Quetiapina", "Ramipril", "Ranitidina", "Rosuvastatina", "Sertralina", "Simvastatina", "Telmisartán", "Tramadol", "Valsartán", "Venlafaxina", "Vitamina C", "Vitamina D", "Zolpidem", "Amoxicilina", "Atorvastatina", "Azitromicina", "Carvedilol", "Ciprofloxacino", "Clonazepam", "Clonidina", "Clobazam", "Diazepam", "Digoxina", "Diltiazem", "Donepezilo", "Enoxaparina", "Ezetimiba", "Fenitoína", "Finasterida", "Furosemida", "Gemfibrozilo", "Gliclazida", "Hidroclorotiazida", "Isotretinoína", "Levocetirizina", "Levetiracetam", "Lisinopril", "Lorazepam", "Metildopa", "Metronidazol", "Minoxidil", "Naproxeno", "Olanzapina", "Omeprazol", "Paracetamol", "Perindopril", "Piroxicam", "Pravastatina", "Prednisona", "Quetiapina", "Ramipril", "Ranitidina", "Risperidona", "Rivaroxabán", "Rosuvastatina", "Sertralina", "Sildenafil", "Simeprevir", "Tacrolimus", "Tamoxifeno", "Telmisartán", "Tenofovir", "Tolbutamida", "Torasemida", "Tramadol", "Valsartán", "Vareniclina", "Vildagliptina", "Vitamina B12", "Vitamina D", "Warfarina", "Zidovudina", "Zolpidem", "Ácido acetilsalicílico", "Ácido fólico", "Ácido valproico", "Acitretina", "Alendronato", "Alprazolam", "Amantadina", "Anastrozol", "Atenolol", "Atorvastatina", "Baclofeno", "Beclometasona", "Betametasona", "Bisoprolol", "Bromazepam", "Budesonida", "Bupropión", "Buspirona", "Calcitriol", "Carbamazepina", "Carvedilol", "Cefalexina", "Cetirizina", "Ciprofloxacino", "Clindamicina", "Clopidogrel", "Clonazepam", "Clozapina", "Codeína", "Colchicina", "Desvenlafaxina", "Dexametasona", "Diazepam", "Diclofenaco", "Diltiazem", "Dipirona", "Donepezilo", "Doxorrubicina", "Duloxetina", "Enalapril", "Escitalopram", "Esomeprazol", "Estriol", "Estrógenos", "Etinilestradiol", "Exemestano", "Famotidina", "Febuxostat", "Fenobarbital", "Fentermina", "Fexofenadina", "Finasterida", "Fluconazol", "Fluoxetina", "Fosfomicina", "Gabapentina", "Galantamina", "Glatiramer", "Glimepirida", "Gluconato de calcio", "Gluconato de potasio", "Gluconato de zinc", "Guanfacina", "Haloperidol", "Heparina", "Hidroclorotiazida", "Hidrocortisona", "Hidróxido de aluminio", "Hidroxocobalamina", "Ibuprofeno", "Imatinib", "Insulina", "Ipratropio", "Irbesartán", "Isotretinoína", "Labetalol", "Lamotrigina", "Lansoprazol", "Latanoprost", "Letrozol", "Levocetirizina", "Levodopa", "Levofloxacino", "Levotiroxina", "Lidocaína", "Lisinopril", "Loperamida", "Loratadina", "Losartán", "Lovastatina", "Meloxicam", "Memantina", "Meprobamato", "Metformina", "Metilfenidato", "Metoclopramida", "Metoprolol", "Miconazol", "Midazolam", "Mirtazapina", "Misoprostol", "Montelukast", "Morfina", "Naproxeno", "Nebivolol", "Neostigmina", "Niacina", "Nifedipino", "Nitrofurantoína", "Nitroglicerina", "Olanzapina", "Omeprazol", "Ondansetrón", "Orlistat", "Oseltamivir", "Oxitocina", "Oxígeno", "Oxicodona", "Oximetazolina", "Pantoprazol", "Paracetamol", "Paroxetina", "Penicilina", "Permetrina", "Piracetam", "Piridostigmina", "Pramipexol", "Pravastatina", "Pregabalina", "Primidona", "Proclorperazina", "Progesterona", "Propafenona", "Propiltiouracilo", "Propranolol", "Quetiapina", "Quinapril", "Raloxifeno", "Ramipril", "Ranitidina", "Repaglinida", "Reserpina", "Rifaximina", "Risperidona", "Rituximab", "Rivaroxabán", "Ropinirol", "Rosuvastatina", "Salbutamol", "Salmeterol", "Selegilina", "Sertralina", "Sildenafilo", "Simvastatina", "Sitagliptina", "Tacrolimus", "Tamoxifeno", "Tamsulosina", "Telmisartán", "Terazosina", "Tetraciclinas", "Tiamina", "Tiotropio", "Tolterodina", "Torasemida", "Tramadol", "Travoprost", "Trazodona", "Triamcinolona", "Triazolam", "Trifluoperazina", "Trimebutina", "Trimetazidina", "Valaciclovir", "Valsartán", "Vareniclina", "Venlafaxina", "Vildagliptina", "Vitamina B12", "Vitamina D", "Voriconazol", "Warfarina", "Zaleplon", "Zidovudina", "Zolpidem", "Zolmitriptán", "Zopiclona" ]
    for _ in range(Numero_Total):
        medicamento_Aleatorio=random.choice(medicamentos)
        Lista.append(medicamento_Aleatorio)

#Ejemplo
'''
Lista_Medicamento=[]
Generar_Medicamientos(10,Lista_Medicamento)
print(Lista_Medicamento)
'''

def Generar_Hora(Numero_Total, Lista): 
    '''Funcion para generar horas de visita'''   
    for _ in range(Numero_Total):
        hora = faker.time(pattern="%H:%M:%S")
        Lista.append(hora)

# Ejemplo
'''
lista_de_fechas = []
Generar_Fecha(10, lista_de_fechas)
print("Lista de fechas generadas:", lista_de_fechas)
'''

def generar_dos_fechas_en_rango(Numero_Total, Lista1, Lista2):
    fecha_inicio = datetime.strptime("1983-01-01", "%Y-%m-%d")
    fecha_fin = datetime.strptime("2026-11-13", "%Y-%m-%d")
    for _ in range(Numero_Total):
        fecha_1 = faker.date_time_between_dates(datetime_start=fecha_inicio, datetime_end=fecha_fin).date()
        fecha_2 = faker.date_time_between_dates(datetime_start=fecha_inicio, datetime_end=fecha_fin).date()
        Lista1.append(fecha_1)
        Lista2.append(fecha_2)

#Generar Informacion de la tabla Paciente sin insertar en la BBDD

def generar_dni(Numero_Total, Lista):
    '''Funcion para generar los DNI'''
    while len(Lista) < Numero_Total:
        dni_numeros = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        dni_letra = letras[int(dni_numeros) % 23]
        dni = dni_numeros + dni_letra
        if dni not in Lista:
            Lista.append(dni)

#Ejemplo
'''
Lista_DNI = []
generar_dni(10, Lista_DNI)
print(Lista_DNI)
'''


def Generar_Nombre(Numero_Total,Lista):
    '''Funcion para generar los Nombres'''
    for _ in range(Numero_Total):
        Generar_Nombre = faker.first_name()
        Lista.append(Generar_Nombre)
#Ejemplo
'''
Lista_Nombre = []
Generar_Nombre(10, Lista_Nombre)
print(Lista_Nombre)
'''

def Generar_Cognom(Numero_Total,Lista):
    '''Funcion para generar los apellidos'''
    for _ in range(Numero_Total):
        Generar_Cognom = faker.last_name()
        Lista.append(Generar_Cognom)    
'''
Lista_Cognom = []
Generar_Cognom(10, Lista_Cognom)
print(Lista_Cognom)
'''
def generar_dni(Numero_Total, Lista):
    '''Funcion Para generar los DNI'''
    for _ in range(Numero_Total):
        dni_numeros = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        dni_letra = letras[int(dni_numeros) % 23]
        Lista.append(dni_numeros + dni_letra)

# Ejemplo 
'''
Lista_Nombre = []
generar_dni(10, Lista_Nombre)
print(Lista_Nombre[1])
'''

def generar_tarjeta_sanitaria_catalana(cantidad, lista, lista_cognom, lista_cognom2, lista_sexe, lista_fecha):
    '''Genera una lista de números de tarjeta sanitaria catalana ficticios'''
    for i in range(cantidad):
        # Obtener los valores correspondientes al índice actual
        cognom = lista_cognom[i].upper()[:2]
        cognom2 = lista_cognom2[i].upper()[:2]
        sexe = "0" if lista_sexe[i] == "H" else "1"
        fecha = str(lista_fecha[i])  # Convertir la fecha a cadena

        # Quitar los segundos de la fecha
        fecha = fecha[:-3]

        # Generar los 3 últimos dígitos de manera aleatoria
        ultimos_tres_digitos = '{:03d}'.format(random.randint(0, 999))

        # Combinar todos los elementos en el número de tarjeta sanitaria
        numero_tarjeta_sanitaria = f'{cognom}{cognom2}{sexe}{fecha}{ultimos_tres_digitos}'

        lista.append(numero_tarjeta_sanitaria)



def Generar_Tlf(cantidad, lista):
    '''Genera una lista de números de teléfono móviles españoles ficticios sin prefijo ni espacios'''
    faker = Faker('es_ES')  # Establecer la localización a España
    for _ in range(cantidad):
        numero_telefono = faker.phone_number()
        numero_sin_prefijo = numero_telefono.split('+34')[-1].replace(" ", "")
        numero_sin_prefijo = numero_sin_prefijo[:9]
        lista.append(numero_sin_prefijo)


# Ejemplo
'''
lista_telefonos_españoles = []
Generar_Tlf(10, lista_telefonos_españoles)
print(lista_telefonos_españoles)
'''
def Generar_correo_electronico(Numero_Total, Lista):
    '''Función para generar correos electrónicos'''
    for _ in range(Numero_Total):
        correo = faker.free_email()
        Lista.append(correo)
#Ejemplo
'''
Lista_correo_electronico = []
Generar_correo_electronico(10, Lista_correo_electronico)
print(Lista_correo_electronico)
'''
def Generar_Especialidad(Numero_Total, Lista):
    '''Función para generar especialidades médicas'''
    especialidades_medicas = ["Medicina Interna", "Cirugía General", "Pediatría", "Ginecología y Obstetricia", "Cardiología", "Dermatología", "Neurología", "Psiquiatría", "Oftalmología", "Otorrinolaringología", "Traumatología y Ortopedia", "Urología", "Endocrinología", "Oncología", "Radiología", "Anestesiología", "Medicina Familiar y Comunitaria", "Medicina de Emergencia", "Nefrología", "Hematología", "Infectología", "Reumatología", "Geriatría", "Medicina Deportiva", "Medicina del Trabajo", "Medicina Intensiva", "Nutriología", "Gastroenterología", "Neumología", "Hematología", "Oncología Médica", "Neurocirugía", "Cirugía Plástica, Estética y Reparadora", "Cirugía Vascular", "Cirugía Torácica", "Cirugía Cardiovascular", "Cirugía Oral y Maxilofacial", "Medicina Nuclear", "Patología", "Anatomía Patológica", "Farmacología Clínica", "Farmacología Básica", "Genética Médica", "Medicina del Dolor", "Medicina Legal y Forense", "Toxicología", "Inmunología", "Epidemiología", "Medicina Tropical", "Medicina de Urgencias", "Telemedicina", "Salud Pública", "Medicina Aeroespacial", "Medicina del Sueño", "Medicina de Rehabilitación", "Fisiatría", "Cuidados Paliativos", "Alergología", "Psicología Clínica", "Psicoterapia", "Fisiología", "Histología", "Embriología", "Microbiología", "Parasitología", "Virología", "Andrología", "Angiología", "Bioquímica Clínica", "Cirugía Cardiotorácica", "Cirugía Cráneo-Maxilofacial", "Cirugía de Mano", "Cirugía Gastrointestinal", "Cirugía Hepatobiliar", "Cirugía Pediátrica", "Cirugía Plástica Pediátrica", "Cirugía Reconstructiva", "Cirugía Tumoral", "Coloproctología", "Ecocardiografía", "Ecografía", "Electrofisiología", "Endocrinología Pediátrica", "Endoscopia Digestiva", "Endoscopia Respiratoria", "Epidemiología Clínica", "Flebología", "Foniatria", "Gastroenterología Pediátrica", "Gastrointestinal", "Ginecología Oncológica", "Hemato-Oncología Pediátrica", "Hepatología", "Imagen Cardiovascular", "Infecciones de Transmisión Sexual", "Inmunohematología", "Inmunoterapia", "Intervencionismo Cardiovascular", "Intervencionismo Neurovascular", "Litotripsia", "Mastología", "Medicina Antienvejecimiento", "Medicina del Tráfico", "Medicina del Viajero", "Medicina Fetal", "Medicina Hiperbárica", "Medicina Ocupacional", "Medicina Psicosomática", "Medicina Reproductiva", "Nefrología Pediátrica", "Neonatología", "Neurocirugía Pediátrica", "Neuroendocrinología", "Neurofisiología Clínica", "Neurología Pediátrica", "Neurorradiología", "Neurorrehabilitación", "Neurosonología", "Neuroterapia", "Nutrición Clínica", "Obstetricia Oncológica", "Oftalmología Pediátrica", "Oncología Radioterápica", "Ortodoncia", "Ortopedia Pediátrica", "Ozonoterapia", "Paliativos Pediátricos", "Parasitología Clínica", "Patología Clínica", "Pediatría del Desarrollo y la Conducta", "Pediatría Hospitalaria", "Periodoncia", "Proctología", "Protesis", "Psicología Infantil", "Psiconeuroinmunología", "Psicopedagogía", "Radiocirugía", "Radiología Intervencionista", "Radioterapia", "Reconstrucción Mamaria", "Rehabilitación Pediátrica", "Reproducción Asistida", "Resonancia Magnética Nuclear", "Retinología", "Reumatología Pediátrica", "Semiología", "Sexología", "Terapia Celular", "Terapia Génica", "Terapia Regenerativa", "Terapia Sexual", "Terapia Vascular", "Toxicología Clínica", "Toxicología Forense", "Toxicología Pediátrica", "Trasplantes", "Tricología", "Tumores Cerebrales", "Urgencias Pediátricas", "Urodinamia", "Uropediatría", "Virología Clínica", "Vulvovaginología"]
    for _ in range(Numero_Total):
        especialidad_aleatoria = random.choice(especialidades_medicas)
        Lista.append(especialidad_aleatoria)
#Ejemplo
'''
Lista_Especilidad = []
Generar_Especialidad(10, Lista_Especilidad)
print(Lista_Especilidad)
'''
def Generar_Tipo_Operacion(Numero_Total,Lista):
    '''Funcion que generarà el tipo de operacion que recibe el paciente'''
    nombres_operaciones = [ "Apendicectomía", "Artroscopia", "Cesárea", "Colecistectomía", "Colonoscopia", "Cirugía cardíaca", "Cirugía de bypass gástrico", "Cirugía de columna vertebral", "Cirugía de cataratas", "Cirugía de hernia", "Cirugía de labio leporino", "Cirugía de oído", "Cirugía de rodilla", "Cirugía de senos paranasales", "Cirugía de tiroides", "Cirugía de trasplante de órganos", "Cirugía de válvula cardíaca", "Cirugía estética", "Cirugía laparoscópica", "Cirugía ortopédica", "Cirugía plástica", "Cirugía vascular", "Cirugía maxilofacial", "Colectomía", "Colostomía", "Corrección de astigmatismo", "Corrección de estrabismo", "Dilatación y curetaje (D&C)", "Endoscopia", "Esofagectomía", "Esplenectomía", "Extracción de cálculos biliares", "Extracción de cataratas", "Extracción de implantes mamarios", "Flebectomía", "Gastrectomía", "Hemicolectomía", "Hemorroidectomía", "Histerectomía", "Injerto de piel", "Laminectomía", "Laparotomía", "Laringectomía", "Liposucción", "Litotricia", "Mamoplastia", "Mastopectomía", "Neurocirugía", "Ooforectomía", "Orquiectomía", "Otoplastia", "Pancreatectomía", "Plastia de reparación de hernia inguinal", "Prostatectomía", "Quimioterapia", "Radioterapia", "Reemplazo de cadera", "Reemplazo de rodilla", "Reparación de aneurisma", "Reparación de hernia", "Resección de tumor cerebral", "Rinoplastia", "Septoplastia", "Timpanoplastia", "Tonsilectomía", "Transplante de corazón", "Transplante de hígado", "Transplante de médula ósea", "Transplante de páncreas", "Vasectomía", "Ventriculostomía", "Vulvectomía", "Amniocentesis", "Angioplastia", "Artroplastia", "Biopsia de mama", "Biopsia de próstata", "Blefaroplastia", "Broncoscopia", "Circuncisión", "Colangiopancreatografía retrógrada endoscópica (CPRE)", "Cordotomía", "Corrección de pie zambo", "Descompresión de disco", "Endarterectomía", "Endodoncia", "Endoscopia gastrointestinal", "Exéresis de tumor", "Fistulotomía", "Gastropexia", "Ginecomastia", "Implante coclear", "Implante dental", "Implante de marcapasos", "Implante de stent", "Implante de válvula cardíaca", "Implante mamario", "Inseminación artificial", "Laparoscopia diagnóstica", "Laparoscopia exploratoria", "Laparoscopia terapéutica", "Limpieza dental", "Mastoidectomía", "Nefrectomía", "Ooforoplastia", "Ortognática cirugía", "Osteotomía", "Polisomnografía", "Proctocolectomía", "Reparación de ligamento cruzado", "Reparación de rotura del manguito de los rotadores", "Rizotomía", "Sigmoidectomía", "Tallectomía", "Tenolisis", "Tonsillectomy", "Trasplante de córnea", "Trasplante de riñón", "Trombectomía", "Tuboplastia", "Ureteroscopia", "Uretroplastia", "Varicocelectomía", "Vasovasostomía", "Ventilación pulmonar", "Vitrectomía", "Vulvoplastia", "Whipple Procedure", "Reparación de fístula anal", "Reparación de hernia ventral", "Reparación de hernia umbilical", "Reparación de hernia inguinal", "Reparación de hernia incisional", "Reparación de hernia epigástrica", "Reparación de hernia femoral", "Reparación de hernia hiatal", "Reparación de hernia lumbar", "Reparación de hernia paraesofágica", "Reparación de hernia paraumbilical", "Reparación de hernia perineal", "Reparación de hernia póstero-lateral", "Reparación de hernia suprapúbica", "Reparación de hernia umbilical congénita", "Reparación de hernia ventral gigante", "Reparación de hernia ventral recurrente", "Reparación de hernia ventral subcostal", "Reparación de hernia ventral supraumbilical", "Reparación de hernia ventral suprapúbica", "Reparación de hernia ventral trasplante de órgano", "Reparación de hernia ventral trasplante renal", "Reparación de hernia ventral trasplante hepático", "Reparación de hernia ventral trasplante intestinal", "Reparación de hernia ventral trasplante cardiaco", "Reparación de hernia ventral trasplante pulmonar", "Reparación de hernia ventral trasplante pancreático", "Reparación de hernia ventral trasplante intestinal multivisceral", "Reparación de hernia ventral trasplante hepatopancreatobiliar", "Reparación de hernia ventral trasplante cardiopulmonar", "Reparación de hernia ventral trasplante renohepático", "Reparación de hernia ventral trasplante cardiorenal", "Reparación de hernia ventral trasplante renopancreático", "Reparación de hernia ventral trasplante cardiorrenal", "Reparación de hernia ventral trasplante pulmonorenal", "Reparación de hernia ventral trasplante pancreorrenal", "Reparación de hernia ventral trasplante hepatorrenal", "Reparación de hernia ventral trasplante multivisceral", "Reparación de hernia ventral trasplante total", "Reparación de hernia ventral trasplante de órganos sólidos", "Reparación de hernia ventral trasplante de tejidos", "Reparación de hernia ventral trasplante de médula ósea", "Reparación de hernia ventral trasplante de células madre", "Reparación de hernia ventral trasplante de sangre", "Reparación de hernia ventral trasplante de plasma", "Reparación de hernia ventral trasplante de plaquetas", "Reparación de hernia ventral trasplante de leucocitos", "Reparación de hernia ventral trasplante de linfocitos", "Reparación de hernia ventral trasplante de órganos y tejidos", "Reparación de hernia ventral trasplante de sangre y componentes", "Reparación de hernia ventral trasplante de células y tejidos", "Reparación de hernia ventral trasplante de médula y órganos", "Reparación de hernia ventral trasplante de médula y tejidos", "Reparación de hernia ventral trasplante de células y órganos", "Reparación de hernia"]
    for _ in range(Numero_Total):
        nombres_operaciones_aletoria = random.choice(nombres_operaciones)
        Lista.append(nombres_operaciones_aletoria)
#Ejemplo
'''
Lista_Tipo_Operacion = []
Generar_Tipo_Operacion(10, Lista_Tipo_Operacion)
print(Lista_Tipo_Operacion)
'''

def Generar_Aparell_Medico(Numero_Total,Lista):
    '''Funcion que genera el tipo de aparato medico que hay en el quirofano'''
    aparatos_medicos = [ "Respirador", "Electrocardiograma (ECG)", "Tomografía computarizada (TC)", "Resonancia magnética (RM)", "Máquina de anestesia", "Monitor de signos vitales", "Desfibrilador", "Endoscopio", "Microscopio", "Láser quirúrgico", "Incubadora", "Bomba de infusión", "Ventilador", "Laringoscopio", "Oxímetro de pulso", "Máquina de hemodiálisis", "Esfigmomanómetro (tensiómetro)", "Termómetro clínico", "Electroencefalograma (EEG)", "Ultrasonido", "Colposcopio", "Mamógrafo", "Aparato de rayos X", "Ecocardiograma", "Analisador de gases sanguíneos", "Centrífuga de laboratorio", "Hemocitómetro", "Medidor de glucosa en sangre", "Espectrómetro de masas", "Espectrofotómetro", "Centrífuga de microhematocrito", "Espectrofotómetro UV-visible", "Cámara hiperbárica", "Microscopio electrónico", "Microscopio de fluorescencia", "Microscopio de luz polarizada", "Autoclave", "Cámara de flujo laminar", "Crioconservador", "Cámara de crioterapia", "Lámpara de Wood", "Glucometro", "Catéter", "Sonda", "Microscopio confocal", "Monitor fetal", "Tensiometro digital", "Hemodinamómetro", "Aparato de presión positiva continua en las vías respiratorias (CPAP)", "Aparato de anestesia regional controlada (CRA)", "Monitor de presión intracraneal (PIC)", "Monitor de electroencefalografía cuantitativa (QEEG)", "Monitor de presión arterial invasiva (PAI)", "Monitor de presión venosa central (PVC)", "Monitor de gasto cardíaco (MGC)", "Monitor de diuresis horaria (MDH)", "Monitor de gasto urinario (MGU)", "Monitor de gasto intestinal (MGI)", "Monitor de gasto enzimático (MGE)", "Monitor de gasto metabólico (MGM)", "Monitor de gasto lumínico (MGL)", "Monitor de gasto calórico (MGC)", "Monitor de gasto proteico (MGP)", "Monitor de gasto lipídico (MGL)", "Monitor de gasto hidroelectrolítico (MGH)", "Monitor de gasto sanguíneo (MGS)", "Monitor de gasto cardiorrespiratorio (MGCR)", "Monitor de gasto respiratorio (MGR)", "Monitor de gasto renal (MGR)", "Monitor de gasto circulatorio (MGC)", "Monitor de gasto circulatorio sistémico (MGCS)", "Monitor de gasto circulatorio pulmonar (MGCP)", "Monitor de gasto circulatorio cerebral (MGCC)", "Monitor de gasto circulatorio renal (MGCR)", "Monitor de gasto circulatorio mesentérico (MGCM)", "Monitor de gasto circulatorio hepático (MGCH)", "Monitor de gasto circulatorio esplénico (MGCE)", "Monitor de gasto circulatorio periférico (MGCP)", "Monitor de gasto circulatorio cutáneo (MGCC)", "Monitor de gasto circulatorio muscular (MGCM)", "Monitor de gasto circulatorio esquelético (MGCE)", "Monitor de gasto circulatorio dérmico (MGCD)", "Monitor de gasto circulatorio subdérmico (MGCS)", "Monitor de gasto circulatorio subcutáneo (MGCS)", "Monitor de gasto circulatorio intradérmico (MGCI)", "Monitor de gasto circulatorio extracutáneo (MGCE)", "Monitor de gasto circulatorio epidérmico (MGCE)", "Monitor de gasto circulatorio interdérmico (MGCI)", "Monitor de gasto circulatorio intersticial (MGCI)", "Monitor de gasto circulatorio intracutáneo (MGCI)", "Monitor de gasto circulator"]
    for _ in range(Numero_Total):
        aparatos_medicos_aletorios = random.choice(aparatos_medicos )
        Lista.append(aparatos_medicos_aletorios)

def Generar_Fecha_Mismo_Mes(Numero_Total, Lista):
    '''Funcion para generar fechas del mes corriente'''
    fake = Faker()
    current_month = fake.date_time_this_month(before_now=True, after_now=False)
    for _ in range(Numero_Total):
        random_day = fake.date_time_between_dates(current_month, current_month, tzinfo=None)
        Lista.append(random_day.date())
# Ejemplo de uso
'''
Lista_Fecha = []
Generar_Fecha_Mismo_Mes(10, Lista_Fecha)
print(Lista[0])
'''
#Ejemplo

'''
Lista_aparatos_medicos = []
Generar_Tipo_Operacion(10, Lista_aparatos_medicos)
print(Lista_aparatos_medicos)
'''

def Generar_Nombre_cirilico(Numero_Total,Lista):
    '''Funcion para generar los Nombres'''
    for _ in range(Numero_Total):
        Generar_Nombre = fakerru.first_name()
        Lista.append(Generar_Nombre)

def Generar_Cognom_cirilico(Numero_Total,Lista):
    '''Funcion para generar los apellidos'''
    for _ in range(Numero_Total):
        Generar_Cognom = fakerru.last_name()
        Lista.append(Generar_Cognom)

def generar_numero_tse_rusa(Numero_total,Lista):
    numero_tse = "RU"
    for _ in range(Numero_total):
        numero_tse += str(random.randint(0, 9))
        Lista.append(numero_tse)
#Curriculum
def Generar_empresa(Numero_Total, Lista):
    for _ in range(Numero_Total):
        empresa = faker.company()
        Lista.append(empresa)

def generar_empleo(Numero_Total,Lista):
    for _ in range(Numero_Total):
        nombre_empleo = faker.job()
        Lista.append(nombre_empleo)
    
def generar_centro_educativo(Numero_Total,Lista):
    for _ in range(Numero_Total):
        centro_educativo=faker.company() + " " + faker.word(ext_word_list=['Escuela', 'Academia', 'Colegio'])
        Lista.append(centro_educativo)
def habilidad(Numero_Total,Lista1,Lista2):
    habilidades = ["Comunicación efectiva", "Trabajo en equipo", "Resolución de problemas", "Pensamiento crítico", "Creatividad", "Liderazgo", "Adaptabilidad", "Organización", "Empatía", "Toma de decisiones", "Gestión del tiempo", "Negociación", "Capacidad de aprendizaje rápido", "Tolerancia al estrés", "Habilidades técnicas (por ejemplo, programación, diseño gráfico, mecánica)", "Pensamiento analítico", "Orientación al cliente", "Manejo de conflictos", "Flexibilidad cognitiva", "Gestión de proyectos"]
    for _ in range(Numero_Total):
        habilidad=random.choice(habilidades)
        Lista1.append(habilidad)
        Lista2.append(habilidad)
    
def generar_dirreccion(Numero_Total, Lista):
    for _ in range(Numero_Total):
        direccion = faker.address()
        Lista.append(direccion)


