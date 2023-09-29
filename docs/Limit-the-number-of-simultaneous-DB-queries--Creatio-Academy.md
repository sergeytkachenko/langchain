



 This functionality is available in Creatio version 8.0.2 and higher for MSSQL PostgreSQL DBMS.
 




 You can improve application performance by limiting the amount of processor resources (threads) that a heavy database query can consume. This will reduce the impact of resource-intensive procedures on the work of users. Such requests are generated both in the background, for example, when executing business processes or integrations, or by users, for example, sorting registries by an aggregate column. This article describes how to configure restrictions for on-site applications. For cloud applications, these restrictions are applied automatically after upgrading to version 8.0.2.
 



 The thread limiting mechanism works most effectively on servers with 4 or more processor cores.
 



 The general procedure for setting restrictions consists requires steps:
 


1. Enable resource limit in configuration files.
 [Read more >>>](#)
2. Set resource limit in Creatio settings.
 [Read more >>>](#)



 Enable resource limit for requests
------------------------------------



 Limiting the number of threads is disabled in Creatio by default. You can enable it in the ApplyMaxDopHintToUserQueries section of the configuration file:
 


* For
 **NET Framework** 
 , these are web.config files located in the root folder of the application and in the TerrasoftWebApp folder.
* For
 **.NET Core and .NET 6** 
 , this is the Terrasoft.WebHost.dll.config file located in the root folder of the application.





 Configuration file line example
 




```

<configuration>
  …
   <appsettings>
    …
     <add key="ApplyMaxDopHintToUserQueries" value="true">
    …
   </appsettings>
  …
</configuration>
```





 Set resource limit for requests
---------------------------------



 The system setting “Number of MaxDopQueryHint Threads” (code “MaxDopHintThreadsCount”) is intended to throttle the resources that can be used for queries to the database. To set a resource limit:
 


1. Open the system designer by clicking the
 ![btn_system_designer00001.png](https://academy.creatio.com/docs/sites/default/files/documentation/user/ru/sys_settings_lookups/BPMonlineHelp/add_lookups/btn_system_designer00001.png)
 button in the upper right corner of the application.
2. In the
 
 System settings
 
 group, click
 
 System settings
 
 .
3. Open the “MaxDopQueryHint thread count” system setting (code “MaxDopHintThreadsCount”)..
4. In the
 
 Default value
 
 field, set the resource limit. We recommend using from a quarter to a half of the total number of available threads, assuming one thread corresponds to one processor core. In this way, you prevent all available threads from being occupied by resource-intensive operations.
 


 Note.
 
 The limit of half of the available number of threads allows you to perform all the necessary processes and tasks, while not slowing down the work of users. For the number of threads between 4 and 8 threads, we recommend setting the limit between 2 and 4 (i.e. half the number of available threads).



 As a result, the load on the resources of the database server processors is significantly reduced, which allows you to perform resource-intensive operations without affecting the work of Creatio users.
 




