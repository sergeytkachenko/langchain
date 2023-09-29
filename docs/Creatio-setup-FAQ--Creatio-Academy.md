






 Which Internet Information Services (IIS) components are required for Creatio?
------------------------------------------------------------------------------------



 To ensure the correct operation of Creatio on-site, enable the following components in the Windows
 
 Programs and Features
 
 menu:
 


1. .NET Framework 3.5:
 


	1. Windows Communication Foundation Non-HTTP Activativation
	2. Windows Communication Foundation HTTP Activation
2. .NET Framework 4.7.2


1. ASP.NET 4.7.2
2. For WCF Services:
 


	* HTTP Activation
	* Message Queuing (MSMQ) Activation
	* Named Pipe Activation
	* TCP Activation
	* TCP Port Sharing
	 
	
	
	
	
	
	 Note.
	 
	 Microsoft .Net Framework 4.7 or higher – for version 7.11.1 – 7.13.1, Microsoft .Net Framework 4.7.2 – for version 7.13.2 or higher;



 Additionally, IIS services are key component for operation of websites and web applications deployed on Windows Server. Enable the following IIS components:
 


1. On the "Web Management Tools” tab:
 


	1. IIS Management Console
	2. IIS Management Script and Tools
	3. IIS Management Service
2. On the "World Wide Web Services" tab:


1. For the Application Development Features component:
 


	* All ASP.NET elements
	* All .NET Extensibility elements
	* ISAPI extensions;
	* ISAPI Filters
	* WebSocket Protocol
	* For the Common HTTP Features component:
	* Default Document
	* HTTP Errors
	* HTTP Redirection
	* Static Content
	* For the "Health and Diagnostics” component:
	* Custom Logging
	* HTTP Logging
	* Logging Tools
	* Request Monitor
	* For the "Security” component:
	* Request filtering
	* IP and Domain Restriction






 How do I switch from HTTP to HTTPS?
----------------------------------------



 The detailed procedure for switching from HTTP to HTTPS is covered in a
 
separate article.








 Which account is used when you first log in to the system?
---------------------------------------------------------------



 After the successful deployment of Creatio on-site, log in with these credentials: user - Supervisor, password - Supervisor.
 






 Does the number of active Creatio users affect the number of Microsoft SQL Server?
---------------------------------------------------------------------------------------



 The number Microsoft SQL Server users does not depend on the number Creatio users, though depends on the number of servers with databases. Please see the
 
[System requirements](https://academy.creatio.com/documents?product=base&ver=7&id=1263) 

 for on-site deployment
 




