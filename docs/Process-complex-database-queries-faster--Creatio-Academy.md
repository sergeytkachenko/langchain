



 This functionality is available for Creatio version 7.18.4 and later.
 




 Some Creatio database queries take a long time to process, which might affect page loading or task completion time significantly. Such queries are usually called “heavy.” They include:
 


* complex filters in pages and dynamic folders
* complex analytical selections in section dashboards
* complex custom queries implemented using development tools



 You can accelerate the processing of heavy queries by forwarding them to a read-only database replica. This will reduce the load on the main database significantly and free up resources for the activity of users and the operation of other Creatio elements.
 



 To set up the redirection of heavy queries, take the following steps:
 


1. Create a read-only database replica.
2. Configure access to the database replica in Creatio.



 Step 1. Create a database replica
-----------------------------------



 The procedure to create a database replica is DBMS-specific. Learn more about the process in vendor documentation:
 


* [Create a database replica in PostgreSQL](https://www.postgresql.org/docs/current/warm-standby.html) 
 .
* [Create a database replica in Microsoft SQL](https://docs.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver15) 
 .
* [Create a database replica in Oracle](https://docs.oracle.com/cd/B19306_01/server.102/b14228/config_simple.htm#STREP056) 
 .



 Step 2. Set up redirection of heavy queries
---------------------------------------------


1. **Set up redirection** 
 of heavy queries to the database replica. Perform the setup in the
 
 Terrasoft.WebHost.dll.config
 
 file for
 **Creatio .NET Core and .NET 6** 
 and in the
 
 web.config
 
 file for Creatio
 **NET Framework** 
 .
 


	1. Select the
	 
	 UseQueryKinds
	 
	 checkbox.
	 
	
	
	
	
	
	
	```
	
	<add key="UseQueryKinds" value="true" />
	
	```
	2. Add the
	 
	 replicaConnectionStringName="db\_Replica"
	 
	 value to the
	 
	 db general
	 
	 parameter.
	 
	
	
	
	
	
	
	```
	
	<general connectionStringName="db" replicaConnectionStringName="db_Replica" securityEngineType="Terrasoft.DB.MSSql.MSSqlSecurityEngine, Terrasoft.DB.MSSql" executorType="Terrasoft.DB.MSSql.MSSqlExecutor, Terrasoft.DB.MSSql" engineType="Terrasoft.DB.MSSql.MSSqlEngine, Terrasoft.DB.MSSql" metaEngineType="Terrasoft.DB.MSSql.MSSqlMetaEngine, Terrasoft.DB.MSSql" metaScriptType="Terrasoft.DB.MSSql.MSSqlMetaScript, Terrasoft.DB.MSSql" typeConverterType="Terrasoft.DB.MSSql.MSSqlTypeConverter, Terrasoft.DB.MSSql" enableRetryDBOperations="false" retryDBOperationFactoryType="Terrasoft.DB.MSSql.MSSqlRetryOperationFactory, Terrasoft.DB.MSSql" binaryPackageSize="1048576" currentSchemaName="dbo" enableSqlLog="false" sqlLogQueryTimeElapsedThreshold="5000" sqlLogRowsThreshold="100" useOrderNullsPosition="false" maxEntitySchemaNameLength="128" /> 
			
	```
	
	
	
	
	```
	
	<general connectionStringName="db" replicaConnectionStringName="db_Replica" maxEntitySchemaNameLength="128" useOrderNullsPosition="false" sqlLogRowsThreshold="100" sqlLogQueryTimeElapsedThreshold="5000" enableSqlLog="false" currentSchemaName="public" binaryPackageSize="1048576" typeConverterType="Terrasoft.DB.PostgreSql.PostgreSqlTypeConverter, Terrasoft.DB.PostgreSql" metaScriptType="Terrasoft.DB.PostgreSql.PostgreSqlMetaScript, Terrasoft.DB.PostgreSql" metaEngineType="Terrasoft.DB.PostgreSql.PostgreSqlMetaEngine, Terrasoft.DB.PostgreSql" engineType="Terrasoft.DB.PostgreSql.PostgreSqlEngine, Terrasoft.DB.PostgreSql" maxAnsiJoinCount="0" isCaseInsensitive="true" executorType="Terrasoft.DB.PostgreSql.PostgreSqlExecutor, Terrasoft.DB.PostgreSql" securityEngineType="Terrasoft.DB.PostgreSql.PostgreSqlSecurityEngine, Terrasoft.DB.PostgreSql"/> 
	
	```
2. **Configure access** 
 to the database replica in Creatio. To do this, add the
 
 db\_Replica
 
 parameter to the
 
 ConnectionStrings.config
 
 file:
 






```

<add name="db_Replica" connectionString="Data Source=[ Database server name ]; Initial Catalog=[ Database name ]; Persist Security Info=True; MultipleActiveResultSets=True; Integrated Security=SSPI; Pooling = true; Max Pool Size = 100; Async = true" />
		
```




```

<add name="db_Replica" connectionString="Server=[ Database server name ];Port=[ Database server port ];Database=[ Database name ];User ID=[ PostgreSQL user that connects to the database ];password=[ PostgreSQL user password ];Timeout=500; CommandTimeout=400;MaxPoolSiz>
	
```




```

<general connectionStringName="db" replicaConnectionStringName="db_Replica" currentSchemaName=" [SCHEMA NAME] " binaryPackageSize="1048576" typeConverterType="Terrasoft.DB.Oracle.OracleTypeConverter, Terrasoft.DB.Oracle" metaScriptType="Terrasoft.DB.Oracle.OracleMetaScript, Terrasoft.DB.Oracle" metaEngineType="Terrasoft.DB.Oracle.OracleMetaEngine, Terrasoft.DB.Oracle" engineType="Terrasoft.DB.Oracle.OracleEngine, Terrasoft.DB.Oracle" maxAnsiJoinCount="0" isCaseInsensitive="true" executorType="Terrasoft.DB.Oracle.OracleExecutor, Terrasoft.DB.Oracle" securityEngineType="Terrasoft.DB.Oracle.OracleSecurityEngine, Terrasoft.DB.Oracle"/>

```






```

<add name="db_Replica" connectionString="Data Source=(DESCRIPTION = 
 (ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = [ Database server name ])(PORT = 1521))) (CONNECT_DATA = (SERVICE_NAME = [ Oracle service name ]) (SERVER = DEDICATED)));User Id=[ Schema name ];Password=[ Schema password ];Statement Cache Size = 300" />
 			
```




