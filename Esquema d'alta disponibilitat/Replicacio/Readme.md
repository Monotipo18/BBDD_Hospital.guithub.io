# Replicacio
## Projecte Intermodular
## Index


Añadir el repositorio PostgreSQL al sistema
dnf install -y [https://download.postgresql.org/pub/r...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbEhHdHV3dllrN0lfbFJTVVVvc25KcEU0VXhWd3xBQ3Jtc0tselBvRG5VZVNmTVBjN1h0Sk1DRDJmVzNOa2NkZnpTVXJqT3ZJcFdBMlF0YnZfU1VnOG5vTXQ5V0tndWQzZ0VYeHZDY2JsaEVmT2g1SXhHLUxQU0JteklSZkpEVDRJOXpVT2FQMDl0dlB2U1dmWVZnMA&q=https%3A%2F%2Fdownload.postgresql.org%2Fpub%2Frepos%2Fyum%2Freporpms%2FEL-9-x86_64%2Fpgdg-redhat-repo-latest.noarch.rpm&v=GIsD1BgFnWc)

disable the built-in PostgreSQL module
sudo dnf -qy module disable postgresql

install PostgreSQL 15 on both Primary and secondary servers.
dnf install -y postgresql15-server postgresql15

initialize the database
/usr/pgsql-15/bin/postgresql-15-setup initdb

start the PostgreSQL service and enable it to start automatically on boot. 
systemctl enable --now postgresql-15

Edit the PostgreSQL configuration file on the primary server to allow replication.
vi /var/lib/pgsql/15/data/postgresql.conf

listen_addresses = '*'
wal_level = replica
max_wal_senders = 10
wal_keep_segments = 8
hot_standby = on

Save and exit the configuration file.

create a replication user on the primary server.
sudo su - postgres
psql
CREATE USER replicator REPLICATION LOGIN ENCRYPTED PASSWORD 'replicator_password';
\q

add a rule in the host-based authentication file
vi /var/lib/pgsql/15/data/pg_hba.conf
host    replication     replicator      192.168.100.75/32       trust

Now save and exit.

restart the PostgreSQL service
systemctl restart postgresql-15

Firewall
add a new rule to the firewall of both primary and secondary servers
firewall-cmd --zone=public --add-port=5432/tcp --permanent
firewall-cmd --reload

Now that you have created the replication user and configured the primary server, you can move on to configuring the secondary server.

Change as postgres user and run the pg_basebackup command.
sudo su - postgres
pg_basebackup -h 192.168.100.72 -U replicator -Fp -Xs -P -R -D /var/lib/pgsql/15/data/

execute systemctl command to start and enable on boot the PostgreSQL service on the secondary server.
systemctl enable --now postgresql-15

At this point, you have configured the secondary server and enabled asynchronous replication.

Verification
To test the replication setup, insert some data into the primary database and verifying that it appears on the secondary server.

su - postgres
psql -c "CREATE TABLE test1 (id serial PRIMARY KEY, data text);"
psql -c "INSERT INTO test (data) VALUES ('test data');"
psql -c "SELECT * FROM test;"

If the replication is working correctly, the SELECT statement should return the inserted row on both the primary and secondary servers.

You can do additional test by performing a 'WRITE' action from the 'SLAVE' server.

psql -c "CREATE TABLE test1 (id serial PRIMARY KEY, data text);"

The result should be 'Cannot execute CREATE TABLE' as shown here.

To verify the streaming status of a secondary server,
psql -x -c "SELECT * FROM pg_stat_replication;"

To view the status of the WAL receiver process on a secondary server in PostgreSQL, you can use this command

psql -x -c "select * from pg_stat_wal_receiver;"

Failover
To perform a failover from a primary PostgreSQL server to a secondary server, you need to promote the secondary server by running the pg_ctl promote command as postgres user.

The pg_ctl promote command is used to initiate the failover process. It signals the standby server to take over as the new primary server and start accepting read-write connections. 

To enable WAL log hints, you can set the parameter in the postgresql.conf file.
vi /var/lib/pgsql/15/data/postgresql.conf
wal_log_hints = on

SECONDARY
On your secondary server, verify that it's still in a read-only state by running the following command.
psql -c "SELECT pg_is_in_recovery();"

/usr/pgsql-15/bin/pg_ctl promote
