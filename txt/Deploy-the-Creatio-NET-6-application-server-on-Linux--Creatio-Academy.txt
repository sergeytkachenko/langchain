



 .NET 6 application deployment is available for Creatio 8.0.8 and later.
 




 Before you deploy the server, take the following steps:
 


* Prepare the Creatio setup files.
 [Read more >>>](https://academy.creatio.com/documents?id=2120)
* Deploy the database server.
 [Read more >>>](https://academy.creatio.com/documents?id=2121)
* Deploy the Creatio caching server (Redis).
 [Read more >>>](https://academy.creatio.com/documents?id=2108)
* Modify the ConnectionStrings.config file.
 [Read more >>>](https://academy.creatio.com/documents?id=2122)





 Note.
 
 Learn more about running a PostgreSQL server in Docker in the
 [Docker documentation](https://hub.docker.com/r/library/postgres/) 
 .
 




 Method 1. Deploy Creatio .NET 6 on Linux directly
---------------------------------------------------



 To deploy the Creatio application server:
 


* Install .NET 6, a GDI+ compatible API for non-Windows operating systems, and development libraries and header files for GNU C.
 [Read more >>>](https://academy.creatio.com/documents?id=2124)
* Run the Creatio application server.
 [Read more >>>](https://academy.creatio.com/documents?id=2125)


### 
 Install .NET 6 and other Creaito dependencies


1. Download the packages-microsoft-prod package:
 






```

wget -q https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
```
2. Log in as root:
 






```

sudo su
```
3. Install the downloaded package:
 






```

dpkg -i packages-microsoft-prod.deb
```
4. Update the package lists:
 






```

apt-get update
```
5. Install the APT transport for downloading via the HTTP Secure protocol:
 






```

apt-get install apt-transport-https
```
6. Update the package lists:
 






```

apt-get update
```
7. Install .NET 6:
 






```

apt-get install dotnet-sdk-6.0
```
8. Install a GDI+ compatible API for non-Windows operating systems:
 






```

apt-get install -y libgdiplus
```
9. Install development libraries and header files for GNU C:
 






```

apt-get install -y libc6-dev
```
10. Log out from your root session:
 






```

exit
```


### 
 Run the Creatio application server





 Note.
 
 If you are deploying the .NET 6 development environment with access via HTTP, modify the Terrasoft.WebHost.dll.config file in the Creatio root directory before you run Creatio. Set the “add key” parameter to the following:
 






```

<add key="CookiesSameSiteMode" value="Lax" />
```





 This ensures correct operation both via HTTP and HTTPS. However, the mobile app will not be operational if you use this setting.
 




 To run Creatio:
 


1. Open the directory that contains Creatio setup files:
 






```

cd /path/to/application/directory/
```
2. Run the .NET 6 server:
 






```

COMPlus_ThreadPool_ForceMinWorkerThreads=100 dotnet Terrasoft.WebHost.dll
```



 Creatio HTTP version will be available on port 5000.
 



 Creatio HTTPS version will be available on port 5002.
 





 Note.
 
 To log in to newly deployed Creatio, use the default Supervisor user account. It is highly recommended to change the Supervisor password immediately. Login: Supervisor; password: Supervisor.
 




 Method 2. Deploy Creatio .NET 6 on Linux using Docker
-------------------------------------------------------



 Use this deployment method to run a compartmentalized Creatio application. We assume that you have installed the Redis sever, deployed the Creatio database, and set up the ConnectionStrings.config file using the instructions in the previous steps.
 



 To deploy Creatio application server using Docker:
 


* Make Redis accessible from the Docker container.
 [Read more >>>](https://academy.creatio.com/documents?id=2126)
* Install Docker.
 [Read more >>>](https://academy.creatio.com/documents?id=2127)
* Create a Dockerfile.
 [Read more >>>](https://academy.creatio.com/documents?id=2128)
* Build and run a Docker image.
 [Read more >>>](https://academy.creatio.com/documents?id=2129)





 Attention.
 
 We recommend deploying Creatio using Docker for development and testing environments only. Avoid using Docker for the production environment before we implement support for Creatio updates in Docker (planned for upcoming releases).
 



### 
 Configure the Creatio caching server (Redis)


1. Open
 **redis.conf** 
 in a text editor as root. For example, use the Nano text editor:
 






```

sudo nano /etc/redis/redis.conf
```
2. Locate the “
 **bind 127.0.0.1 ::1** 
 ” entry. Replace the entry with “
 **bind 0.0.0.0** 
 ” to listen to all available IPV4 interfaces.
3. Save changes and exit the editor.
4. Restart the Redis server:
 






```

sudo systemctl restart redis-server
```


### 
 Install Docker



 To install Docker, run:
 






```

sudo apt-get install docker
```




#### 
 Create a Dockerfile



**/path/to/application/directory/** 
 is the directory that contains unpacked Creatio installation files.
 


1. Open the Creatio directory:
 






```

cd **/path/to/application/directory/**
```
2. Create a Dockerfile using a text editor. For example, use the Nano text editor:
 






```

nano Dockerfile
```
3. Insert the following code:
 






```

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS base
EXPOSE 5000 5002
RUN apt-get update && \
apt-get -y --no-install-recommends install \
libgdiplus \
libc6-dev && \
apt-get clean all && \
rm -rf /var/lib/apt/lists/* /var/cache/apt/*
WORKDIR /app
COPY . ./
FROM base AS final
WORKDIR /app
ENV ASPNETCORE_ENVIRONMENT Development
ENV TZ US/Eastern
ENV COMPlus_ThreadPool_ForceMinWorkerThreads 100
ENTRYPOINT ["dotnet", "Terrasoft.WebHost.dll"]
```
4. Press Ctrl+O to save the changes.
5. Press Ctrl+X to exit the editor.


#### 
 Build and run a Docker image





 Note.
 
 If you are deploying the .NET 6 development environment with access via HTTP, modify the Terrasoft.WebHost.dll.config file in the Creatio root directory before you run the Docker image. Set the “add key” parameter to the following:
 






```

<add key="CookiesSameSiteMode" value="Lax" />
```




 This ensures correct operation both via HTTP and HTTPS. However, the mobile app will not be operational if you use this setting.
 

 Build a Docker image:
 






```

docker build -f Dockerfile -t creatioimg .
```





 Run the docker image:
 






```

docker run -p http_port_number:5000 -p https_port_number:5002  -d --dns=DNS_server_ip --dns-search=DNS_address_suffix -v /logspath/mycreatio:/app/Logs --name Creatio creatioimg
```





**http\_port\_number** 
 is a port number. Docker will serve the HTTP version on this port
 



**https\_port\_number** 
 is a port number. Docker will serve the HTTPS version on this port
 



**DNS\_server\_ip** 
 is the IP address of a DNS server that enables the container to resolve Internet domains. You can use multiple
 **--dns** 
 flags for multiple DNS servers.
 



**DNS\_address\_suffix** 
 is a DNS search domain that enables the container to search for non-fully-qualified hostnames. You can use multiple
 **--dns-search** 
 flags for multiple DNS search domains.
 





 Note.
 
 Add the --restart=always flag to the command make a persistent Docker container.
 




 Creatio HTTP version will be available on port
 **http\_port\_number** 
 .
 



 Creatio HTTPS version will be available on port
 **https\_port\_number** 
 .
 





 Note.
 
 To log in to a newly deployed application, use the default Supervisor user account. It is highly recommended to change the Supervisor password immediately. Login: Supervisor; password: Supervisor.
 




 Configure Creatio .NET 6 for HTTPS
------------------------------------



 Before you start working in Creatio via HTTPS, take the following steps:
 


1. Obtain a \*.pfx digital certificate from the certification center.
 


 Note.
 
 If you use a self-signed certificate, Creatio mobile application cannot connect to the Creatio website due to security policies of mobile applications.
2. Go to Creatio root directory and open appsettings.json.
3. Specify your website address, path to the certificate, and certificate password in the “Https” block.





 Example of the “Https” block in appsettings.json
 




```

"Https": {
    "Url": "https://::5002",
    "Certificate": {
    "Path": "C:\\Projects\\site\\20210215_103239\\localhost.pfx",
    "Password": "Password"
    }
}
```







 Note.
 
 You can specify both relative and absolute path to the certificate. The absolute path must be JSON compatible.
 





