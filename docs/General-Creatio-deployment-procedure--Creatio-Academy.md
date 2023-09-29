


 This guide covers all steps needed to deploy and set up Creatio on-site on Windows or Linux, as well as links to detailed descriptions of each step.
 



 Deploy the Creatio application on Windows
-------------------------------------------



 The general procedure to deploy Creatio on-site is as follows:
 


1. Deploy the Creatio caching server (Redis).
 [Read more >>>](https://academy.creatio.com/docs/user/on_site_deployment/caching_server)
2. Deploy the database. Note that this step is DBMS-dependent.
 [Read more >>>](https://academy.creatio.com/docs/user/on_site_deployment/database_server)
3. Enable and install the required Windows components.
 [Read more >>>](https://academy.creatio.com/documents?id=2081)
4. Install the latest Windows updates.
5. Create and set up the application website using IIS.
 [Read more >>>](https://academy.creatio.com/documents?id=2136)
6. Modify the ConnectionStrings.config file. Note that this step is DBMS-dependent.
 [Read more >>>](https://academy.creatio.com/docs/user/on_site_deployment/net_framework_application_server_on_windows)
7. Modify the Web.config file.
 [Read more >>>](https://academy.creatio.com/documents?id=2141)



 After installing Creatio, perform
 **additional setup** 
 to ensure correct operation of all its components.
 


* Set up websockets.
 [Read more >>>](https://academy.creatio.com/documents?id=1631)
* Switch Creatio from HTTP to HTTPS.
 [Read more >>>](https://academy.creatio.com/documents?id=1632)
* Deploy and set up global search in Creatio.
 [Read more >>>](https://academy.creatio.com/documents?id=1712)
* Set up the machine learning service.
 [Read more >>>](https://academy.creatio.com/documents?id=1935)
* Set up integrations and Internet access for additional functions. For example, the data enrichment service, social media integration, or Google synchronization.
 [Read more >>>](https://academy.creatio.com/docs/user/on_site_deployment/deployment_additional_setup)
* Set up bulk emails (only for configurations with Marketing Creatio).
 [Read more >>>](https://academy.creatio.com/documents?id=1777)



 Deploy the Creatio application on Linux
-----------------------------------------


### 
 Deploy the Creatio .NET 6 application on Linux




 .NET 6 application deployment is available for Creatio 8.0.8 and later.
 




 The general procedure to deploy Creatio on-site is as follows:
 


1. Prepare the Creatio setup files.
 [Read more >>>](https://academy.creatio.com/documents?id=2450)
2. Deploy the database server.
 [Read more >>>](https://academy.creatio.com/documents?id=2121)
3. Deploy the Creatio caching server (Redis).
 [Read more >>>](https://academy.creatio.com/documents?id=2108)
4. Modify the ConnectionStrings.config file.
 [Read more >>>](https://academy.creatio.com/documents?id=2450#title-263-2)
5. Deploy the Creatio application server.
 [Read more >>>](https://academy.creatio.com/documents?id=2451)



 If you are going to run Creatio directly
 **on the local machine** 
 :
 


1. Install .NET 6, a GDI+ compatible API for UNIX-like operating systems, and development libraries and header files for GNU C.
 [Read more >>>](https://academy.creatio.com/documents?id=2451#title-2649-2)
2. Run the Creatio application server.
 [Read more >>>](https://academy.creatio.com/documents?id=2451#title-2649-3)



 If you are going to run Creatio
 **in a Docker container** 
 :
 


1. Make Redis accessible from the Docker container.
 [Read more >>>](https://academy.creatio.com/documents?id=2451#title-2649-5)
2. Install Docker.
 [Read more >>>](https://academy.creatio.com/documents?id=2451#title-2649-6)
3. Create a Dockerfile.
 [Read more >>>](https://academy.creatio.com/documents?id=2451#title-2649-7)
4. Build and run the Docker image.
 [Read more >>>](https://academy.creatio.com/documents?id=2451#title-2649-8)





 Note.
 
 The procedure for running a PostgreSQL server in Docker is covered in the
 [Docker documentation](https://hub.docker.com/_/postgres) 
 .
 



### 
 Deploy the Creatio .NET Core application on Linux





 Attention.
 
 The deprecated .NET Core platform will be retired in Creatio version 8.1. We recommend platform .Net 6 for deploying Creatio version 8.0.8 and later.
 




 The general procedure to deploy Creatio on-site is as follows:
 


1. Prepare the Creatio setup files.
 [Read more >>>](https://academy.creatio.com/documents?id=2120)
2. Deploy the database server.
 [Read more >>>](https://academy.creatio.com/documents?id=2121)
3. Deploy the Creatio caching server (Redis).
 [Read more >>>](https://academy.creatio.com/documents?id=2108)
4. Modify the ConnectionStrings.config file.
 [Read more >>>](https://academy.creatio.com/documents?id=2120#title-263-2)
5. Deploy the Creatio application server.
 [Read more >>>](https://academy.creatio.com/documents?id=2148)



 If you are going to run Creatio directly
 **on the local machine** 
 :
 


1. Install .NET Core, a GDI+ compatible API for UNIX-like operating systems, and development libraries and header files for GNU C.
 [Read more >>>](https://academy.creatio.com/documents?id=2148#title-247-2)
2. Run the Creatio application server.
 [Read more >>>](https://academy.creatio.com/documents?id=2148#title-247-3)



 If you are going to run Creatio
 **in a Docker container** 
 :
 


1. Make Redis accessible from the Docker container.
 [Read more >>>](https://academy.creatio.com/documents?id=2148#title-247-5)
2. Install Docker.
 [Read more >>>](https://academy.creatio.com/documents?id=2148#title-247-6)
3. Create a Dockerfile.
 [Read more >>>](https://academy.creatio.com/documents?id=2148#title-247-7)
4. Build and run the Docker image.
 [Read more >>>](https://academy.creatio.com/documents?id=2148#title-247-8)





 Note.
 
 The procedure for running a PostgreSQL server in Docker is covered in the
 [Docker documentation](https://hub.docker.com/_/postgres) 
 .
 





