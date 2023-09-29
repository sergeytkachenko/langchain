


 Use one of two database configurations to deploy Creatio:
 


* Use a remote DBMS (recommended)
* Use a local PostgreSQL server.



 If you already have a PostgreSQL server set up, skip to step II.
 



 If you have already set up sysadmin (with privileges to log in, create and modify databases) and public (unprivileged) user roles, skip to step III.
 





 I. Install PostgreSQL
-------------------------



 PostgreSQL setup files are available for download at
 
[postgresql.org](https://www.postgresql.org/download/) 

 .
 





 Note.
 
 High-availability PostgreSQL configurations have not been tested with Creatio. Please refer to the
 
[PostgreSQL documentation](https://www.postgresql.org/docs/9.5/high-availability.html) 

 for details on PostgreSQL clustering.
 






 II. Create PostgreSQL user
------------------------------



 A fresh installation of PostgreSQL Server is not ready for deploying Creatio immediately. If you plan to use a fresh installation of PostgreSQL Server, you need to create a user that can log in to the database using a password and has sufficient privileges to create and update a database. By default, no such user will be available.
 



 We recommend to create two database users in PostgreSQL:
 


* A user with the “
 **sysadmin** 
 ” role who has maximum access privileges on the database server level. This user will restore the Creatio database from a backup file and assign access permissions. These instructions use
 **pg\_sysadmin** 
 as a placeholder username, but you can set the username to any value.
* A user with the “
 **public** 
 ” role whose permissions are limited. You will need this user to set up a secure connection to the restored Creatio database using PostgreSQL authentication. These instructions use
 **pg\_user** 
 as a placeholder username, but you can set the username to any value.



 To create the two PostgreSQL users:
 


1. Open the Command Prompt.
2. Navigate to the PostgreSQL software install folder:
 






```

cd /D "\\path\to\PostgreSQL\folder"
```




	* **\\path\to\PostgreSQL\folder** 
	 – the path to the PostgreSQL software install folder.
3. Navigate to the folder with the Command Line Tools component:
 






```

cd bin
```
4. Enter the DB connection password in the environment variable.
 






```

set PGPASSWORD=pg_password
```




	* **pg\_password** 
	 – password of the
	 **postgres** 
	 user for connecting to the PostgreSQL server.
5. Run PostgreSQL shell as
 **postgres** 
 :
 






```

psql.exe --username postgres
```
6. Create a sysadmin user, e. g.
 **pg\_sysadmin** 
 :
 






```

CREATE USER pg_sysadmin;
```




	* **pg\_sysadmin** 
	 – placeholder name for a sysadmin user. The sysadmin will restore the Creatio database from a backup file and assign access permissions.
7. Make
 **pg\_sysadmin** 
 a system administrator:
 






```

ALTER ROLE pg_sysadmin WITH SUPERUSER;
```
8. Allow
 **pg\_sysadmin** 
 to log in:
 






```

ALTER ROLE pg_sysadmin WITH LOGIN;
```
9. Set a password for
 **pg\_sysadmin** 
 :
 






```

ALTER ROLE pg_sysadmin WITH PASSWORD 'pg_syspassword';
```




	* **pg\_syspassword** 
	 – sysadmin user password for connecting to the PostgreSQL server.
10. Create a public user, e. g.
 **pg\_user** 
 :
 






```

CREATE USER pg_user;
```




	* **pg\_user** 
	 – placeholder name for a public user. This user will set up a connection to the restored Creatio database.
11. Allow
 **pg\_user** 
 to log in:
 






```

ALTER ROLE pg_user WITH LOGIN;
```
12. Set a password for
 **pg\_user** 
 :
 






```

ALTER ROLE pg_user WITH PASSWORD 'pg_password';
```




	* **pg\_password** 
	 – public user password for connecting to the PostgreSQL server.
13. Exit the PostgreSQL shell:
 






```

\q
```





 III. Restore PostgreSQL database
------------------------------------



 To restore a PostgreSQL database from a backup file, you will need
 **psql.exe** 
 and
 **pg\_restore.exe** 
 utilities. Both are part of the Command Line Tools PostgreSQL component that comes with the PostgreSQL Server. They are located in the PostgreSQL software install folder.
 



 If you plan to use a remote PostgreSQL database without installing the PostgreSQL Server on your machine, take the following steps:
 


1. Get a PostgreSQL binary package. Binary packages are available for download at
 
[postgresql.org](https://www.postgresql.org/download/) 

 .
2. Select the Command Line Tools component during installation. Selecting the other components is optional.



 To restore the Creatio database from a backup file:
 


1. Open Command Prompt.
2. Navigate to the PostgreSQL software install folder:
 






```

cd /D "\\path\to\PostgreSQL\folder"
```




	* **\\path\to\PostgreSQL\folder** 
	 – the path to the PostgreSQL software install folder.
3. Navigate to the folder with executables:
 






```

cd bin
```
4. Enter the DB connection password in the environment variable:
 






```

set PGPASSWORD=pg_syspassword
```




	* **pg\_syspassword** 
	 – sysadmin user password for connecting to the PostgreSQL server.
5. Create a database where the backup data will be restored.
 



**For Creatio version 7.16.3 or higher:** 







```

psql.exe --host pg_server_ip --port pg_server_port --username=pg_sysadmin -–command "CREATE DATABASE pg_dbname_ceatio WITH OWNER = pg_user ENCODING = 'UTF8' CONNECTION LIMIT = -1"
```




	* **pg\_server\_ip** 
	 – PostgreSQL server address.
	* **pg\_server\_port** 
	 – PostgreSQL server port.
	* **pg\_sysadmin** 
	 – user for connecting to the PostgreSQL server. The user must have either superuser (administrator) privileges or “CREATE DATABASE” privileges.
	* **pg\_user** 
	 – the application will use this user's credentials to connect to the database. You can specify any user when creating the database. To change the user data, follow
	 **step 10** 
	 of this instruction.
**For Creatio version 7.16.0 – 7.16.2:** 







```

psql.exe --host pg_server_address --port pg_server_port --username=pg_sysadmin -–command "CREATE DATABASE pg_dbname_creatio WITH OWNER = pg_user ENCODING = 'UTF8' CONNECTION LIMIT = -1"
```




	* **pg\_server\_address** 
	 – PostgreSQL server address.
	* **pg\_server\_port** 
	 – PostgreSQL server port.
	* **pg\_sysadmin** 
	 – user for connecting to the PostgreSQL server. The user must have either superuser (administrator) privileges or “CREATE DATABASE” privileges.
	* **pg\_user** 
	 – the “public” user who will be granted permission to use and update the Creatio database
6. If you are using AWS RDS:
 


	1. Download the
	 
	[ChangeTypesOwner.sql](https://academy.creatio.com/sites/default/files/documents/downloads/ChangeTypesOwner.sql) 
	
	 script.
	2. In the script, replace the “postgres” value with a valid Postgres username.
	3. Run the updated ChangeTypesOwner.sql script.
7. Restore the Creatio database from the backup file:
 



**For Creatio version 7.16.3 or higher:** 







```

pg_restore --host pg_server_ip --port pg_server_port --username=pg_sysadmin --dbname=pg_dbname_creatio --no-owner --no-privileges --verbose \\path\to\db.backup
```




	* **pg\_server\_ip** 
	 – PostgreSQL server address.
	* **pg\_server\_port** 
	 – PostgreSQL server port.
	* **pg\_sysadmin** 
	 – user for connecting to the PostgreSQL server. The user must have either superuser (administrator) privileges or sufficient access permissions to run the
	 **pg\_restore** 
	 utility.
	* **pg\_dbname\_creatio** 
	 – name of the PostgreSQL DB to insert backup tables.
**For Creatio version 7.16.0 – 7.16.2:** 







```

pg_restore.exe --host pg_server_address --port pg_server_port --username=pg_sysadmin --dbname=pg_dbname_creatio --verbose \\path\to\db.backup
```




	* **pg\_server\_address** 
	 – PostgreSQL server address.
	* **pg\_server\_port** 
	 – PostgreSQL server port.
	* **pg\_sysadmin** 
	 – user for connecting to the PostgreSQL server. The user must have either superuser (administrator) privileges or sufficient access permissions to run the pg\_restore utility.
	* **pg\_dbname\_creatio** 
	 – name of the PostgreSQL DB to insert backup tables.
8. Download the
 
[CreateTypeCastsPostgreSql.sql file](https://academy.creatio.com/sites/default/files/documents/downloads/CreateTypeCastsPostgreSql.sql) 

 .
9. Execute type conversion:
 






```

psql.exe --host pg_server_ip --port pg_server_port --username=pg_sysadmin --dbname=pg_dbname_creatio --file=\\path\to\CreateTypeCastsPostgreSql.sql
```




	* **pg\_server\_ip** 
	 – PostgreSQL server address.
	* **pg\_server\_port** 
	 – PostgreSQL server port.
	* **pg\_sysadmin** 
	 – user with administrator privileges for connecting to the PostgreSQL server.
	* **pg\_dbname\_creatio** 
	 – name of the PostgreSQL DB where the instructions will be executed.
	* **\\path\to\CreateTypeCastsPostgreSql.sql** 
	 – path to the downloaded CreateTypeCastsPostgreSql.sql file.
10. Creatio version
 **7.16.3** 
 supports changing the owner of the database and database objects to a non-administrator user (i. e. not a superuser). To do this, use the ChangeDbObjectsOwner script.
 [Download the script](https://academy.creatio.com/sites/default/files/documents/downloads/ChangeDbObjectsOwner.sql) 
 .
 



 To restore the database from a backup as a regular user:
 


	1. Change the owner of the database:
	 
	
	
	
	
	
	
	```
	
	psql.exe --host pg_server_ip --port pg_server_port --username=pg_sysadmin --dbname=pg_dbname –-command "ALTER DATABASE pg_dbname_creatio OWNER TO pg_user"
	```
	
	
	
	
		* **pg\_server\_ip** 
		 – PostgreSQL server address.
		* **pg\_server\_port** 
		 – PostgreSQL server port.
		* **pg\_sysadmin** 
		 – user for connecting to the PostgreSQL server. The user must have either administrator (superuser) privileges or “CREATE DATABASE” privileges.
		* **pg\_user** 
		 – new database owner.
		* **pg\_dbname\_creatio** 
		 – the name of the database whose owner is changed.
	2. Change the owner of the database objects:
	 
	
	
	
	
	
	
	```
	
	psql.exe --host pg_server_ip --port pg_server_port --username=pg_sysadmin --dbname=pg_dbname_creatio --file=\\path\to\ChangeDbObjectsOwner.sql --variable owner=pg_user --variable ON_ERROR_STOP=1
	```
	
	
	
	
		* **pg\_server\_ip** 
		 – PostgreSQL server address.
		* **pg\_server\_port** 
		 – PostgreSQL server port.
		* **pg\_sysadmin** 
		 – user for connecting to the PostgreSQL server. The user must have either administrator (superuser) privileges or “CREATE DATABASE” privileges.
		* **pg\_user** 
		 – new database owner.
		* **pg\_dbname\_creatio** 
		 – the name of the database whose owner is changed.
		* **\\path\to\ChangeDbObjectsOwner.sql** 
		 – path to the downloaded ChangeDbObjectsOwner.sql file.
 Skip this step to leave the default owner of the database and database objects, which is the user who runs the
 **pg\_restore** 
 utility (usually
 **postgres** 
 )




