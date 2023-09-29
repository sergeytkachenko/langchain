


 The ConnectionStrings.config file in the Creatio root directory stores the connection parameters of the database and external services for your application.
 


### 
 Set up ConnectionStrings.config


1. Go to the root directory of the Creatio application
 **~\WebAppRoot\Creatio** 
 .
2. Open the ConnectionStrings.config file in a text editor.
3. Specify the connection parameters (
 **connectionStrings** 
 ) of your site.






 A sample ConnectionStrings.config file.
 



```

<?xml version="1.0" encoding="utf-8"?> 

<connectionStrings> 

<add name="db" connectionString="Data Source=Database server name; Initial Catalog=Database name; Persist Security Info=True; MultipleActiveResultSets=True; Integrated Security=SSPI; Pooling = true; Max Pool Size = 100; Async = true" /> 

<add name="redis" connectionString="host=Redis server machine name;db=Redis DB number;port=6379; maxReadPoolSize=10;maxWritePoolSize=500" /> <Integrated Security=SSPI" /> 

<add name="defRepositoryUri" connectionString="" /> 
 
<add name="defWorkingCopyPath" connectionString="%TEMP%\%WORKSPACE%" /> 
 
<add name="defPackagesWorkingCopyPath" connectionString="%TEMP%\%APPLICATION%\%WORKSPACE%\TerrasoftPackages" /> 
 
<add name="clientUnitContentPath" connectionString="%TEMP%\%APPLICATION%\%WORKSPACE%\ClientUnitSrc" /> 

<add name="sourceControlAuthPath" connectionString="%TEMP%\%APPLICATION%\%WORKSPACE%\Svn" /> 

<add name="elasticsearchCredentials" connectionString="User=ElasticSearch username; Password=ElasticSearch password;" /> 

</connectionStrings>

```




### 
 Required ConnectionStrings.config settings



 Creatio requires the database and caching server connection parameters for operation.
 


* **name="db"** 
 manages the connection to the restored database.
 



 You can see the database server name (
 **Data Source** 
 ) in the authorization window while connecting to the server using Microsoft SQL Server Management Studio (Fig. 1).
 




 Fig. 1 The SQL server authorization window
 

![scr_setup_server_name.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/modify_config_for_MSSQL/scr_setup_server_name.png)


 The database name (Initial Catalog) must match the
 
 Database
 
 field value you specified when restoring the database.
 



 By default, Creatio uses
 **Windows authentication** 
 (Integrated Security) based on the SPPI interface to connect to the database server. To ensure successful connection to the database, specify the Windows user on whose behalf you will connect to the database server.
 






```

<add name="db" connectionString="Data Source=Database server name; 
Initial Catalog=Database name; 
Persist Security Info=True; MultipleActiveResultSets=True; 
Integrated Security=SSPI; Pooling = true; Max Pool Size = 100; Async = true" />
```





 If you want to log in to the database server using the
 **Microsoft SQL user credentials** 
 , create the credentials on the Microsoft SQL server and specify them in the ConnectionStrings.config file. Replace the
 **Integrated Security=SSPI** 
 variable with the
 **User ID** 
 and
 **Password** 
 variables in the database connection string (add name="db"):
 






```

<add name="db" connectionString="Data Source=TSW\MSSQL2014; 
Initial Catalog=7.10.2.1416_SalesEnterprise_Demo; 
Persist Security Info=True; MultipleActiveResultSets=True; 
User ID=Sup; Password=password; Pooling = true; Max Pool Size = 100; Async = true" />

```
* **name="redis"** 
 manages the interaction with the Redis server.
 






```

<add name="redis" connectionString="host=Redis server machine name;db=Redis DB number;port=6379;
maxReadPoolSize=10;maxWritePoolSize=500" />
```


### 
 Optional ConnectionStrings.config settings



 The external service connection parameters are optional. Fill them out only if your Creatio configuration requires it. For example, do that if you want to integrate the version control system.
 


* **tempDirectoryPath** 
 is the path to the temporary directory the package installation mechanism requires:
 






```

<add name="tempDirectoryPath" connectionString=Path to the temporary directory the package installation mechanism requires />
```
* **defPackagesWorkingCopyPath** 
 is the path to the working copy of Creatio custom packages. Fill out this parameter only if you use the SVN version control system. The working copy contains custom packages organized as directories and files. The built-in Creatio SVN client synchronizes the working copy with the repository of the SVN version control system. Set up this parameter when integrating the version control system. Creatio will use it only in the default development mode; i. e., if the file system development mode is disabled. The default value is a temporary directory, which the operating system may clear. We recommend specifying a custom directory. If you specify an existing Creatio directory, for example, .\Terrasoft.WebApp\Terrasoft.Configuration\Pkg, that may cause compilation errors.
 






```

<add name="defPackagesWorkingCopyPath" connectionString=Path to the working copy of custom packages />
```
* **sourceControlAuthPath** 
 is the path to the authorization data of the built-in client of the SVN version control system (if used): The default value is a temporary directory, which the operating system may clear. If you use a version control system, we recommend specifying the path to a permanent directory in this parameter.
 






```

<add name="sourceControlAuthPath" connectionString=Path to the authorization data of the version storage system (SVN) />
```
* **Influx** 
 manages the interaction with the site analytics collection service. Fill out this parameter only if you need to collect the functionality use analytics for debugging.
 






```

<add name="influx" connectionString="url=Site analytics collection service address; user=User on whose behalf the connection is established; password=Password; batchIntervalMs=5000" />
```
* **clientPerformanceLoggerServiceUri** 
 manages the interaction with the logging service. Fill out this parameter only if you need to collect the data about how Creatio pages load.
 






```

<add name="clientPerformanceLoggerServiceUri" connectionString="Logging service address" />
```
* **messageBroker** 
 manages the interaction with the RabbitMQ service. Fill out this parameter only if you need to set up horizontal load scaling using RabbitMQ.
 






```

<add name="messageBroker" connectionString="amqp://MessageBroker username:Password@Address of the server where the service is deployed/Virtual server name" /> 
```




