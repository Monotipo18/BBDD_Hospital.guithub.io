# Tipus de documents per l’AGPD i requisits d'encriptacio.

A continuacio trobareu els documents que ha de tenir un hospital per cumplir amb el Reglament General de Protecció de dades o RGPD.
Els diferenciarem en 3 nivell de requisits d'encriptacio.

## 1 Requisits Alts.

Aquest documents son especialments relevants donada la sensivilitat que contenen. Els enmascararem amb Data masking dins de la base de dades juntament amb SSL per tenir encriptada la conecció entre el servidor i la BDD. A mes restringirem el acces a les dades depenent de la teva profecio dins de l'hospital.

Dins d'aquest requisits trobem documentacio com:

    - Politica de Protecció de dades personals.
    - Registre de medicaments.
    - Registre de activitats de tractament.
    - Consentiments Médics.
    - Historial clinics.
    - Contractes de procesament de dades.
    - Evaluacio de impacte en la protecció de dades (EIPD) per dades de salud sensibles.
    - Avis de privacitat dels Empleats.
    - Registre de la violació de seguretat de Dades
    - Politica de privacitat especifica per l'atencio medica.
    - Registre de acces a dades médiques.
    - Registre de formació en proteccio de dades.
    - Cláusulas Contractuales Estándar para la Transferencia de Datos Personales a Responsables

## 2 Requisits Intermitgos.

Aquest documents son relevants amb informació personal important. Tot i que l'informacio que contenen els documents es menys relevant que els anteriors, encara s'han d'encriptar dades personals importants com DNI, telefons, noms, etc. Utilitzarem datamasking i el SSL com en l'anterior.

Dins d'aquests requisits trobarem documentacio com:

    - Programa de retencio de dades.
    - Formulari de consentiment patern.
    - Acord de tractament de dades del proveidor.
    - Formulari de notificació de violació de seguretat de dades a les autoritats de control
    - Formulari de notificacio de violacio de seguretat de dades als interesats.
    - Descripcio del lloc de delegat de proteccio de dades
    - Registre de consentiment informat
    - Politica de retencio de registres medics.

## 3 Requisits Baixos.

Aquest documents son necesaris i obligatoris, pero poc relevants, per tant tindran poca necesitat d'encriptació. Utilitzarem datamasking minimament i l'encriptacio SSL

Dins d'aquest requisits trobem documentacio com:

    - Avis de Privacitat.
    - Politica de retencio de dades.
    - Formulari de consentiment de l'interesat.
    - Procediment de resposta a la violació de seguretat de dades.
    - Llistat d'activitats de tractament.


### Webgrafia
https://advisera.com/es/articulos/lista-de-documentos-obligatorios-requeridos-por-el-rgpd-de-la-ue/