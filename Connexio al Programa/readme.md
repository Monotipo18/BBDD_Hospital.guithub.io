# Connectar al Programa final
##### *It just works*
Primer explicarem una mica el sistema que hem usat per a fer que qualsevol pot accedir al codi, el qual és '*Secure SHELL*' o SSH, que és una eina que es connecta a un servidor per a controlar el seu Shell, el que llaurem és que quan iniciï una connexió amb un usuari específic ens obri el script de Python, és ens dona centralització, la qual cosa comporta que actualitzar i mantenir el programa és més fàcil, també és més fàcil a l'hora que l'usuari treballi, ja que el SSH és una cosa que ve per defecte estalviant instal·lació i també recursos, ja que serà el servidor el que s'encarregui d'executar el programa.

### Configuració del Servidor SSH
És bastant fàcil, així que el tutorial serà molt breu

Primer obrirem la configuració d'arrencada amb el següent comando
```bash
nano /rutade/tuusario/.profile
```
Exemple
```bash
nano /home/guest/.profile
```
Ens anirem a la primera línia del codi i posarem això:

```bash
trap '' 2
if [ -n "$SSH_CONNECTION" ]; then
    #source /home/guest/.venv/bin/activate #Descomenta aquesta línia si té un virtualenv
    python /home/guest/script/script.py
    logout
fi
trap 2
```

El '*trap*' ens serveix per a evitar que l'usuari surto amb un ctrl+c, com diu, atrapa a l'usuari
```bash
trap '' 2
    #codigo
trap 2
```
Després tenim un IF per a comprovar si està entrant en local o en SSH si és l'últim executarà el codi
```bash
if [ -n "$SSH_CONNECTION" ]; then
    #codigo
fi
```

I per a l'últim tenim en si el que volem fer en aquest exemple, primer entrem en el virtualenv i després executem el script, i si l'usuari surt del script tanca sessió automàticament.
```bash
    source /home/guest/.venv/bin/activate #Descomenta aquesta línia si té un virtualenv
    python /home/guest/script/script.py
    logout
```
Una cosa que afegir, gràcies al IF si som administrador podem entrar amb un altre usuari i iniciar normal dins del guest, per si hem de canviar alguna cosa, afegit això, ara simplement fem ssh guest@ip.del.host.ssh i automàticament s'iniciés el codi