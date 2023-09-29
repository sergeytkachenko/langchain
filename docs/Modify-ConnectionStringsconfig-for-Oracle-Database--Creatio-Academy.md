


 The ConnectionStrings.config file in the Creatio root directory stores the connection parameters of the database and external services for your application.
 


### 
 Set up ConnectionStrings.config


1. Go to the root directory of the Creatio application
 **~\WebAppRoot\Creatio** 
 .
2. Open the ConnectionStrings.config file in a text editor.
3. Specify the connection parameters (
 **connectionStrings** 
 ).






 A sample ConnectionStrings.config file.
 



```

<?xml version="1.0" encoding="utf-8"?>
<connectionStrings>
  <add name="db" connectionString="Data Source=(DESCRIPTION =
 (ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = Database server name)(PORT = 1521))) (CONNECT_DATA = (SERVICE_NAME = Oracle service name) (SERVER = DEDICATED)));User Id=Schema name;Password=Schema password;Statement Cache Size = 300" />
  <add name="redis" connectionString="host=Machine name;db=Redis DB number;port=6379;
maxReadPoolSize=10;maxWritePoolSize=500" />
  <add name="defRepositoryUri" connectionString="" />
  <add name="defWorkingCopyPath" connectionString="%TEMP%\%WORKSPACE%" />
  <add name="defPackagesWorkingCopyPath"
 connectionString="%TEMP%\%APPLICATION%\%WORKSPACE%\TerrasoftPackages" />
  <add name="clientUnitContentPath"
 connectionString="%TEMP%\%APPLICATION%\%WORKSPACE%\ClientUnitSrc" />
  <add name="sourceControlAuthPath"
 connectionString="%TEMP%\%APPLICATION%\%WORKSPACE%\Svn" />
</connectionStrings>

```




### 
 Required ConnectionStrings.config settings



 Creatio requires the database and caching server connection parameters for operation.
 


* **name="db"** 
 manages the connection to the restored database, where:
 


	+ Database server name
	 
	 is the network address of the database server.
	+ Oracle service name
	 
	 is the service name.
	+ Schema name
	 
	 is the schema name of the restored database.
	+ Schema password
	 
	 is the schema password of the restored database.



```

 <add name="db" connectionString="Data Source=(DESCRIPTION =
 (ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = Database server name)(PORT = 1521))) (CONNECT_DATA = (SERVICE_NAME = Oracle service name) (SERVER = DEDICATED)));User Id=Schema name;Password=Schema password;Statement Cache Size = 300" />

```
* **name="redis"** 
 manages the interaction with the Redis server.
 






```

  <add name="redis" connectionString="host=Machine name;db=Redis DB number;port=6379;
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
 is the path to the working copy of Creatio custom packages. Fill out this parameter only if you use the SVN version control system. The working copy contains custom packages arranged as directories and files. The built-in Creatio SVN client synchronizes the working copy with the repository of the SVN version control system. Set up this parameter when integrating the version control system. Creatio will use it only in the default development mode; i. e., if the file system development mode is disabled. The default value is a temporary directory, which the operating system may clear. We recommend specifying a custom directory. If you specify an existing Creatio directory, for example, .\Terrasoft.WebApp\Terrasoft.Configuration\Pkg, that may cause compilation errors.
 






```

<add name="defPackagesWorkingCopyPath" connectionString=Path to the working copy of custom packages />
```
* **sourceControlAuthPath** 
 is the path to the authorization data of the built-in client of the SVN version control system (if used): The default value is a temporary directory, which the operating system may clear. If you use a version control system, we recommend specifying the path to a permanent directory in this parameter.
 






```

<add name="sourceControlAuthPath" connectionString=Path to the authorization data of the version storage system (SVN) />
```




