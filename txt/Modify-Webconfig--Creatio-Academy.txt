


 Generate a unique
 
 machineKey
 
 value for your Creatio application. To do this:
 


1. Download the PowerShell script.
 [Download the script](https://academy.creatio.com/sites/default/files/documents/downloads/UpdateMachineKey.zip) 
 .
2. Run the PowerShell console as an administrator.
3. Specify the path to the root Creatio directory in the PowerShell terminal and run the script. Example of the command to run:
 






```

.\UpdateMachineKey.ps1 "[Path to the root Creatio directory]" 

```



 As a result, the script will generate a unique
 
 machineKey
 
 value in Web.config files located in the root Creatio directory and the Terrasoft.WebApp directory.
 



 Additional Web.config setup for Oracle
----------------------------------------



 After you set up the database connection parameters in the ConnectionStrings.config file for the Oracle database, set up the Web.config configuration file that includes certain configuration parameters required for Creatio to operate as intended.
 



 To set up Web.config:
 


1. Ensure the Creatio website can access the configuration parameters described in the ConnectionStrings.config configuration file. To do this, open the Web.config configuration file in the root Creatio directory and set the
 
 currentSchemaName
 
 attribute of the
 
 general
 
 parameter in the
 
 db
 
 section to the name of the schema specified in the ConnectionStrings.config configuration file.
 






```

<configuration>
    ...
    <terrasoft>
        <db>
            <general ... currentSchemaName="SOME_SCHEMA_NAME_OF_ORACLE_DATABASE" />
        </db>
    </terrasoft>
    ...
</configuration>

```





 where
 
 currentSchemaName
 
 is the name of the Oracle database schema.
2. Save the changes.



 Set up Creatio to work with Oracle 19c
----------------------------------------




 You can set up Creatio to work with Oracle 19c in Creatio version 8.0 Atlas and later. Since version 8.0.2 Atlas, Creatio works with Oracle 19c out of the box.
 




 We recommend using Oracle 19c as Creatio DBMS. Familiarize yourself with Oracle 19c capabilities in the
 [official vendor documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/whats-new.html) 
 . You can use Oracle 19c thanks to the Managed ODAC 12 library.
 





 Note.
 
 We recommend performing the setup on a pre-production environment first. Learn more in developer documentation:
 [Environments](https://academy.creatio.com/documents?id=15201&anchor=title-2124-2) 
 .
 




 In general, the procedure to set up Creatio to work with Oracle 19c consists of the following steps:
 


1. Enable the Managed ODAC 12 library.
 [Read more >>>](#title-3966-1)
2. Update the Oracle DBMS to version 19c.
 [Read more >>>](#title-3966-2)


### 
 Enable the Managed ODAC 12 library



 Make sure that you are using Creatio version 8.0 Atlas or later. If you are using an earlier version, update Creatio. To do this, follow the
 [update guide](https://academy.creatio.com/node/143) 
 .
 



 To
 **enable the Managed ODAC 12 library** 
 :
 


1. Check the Oracle 19c database connector the website uses.
 






```

<configuration>
    ...
    <system.data>
        <DbProviderFactories>
            <add name="Oracle.ManagedDataAccess, Managed Driver" invariant="Oracle.ManagedDataAccess.Client" description="Oracle Data Provider for .NET, Managed Driver" type="Oracle.ManagedDataAccess.Client.OracleClientFactory, Oracle.ManagedDataAccess"/>
        </DbProviderFactories>
    </system.data>
    ...
</configuration>

```
2. Back up the Web.config configuration file in the root Creatio directory.
3. Set up the interaction between the Creatio website and database via the Managed ODAC 12 library. To do this, set the
 
 executorType
 
 parameter in the Web.config configuration file to
 
 Terrasoft.DB.Oracle.OracleManagedExecutor, Terrasoft.DB.Oracle
 
 :
 






```

<configuration>
    ...
    <terrasoft>
        <db>
            <general ... executorType="Terrasoft.DB.Oracle.OracleManagedExecutor, Terrasoft.DB.Oracle" ... />
        </db>
    </terrasoft>
</configuration>

```





 where
 
 executorType
 
 is the library that manages the Creatio database.
4. Set up the interaction between the scheduler and database tables via the Managed ODAC 12 library. To do this, set the
 
 quartz.dataSource.SchedulerDb.provider
 
 key in the Web.config configuration file to
 
 OracleManagedProvider
 
 :
 






```

<configuration>
    ...
    <quartzConfig defaultScheduler="BPMonlineQuartzScheduler">
        <quartz isActive="true">
            ...
            <add key="quartz.dataSource.SchedulerDb.provider" value="OracleManagedProvider" />
        </quartz>
    </quartzConfig>
</configuration>

```





 where
 
 quartz.dataSource.SchedulerDb.provider
 
 is the key that enables the scheduler to interact with database tables.
5. Run Creatio and check the functionality in operation. If you notice issues, restore the Web.config configuration file from backup and repeat the setup.
6. Repeat the setup in the production environment or transfer changes to the production environment. Learn more in developer documentation:
 [Environments](https://academy.creatio.com/documents?id=15201&anchor=title-2124-3) 
 .


### 
 Update the Oracle DBMS to version 19c



 To update the Creatio Oracle DBMS to version 19c, follow the
 [official vendor documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/upgrd/index.html) 
 .
 



 As a result, your Creatio application will use Oracle 19c DBMS.
 




