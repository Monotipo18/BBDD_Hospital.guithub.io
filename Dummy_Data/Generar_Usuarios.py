from Funciones_Login import *
#100 Medicos
Insercion_Medicos=100
Insercion_infermeres=200
Insercion_persones_neteja=100
Insercion_persones_adm=50
Insercion_Paciente=50000
for i in range(Insercion_Medicos):
    User_Med=(f"MedUsr{i}")
    Contraseña="P@ssw0rd"
    print(User_Med)
    Registro(User_Med,Contraseña,"MEDICO")

#200 infermeres
for i in range(Insercion_infermeres):
    User_Med=(f"infUsr{i}")
    Contraseña="P@ssw0rd"
    print(User_Med)
    Registro(User_Med,Contraseña,"INFERMER/A")

#Personal Limpieza
for i in range(Insercion_persones_neteja):
    User_Med=(f"NetUsr{i}")
    Contraseña="P@ssw0rd"
    print(User_Med)
    Registro(User_Med,Contraseña,"PERSONAL NATEJA")

for i in range(Insercion_Paciente):
    User_Med=(f"PacUsr{i}")
    Contraseña="P@ssw0rd"
    print(User_Med)
    Registro(User_Med,Contraseña,"PERSONAL NATEJA")