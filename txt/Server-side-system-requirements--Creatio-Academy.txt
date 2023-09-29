


 The following components are
 **required** 
 for any Creatio on-site application (Fig. 1):
 


* **Web server** 
 , which is also going to be Creatio
 **application server**
* **Database server** 
 with the chosen database management system (DBMS)
* **Session storage server** 
 (Redis), also known as “
 **caching server** 
 ”





 Fig. 1
 

 Creatio basic infrastructure
 

![eng_deployment_infrastructure_simple.png](/docs/sites/en/files/images/Setup_and_Administration/Server-side_system_requirements/7_18/eng_deployment_infrastructure_simple.png)



**Optional components** 
 include:
 


* **Version control server** 
 (SVN) – recommended for development environments. It lets the developers manage versions and changes of the Creatio configuration (eg., rollback, merge versions, etc).
* **Load balancers** 
 for the application, database, and caching servers for fault-tolerant configurations (Fig. 2).





 Fig. 2
 

 Creatio fault-tolerant infrastructure
 

![eng_deployment_infrastructure_fault-tolerant_cluster.png](/docs/sites/en/files/images/Setup_and_Administration/Server-side_system_requirements/7_18/eng_deployment_infrastructure_fault-tolerant_cluster.png)



 Several functions, such as global search, deduplication, and machine learning require deployment of additional
 **containerization** 
 (operating-system-level virtualization) infrastructure. Implementing the containerization (operating-system-level virtualization) is required for the following Creatio services:
 


* machine learning
* data enrichment
* bulk email service
* global search
* deduplication
* Exchange Listener





 General guidelines
----------------------



 All system components should be functional in a virtual environment. The list of officially supported cloud/virtual platforms:
 


* Amazon Web Services
* Microsoft Azure / Hyper-V
* VMware vCloud Director / vSphere





 Note.
 
 Compatibility with other cloud / virtual platforms is not guaranteed.
 




 Active system component instances must be placed in a single location (data center / server room / office building, etc.). Placing backup components in remote locations when implementing protection against catastrophic events is acceptable.
 



 All components should function in their dedicated operating systems. Merging components is possible, but not recommended.
 



 To organize a DBMS cluster, you can use either a shared file storage or separate disk space of cluster nodes.
 



 The version control server (SVN) is optional. You only need it in case of configuration version control.
 



 The load balancer is an optional component, which may be useful, if:
 


* there is an increased network load on the application servers
* application servers are deployed in a fault-tolerant configuration (web farm)



 The load balancer may be either hardware or software. To work in fault-tolerant mode, use the HTTP/HTTPS traffic balancer that supports the WebSocket protocol. Creatio has been tested on HAproxy and MS ARR (Microsoft Advanced Request Routing) software load balancers. There are known cases where other balancers like Citrix, Cisco, NginX, FortiGate were successfully implemented.
 






 Connection channels
------------------------



**IIS – SQL:** 



* the capacity of 10Mb/sec per 100 active users
* delays no more than 15-20 ms



**IIS – user:** 



* minimum 256 Kb/sec per 1 active user
* recommended 512 Kb/sec per 1 active user
* formula: 30kByte/sec \* (total number of users working at a time) \* 10%



**Input/output** 
 :
 


* IIS; 100 IOPS per 1000 active users
* SQL: 1000 IOPS per 1000 active users.



**Requirements for sending marketing emails** 
 (Marketing Creatio):
 



 The recommended speed of DB disks depends on the number of recipients.
 


* Audience of up to 1 mln recipients in an email or above 1 mln recipients per month – minimum 300 IOPS, < 8 ms.
* Audience from 1 mln to 2 mln recipients in an email or above 3 mln recipients per month – minimum 500 IOPS, < 8 ms.
* Audience from 2 mln to 5 mln recipients in an email or above 5 mln recipients per month – minimum 1000 IOPS, < 7 ms.







 Requirements to servers for the Exchange Listener synchronization service
-------------------------------------------------------------------------------



 Exchange Listener processes requests by separate handlers simultaneously serving 40 active mailboxes each.
 



 You specify the number of handlers when installing the microservice component. It depends on the planned number of mailboxes.
 



 One processor requires 30% of the 1GHz processor time and 850 Mb of RAM (disk storage is not used).
 





 Software requirements
-------------------------





|  |  |
| --- | --- |
| 

 Component
 
 | 

 Software
 
 |
| 
 Web server
 

 (.NET Framework application)
  | 
 Windows Server 2012 R2 and up
 

 IIS
 

 .Net framework 4.7.2
  |
| 
 Web server
 

 (.NET Core application)
  | 
 Linux Debian 10–11
 

 .NET Core version 3.1
 

 GDI+ compatible API on non-Windows operating systems
 

 Development libraries and header files for GNU C
  |
| 
 Database server (Windows)
  | 
 Windows Server 2012 R2 and up
 

 MSSQL 2016 and up, or
 

 Oracle 11g and up, or
 

 PostgreSQL 11 and up
  |
| 
 Database server (Linux)
  | 
 Linux Debian 10–11
 

 PostgreSQL 11 and up
  |
| 
 Caching server
  | 
 Linux Debian 10–11; Redis Server 4.0 and up
  |
| 
 Load balancer server
  | 
 Linux Debian 10–11; HAproxy
  |
| 
 Version control system server (SVN)
  | 
 Linux Debian 10–11; SVN
  |
| 
 Containers
  | 
 Linux Debian 10–11; Docker; Kubernetes
  |





