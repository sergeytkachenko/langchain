


 Install Oracle Database on the database server. Installation instructions are available in the
 
[Oracle Database Online Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/index.html) 

 . The “sqlplus” and “impdp” utilities required for restoring the application database from backup are installed with Oracle Database.
 





 Note.
 
 Please refer to the
 
[Oracle Database Online Documentation](https://docs.oracle.com/database/121/nav/portal_16.htm) 

 for more details on Oracle Database clustering.
 




 In Oracle Database, create two database users.
 


* A user with the “
 **admin** 
 ” role, who has maximum access privileges on the database server level. This user will restore the Creatio database from a backup file and assign access permissions.
* A user with the “
 **public** 
 ” role, whose permissions are limited. You will need this user to set up a secure connection to the restored Creatio database using Oracle authentication.



 For more on creating users and access permissions on the database server, see
 
[Oracle Database Online Documentation](https://docs.oracle.com/database/121/SQLRF/statements_8003.htm#SQLRF01503) 

 .
 



 Download and unzip the
 
[archive with the SQL scripts](https://academy.creatio.com/sites/default/files/documents/downloads/Oracle_restore_database_scripts.zip) 

 that are used to restore the database from the Oracle backup file.
 



 By default the Oracle DB backup file is located in the ~\db folder with the Creatio executable files. If the backup file is located not on the Oracle server, it should be located in the network folder with general access.
 



 To restore the database:
 


1. Open the CreateUser.sql and RecompileSchema.sql scripts in the editor and modify the following macros:
 


	1. YOUR\_SCHEMA\_NAME – schema name
	2. YOUR\_SCHEMA\_PASSWORD – schema password
	3. \\your\_server.com\Share – path to the backup (\*.dmp file).
2. Open the backup file in a text editor, find and save the name of the used schema located before the “.SYS\_EXPORT\_SCHEMA” record (Fig. 1).
 





 Fig. 1
 

 The schema name in the backup file
 

![chapter_setup_oracle_find_schema_name.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/deploy_oracle_database/chapter_setup_oracle_find_schema_name.png)
3. Remove the modified scripts on the Oracle server. To create a new schema, execute the following command from the folder with the scripts:
 






```

sqlplus.exe "SYS/SYS_PASSWORD@your_server.com:1521/YOUR_SERVICE_NAME AS SYSDBA" @CreateUser.sql
```


1. SYS\_PASSWORD – a password for authorization on the Oracle server
2. your\_server.com – network address of the Oracle server
3. YOUR\_SERVICE\_NAME – Oracle service name.
4. Run import of the DB backup copy in the created schema:
 






```

impdp "YOUR_SCHEMA_NAME/YOUR_SCHEMA_NAME@//your_server.com:1521/BPMBUILD"
 REMAP_SCHEMA=ORIGINAL_SCHEMA_NAME:YOUR_SCHEMA_NAME
 DIRECTORY=BACKUPDIR DUMPFILE=filename.dmp NOLOGFILE=YES
```


1. YOUR\_SCHEMA\_NAME – the name of the schema specified in the CreateUser.sql
2. your\_server.com – network address of the Oracle server
3. ORIGINAL\_SCHEMA\_NAME – the name of the schema from the backup file (step 2).
4. Consistently run:
 






```

sqlplus.exe "YOUR_SCHEMA_NAME/YOUR_SCHEMA_PASSWORD@your_server.com:1521/YOUR_SERVICE_NAME"
 @tspkg_UtilitiesGlobalTypes.sql
```





 sqlplus.exe "YOUR\_SCHEMA\_NAME/YOUR\_SCHEMA\_PASSWORD@your\_server.com:1521/YOUR\_SERVICE\_NAME"
   

 @tspkg\_UtilitiesGlobalTypes.sql






```

sqlplus.exe "YOUR_SCHEMA_NAME/YOUR_SCHEMA_PASSWORD@your_server.com:1521/ YOUR_SERVICE_NAME"
 @RecompileSchema.sql
```






