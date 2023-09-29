


 You can enhance the performance of large-scale Creatio projects (up to several thousand users) through horizontal scaling, i. e., by increasing the number of servers with deployed Creatio applications and setting up workload distribution between them.
 



 The load balancer may be either hardware or software. To work in fault-tolerant mode, use an HTTP/HTTPS traffic balancer that supports the WebSocket protocol. Creatio has been tested on the HAProxy software load balancer. There are cases of successful implementation of other balancers, e. g., Citrix, Cisco, NginX, FortiGate, Microsoft ARR.
 





 Note.
 
 The installation procedure of Marketplace add-ons and custom improvements for an environment that uses a balancer differs from the standard deployment process. Learn more in a separate article:
 [Install applications from the Marketplace](https://academy.creatio.com/documents?id=1835) 
 .
 




 This guide covers horizontal scaling of Creatio using a free open-source load balancer (HAProxy), designed for distributing the load between several application servers.
 





 Note.
 
 Synchronize the server time of the nodes (servers and computers) that run deployed application instances to ensure smooth operation of Creatio.
 




 General deployment procedure
------------------------------


### 
 Creatio .NET Framework



 To deploy Creatio using the horizontal scaling of
 **.NET Framework** 
 application servers:
 


1. Deploy the required number of Creatio application instances in a web farm.
 





 Note.
 
 We recommend specifying identical names in IIS and the Application pool setting for all Creatio instances.
2. Specify identical SQL and Redis databases in the ConnectionStrings.config file for all instances.
 






```

<add name="redis" connectionString="host=DOMAIN.COM;db=0;port=6379;maxReadPoolSize=10;maxWritePoolSize=500"/>
<add name="db" connectionString="Data Source=DOMAIN.COM;Initial Catalog=DatabaseName;Integrated Security=SSPI; MultipleActiveResultSets=True;Pooling-true;Max Pool Size=100"/>
```
3. Add the following key in the <appSettings> block of the application’s Web.config file:
 






```

<add key="TenantId" value="1" />
```





 The “value” number must be identical for all Creatio instances of the web farm.
 





 Attention.
 
 Starting with Creatio version 7.14.1, the <add key="TenantId" value="..."/> key can only be added to the internal Web.config file (Terrasoft.WebApp\Web.config). Adding the key to an external Web.config file may lead to application failures.
4. Generate a unique machineKey value for one of Creatio instances. Learn more in a separate article:
 [Modify Web.config](https://academy.creatio.com/documents?id=2141) 
 . Copy the resulting value and specify it in the Web.config files of each Creatio instance. You can locate the files in the root Creatio folder and the Terrasoft.WebApp folder.
5. Turn on clustering for all schedulers in the <quartzConfig> block of every node's external configuration file (Web.config):
 






```

<add key="quartz.jobStore.clustered" value="true" />
<add key="quartz.jobStore.acquireTriggersWithinLock" value="true" />

```
6. If the instanceId settings collide, specify unique values for each scheduler node.
 



 The
 **ways to specify** 
 unique instanceId values are as follows:
 


	* Add the following string to all schedulers in the <quartzConfig> block of every node’s external configuration file (Web.config):
	 
	
	
	
	
	
	
	```
	
	<add key="quartz.scheduler.instanceId" value="AUTO" />
	
	```
	
	
	
	
	
	
	
	 Attention.
	 
	 The “AUTO” value of the “value” attribute must be uppercase. Otherwise, Creatio will treat the value as the node name, which may lead to errors in the scheduler’s operation.
	 
	
	
	
	
	 As a result, the scheduler will generate the unique node name based on the <node name>+timestamp template.
	* Add unique quartz.scheduler.instanceId values manually.
7. Set the “value” attribute of the quartz.jobStore.clustered setting to “true.”
 






```

<add key="quartz.jobStore.clustered" value="true" />

```
8. Grant access permissions to created application directories for the IUSR user and the user who launches the Application pool in IIS.
9. Set up a load balancer (e. g., HAProxy) to distribute the workload between the deployed application servers.
10. If necessary, set up load balancing for database and session servers.
 





 Note.
 
 Learn more about setting up clustering in the
 [Microsoft SQL](https://docs.microsoft.com/en-us/sql/sql-server/failover-clusters/install/create-a-new-sql-server-failover-cluster-setup?view=sql-server-2017) 
 and
 [Oracle](https://docs.oracle.com/cd/B28359_01/rac.111/b28254/admcon.htm#i1058057) 
 documentation. Learn more about setting up fault tolerance using Redis Cluster in a separate article:
 [Redis Cluster](https://academy.creatio.com/documents?id=2349) 
 .


### 
 Creatio .NET Core



 To deploy Creatio using the horizontal scaling of
 **.NET Core** 
 application servers:
 


1. Deploy the required number of
 [Creatio application instances](https://academy.creatio.com/documents?id=2124) 
 .
2. Specify identical SQL and Redis databases in the
 [ConnectionStrings.config file](https://academy.creatio.com/documents?id=2120) 
 for all instances.
3. Go to the root directory of any Creatio instance and locate the Terrasoft.WebHost.dll file.
4. Run the following command:
 






```

dotnet Terrasoft.WebHost.dll configureWebFarmMode
```





 As a result, configuration files of the current application instance will be updated.
5. Enable clustering for all schedulers in the <quartzConfig> block of every node's external configuration file (Terrasoft.WebHost.dll):
 






```

<add key="quartz.jobStore.clustered" value="true" />
<add key="quartz.jobStore.acquireTriggersWithinLock" value="true" />
```
6. If the instanceId settings collide, specify unique values for each scheduler node.
 



 The
 **ways to specify** 
 unique instanceId values are as follows:
 


	* Add the following string to all schedulers in the <quartzConfig> block of every node’s external configuration file (Terrasoft.WebHost.dll):
	 
	
	
	
	
	
	
	```
	
	<add key="quartz.scheduler.instanceId" value="AUTO" />
	
	```
	
	
	
	
	
	
	
	 Attention.
	 
	 The “AUTO” value of the “value” attribute must be uppercase. Otherwise, Creatio will treat the value as the node name, which may lead to errors in the scheduler’s operation.
	 
	
	
	
	
	 As a result, the scheduler will generate the unique node name based on the <node name>+timestamp template.
	* Add unique quartz.scheduler.instanceId values manually.
7. Set the “value” attribute of the quartz.jobStore.clustered setting to “true.”
 






```

<add key="quartz.jobStore.clustered" value="true" />

```
8. If necessary, set up load balancing for the database and session servers.
9. Copy all configuration files of the current application instance to the root folders of other application instances.
10. Set up a load balancer (e. g., HAProxy) to distribute the workload between the deployed application servers.





 Note.
 
 Learn more about setting up clustering in the DBMS vendor documentation. Learn more about setting up fault tolerance using Redis Cluster in a separate article:
 [Redis Cluster](https://academy.creatio.com/documents?id=2349) 
 .
 




 Install the HAProxy balancer
------------------------------



 The HAProxy load balancer supports a range of free open-source OS. This guide covers one of the simpler methods of deploying HAProxy on the Debian OS via the haproxy.debian.net service.
 


1. Open the installation service page by clicking
 <https://haproxy.debian.net/>
 .
2. Select the OS and its version, as well as the HAProxy version.
 





 Note.
 
 Use the cat /etc/issue command to check the currently installed Debian version.
 




 As a result, the service will generate a set of HAProxy installation commands to run in the Debian OS.
 




 Fig. 1 HAProxy installation commands generated by the haproxy.debian.net service
 

![haproxy_settings_commands.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/app_server_webfarm/haproxy_settings_commands.png)
3. Run the generated commands one after another.



 Set up the HAProxy balancer
-----------------------------



 To set up HAProxy, modify the haproxy.cfg file. Follow this path to locate the file:
 






```

.../etc/haproxy/haproxy.cfg
```




### 
 Primary setup (required)



 Add the sections required for HAProxy operation:
 **frontend** 
 and
 **backend** 
 .
 


#### 
 The frontend section



 Add the following settings to the frontend section:
 **bind** 
 and
 **default\_backend** 
 .
 


* Specify the address and the port that will receive requests distributed by HAProxy in the
 **bind** 
 setting.
* Specify the name that will match the name of the backend section in the
 **default\_backend** 
 option.



 As a result, the setting will look as follows:
 






```

frontend front
maxconn 10000
#Using these ports for binding
bind *:80
bind *:443
#Convert cookies to be secure
rspirep ^(set-cookie:.*)  \1;\ Secure
default_backend creatio
```




#### 
 The backend section



 Add the following required settings to the backend section:
 


* Specify the type of balancing, e. g.,
 **roundrobin** 
 , in the
 **balance** 
 parameter. Learn more about the different types of balancing in the
 [HAProxy documentation](https://cbonte.github.io/haproxy-dconv/configuration-1.5.html#4.2-balance) 
 .
* Use the
 **server** 
 parameter to specify all servers (or nodes) that distribute the load.



 Add a unique “server” parameter that contains the server address, port address, and weight for each server (i. e. the deployed Creatio instance). The server weight enables the balancer to distribute the load based on the physical capabilities of the servers. The higher weight you specify for the server, the more requests it will receive. For example, if you need to distribute the load between 2 Creatio application servers, add 2 “server” parameters to backend:
 






```

server node_1 [server address]:[port] weight
server node_2 [server address]:[port] weight
```





 As a result, the setting will look as follows:
 






```

backend creatio
#set balance type
balance roundrobin
            
server node_1 nodeserver1:80 check inter 10000 weight 2
server node_2 nodeserver2:80/sitename check inter 10000 weight 1

```





 The new settings will be applied as soon as you restart HAProxy. Use the following command to restart HAProxy:
 






```

service haproxy restart
```




### 
 Check the server status



 The HAProxy balancer works with the following server statuses:
 





| 
 Status
  | 
 Description
  |
| --- | --- |
| 
 UP
  | 
 The server is operational.
  |
| 
 UP - transitionally DOWN
  | 
 The server is considered operational at the moment, but the last health check has failed. As a result, the server is currently switching to the DOWN status.
  |
| 
 DOWN - transitionally UP
  | 
 The server is not considered operational at the moment, but the last health check has succeeded. As a result, the server is currently switching to the UP status.
  |
| 
 DOWN
  | 
 The server is not operational.
  |




 Health checks initiate changes in a server’s operational status. The simplest health check requires adding the “check” keyword to the server setup string. Running the health check requires the server’s IP and TCP port. Health check example:
 






```

server node1 ... check
option httpchk GET /Login/NuiLogin.aspx
option httpchk GET /0/ping
```




### 
 Set up web stats (optional)



 To turn on web stats, add a new listen section that contains the following parameters:
 **bind** 
 ,
 **mode http** 
 ,
 **stats enable** 
 ,
 **stats uri** 
 . The section will look as follows:
 






```

listen stats # Define a listen section called "stats"
    bind :9000 # Listen on localhost:9000
    mode http
    stats enable  # Enable stats page
    stats uri /haproxy_stats  # Stats URI
```





 As a result, you will be able to view the web stats of Creatio load balancing in the browser.
 




 Fig. 2 The web stats of the load balancer
 

![load_balancer_stats.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/app_server_webfarm/load_balancer_stats.png)



 To view the stats, follow the path:
 
 balancer address
 
 :9000/haproxy\_stats.
 


### 
 Set up the IP addresses in the audit log for .NET Core (optional)



 With a web farm, user requests reach the servers through a load balancer and/or a proxy server. As such, by default, the
 [audit log](https://academy.creatio.com/documents?id=2320) 
 displays the IP address of the proxy that forwarded the request last, not the actual IP address of the user.
   

 You can configure the audit log so that it displays the actual IP address of the user. To do this:
 


1. Configure the balancer so that each request it forwards to one of the Creatio application instances has a header with “ForwardedForHeaderName” name and the user’s IP address value.
2. Modify the configuration files of Creatio application instances accordingly.
 


	1. Go to Creatio root directory and open appsettings.json.
	2. Edit the “ForwardedHeaders” section so that it reads:
	 
	
	
	
	
	
	
	```
	
	{
	    ...
	    "ForwardedHeaders": {
	        "Enable": true,
	        "ForwardedForHeaderName": "X-Forwarded-For",
	        "KnownProxiesIP": [trusted IP addresses],
			"ForwardLimit": 3
	    }
	    ...
	}
	```
	
	
	
	
	
	 Where:
	 
	
	
	
	 “
	 **Enable** 
	 ” turns on the Forwarded headers processing function in the web application.
	 
	
	
	
	 “
	 **ForwardedForHeaderName** 
	 ” is the name of the header that contains the IP address.
	 
	
	
	
	 “
	 **KnownProxiesIP** 
	 ” is the trusted IP address list. Creatio processes the “
	 **ForwardedHeader** 
	 ” value only if it receives a request from these IP addresses. They сфт belong to the load balancer, reverse proxy, etc. If you leave this value empty, Creatio processes the “ForwardedHeader” value received from any IP address.
	 
	
	
	
	
	
	 Example
	 
	
	
	
	
	```
	"KnownProxiesIP": ["127.0.0.1", "12.34.56.78", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"]
			
	```
	
	
	
	
	
	 “
	 **ForwardLimit** 
	 ” is the limit of IP addresses in the “X-Forwarded-For” processed header. The parameter adds more protection from incorrectly setup proxy servers and malicious requests received from third-party network channels. Proxy servers write their IP addresses to the end of the “X-Forwarded-For” header when forwarding requests. For example, the “X-Forwarded-For” header can have the following IP address chain: ip1, ip2, ip3, ip4. In this case:
	 
	
	
		* ip1 is the client (browser) address.
		* ip2 and ip3 are proxy server addresses.
		* ip4 is the balancer address.
	 If you set “ForwardLimit” to 4, the web server receives all 4 addresses. If you set it to 3, the web server receives only the last 3 IP addresses, i. e., ip2, ip3, and ip4.
	 
	
	
	
	 The default value is 3. If you have the “
	 **KnownProxiesIP** 
	 ” parameter set up, you can set the “
	 **ForwardLimit** 
	 ” parameter to null.
	3. Repeat steps a-b for all Creatio application instances in your web farm.




